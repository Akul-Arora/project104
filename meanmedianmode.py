import csv
import pandas as pd
import statistics

df=pd.read_csv("data.csv")
case_list=df["cases"].to_list()

case_mean=statistics.mean(case_list)
case_median=statistics.median(case_list)
case_mode=statistics.mode(case_list)

print("mean=", case_mean)
print("median=", case_median)
print("mode=", case_mode)