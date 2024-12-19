# Exercise 1: Log File Analysis System

import pandas as pd


df = pd.read_json('sample-dataset-1.json')

def high_priority_warnings(df):
    l1=[]
    for i in range(len(df)):
        if df.iloc[i]['metrics']['cpu_usage'] > 80:
            l1.append(df.iloc[i]['server_id'])

    print(f'Servers with CPU usage above 80% {l1}')
    return df[(df['status']=='warning') & (df['priority']=='high')]


def unique_server_id(df):
    return set(df['server_id'])

def sort_log_timestamp(df):
    return df.sort_values(by='timestamp', ascending=True, ignore_index=True)

def sort_by_priority(df):
    cf = df.copy()
    cf['priority'] = cf['priority'].replace('high',2)
    cf['priority'] = cf['priority'].replace('medium',1)
    cf['priority'] = cf['priority'].replace('low',0)
    return sorted(cf,key= lambda x: x[priority])


def summary_report(df):
    event_df = df.groupby(['event_type','priority'])['timestamp'].count().reset_index()
    unique_events = f'Unique Event Types are {set(df['event_type'])}'
    usage = 0
    for i in range(len(df)):
        usage = usage + df['metrics'][i]['cpu_usage']

    avg_usage = f'The Average Usage of CPU Across Servers is {usage/len(df)}'
    return event_df, unique_events, avg_usage

if __name__ =='__main__' :
    print(summary_report(df))
