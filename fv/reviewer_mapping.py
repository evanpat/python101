import pandas as pd
import numpy as np

name_list = pd.read_csv('name_list.csv', header=None)
fvp_user = pd.read_csv('fvp_user.csv') 


#print(name_list.head())

def find_user_id(first_name):
    for i, row in fvp_user.iterrows():
        if first_name in row.values:
            return row[2]
        
    return ""

def process_row(row):
    for i in range(name_list.shape[1]):
        if i == 0:
            continue
        if not pd.isna(row[i]):
            #print(f"Reviewer: {row[0]}, ReviewerId: {find_user_id(row[0])}, Reviewee:{row[i]} RevieweeId: {find_user_id(row[i])}")
            print(f"insert into pr_reviewer_map values ({find_user_id(row[0])}, {find_user_id(row[i])})")

name_list.apply(process_row, axis=1)
