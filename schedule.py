import pandas as pd
import datetime as dt
from parse import *

start = "1/11/2022"
schedule_str = "C N P D D D D N P N P D D D N P D D D D N P N P D N P N P 6/4"

schedule = pd.DataFrame(columns=[
    "Subject", "Start Date", "Start Time",
    "End Date", "End Time", "All Day Event"
])
start = parse("{day:d}/{month:d}/{year:d}", start).named
start = dt.date(**start)
schedule_str = schedule_str.split()

for event in schedule_str:
    params = {}
    if event == "C":
        params = {
            "Subject": "Corrido",
            "Start Date": start,
            "Start Time": "7:00 AM",
            "End Date": start,
            "End Time": "7:00 PM"}
    elif event == "N":
        params = {
            "Subject": "Noche",
            "Start Date": start,
            "Start Time": "7:00 PM",
            "End Date": start + dt.timedelta(days = 1),
            "End Time": "7:00 AM"}
    elif event == "P":
        params = {
            "Subject": "Posturno",
            "Start Date": start,
            "End Date": start,
            "All Day Event": "True"}
    elif event == "D":
        params = {
            "Subject": "Descanso",
            "Start Date": start,
            "End Date": start,
            "All Day Event": "True"}
    else:
        event_time = parse("{time1}/{time2}", event).named
        params = {
            "Subject": event,
            "Start Date": start,
            "Start Time": event_time['time1'] + ":00 AM",
            "End Date": start,
            "End Time": event_time['time1'] + ":00 PM"}
    schedule = pd.concat([schedule, pd.Series(params).to_frame().T])
    start = start + dt.timedelta(days = 1)
schedule.to_csv("lau_schedule.csv")
