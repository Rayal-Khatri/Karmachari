import pandas as pd
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
import os
import django
from django.db import connection


DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def get_prediction(user_id):
    # Load the dataset into a pandas dataframe

    if os.path.isfile(os.path.join(DATA_PATH, 'dataset.csv')):
        # Load the dataset into a pandas dataframe
        df = pd.read_csv(os.path.join(DATA_PATH, 'dataset.csv'))
    else:
        return None
    # Filter the dataset to only include rows for the selected employee
    selected_employee_data = df.loc[df["user_id"] == int(user_id)]

    # Filter out rows with "Leave", "Absent", and "Holiday" status
    selected_employee_data = selected_employee_data.loc[(selected_employee_data["status"] != "Leave") &
                                                        (selected_employee_data["status"] != "Absent") &
                                                        (selected_employee_data["status"] != "Holiday")]

    # Map dayOfQuestion to day_numeric
    selected_employee_data["day_numeric"] = selected_employee_data["dayOfQuestion"].apply(lambda x: pd.to_datetime(x, format="%A").dayofweek + 1)

    # Map status to a binary value (0 for Present, 1 for Late)
    selected_employee_data["status_binary"] = selected_employee_data["status"].apply(lambda x: 0 if x == "Present" else 1)

    X = selected_employee_data[["day_numeric"]]
    X.columns = ["day_numeric"]
    y = selected_employee_data["status_binary"]
    regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    regressor.fit(X, y)

    # Get the current day of the week (as a string)
    today = datetime.now().strftime("%A")

    # Get the numeric value of tomorrow's day of the week
    tomorrow_numeric = (datetime.now() + timedelta(days=1)).strftime("%w")

    # Map tomorrow's day of the week to a string
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    tomorrow = days[int(tomorrow_numeric)]

    # Make a prediction for tomorrow's status
    prediction = regressor.predict(selected_employee_data[["day_numeric"]])

    # Get the name of the employee
    employee_name = selected_employee_data["name"].unique()[0]

    # Return the prediction
    return prediction[0]*100,employee_name
