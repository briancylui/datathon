import csv, itertools, random, math,sys
import pandas as pd
import numpy as np
import collections

df = pd.read_csv(r"../datasets/flight_traffic.csv",usecols=[3, 4, 1])
# Change the months for relevant quarter
test = df[(df['month'] >= 1) & (df['month'] <= 6)]
test = test.groupby(["origin_airport", "airline_id"]).size().reset_index(name="outbound_flight")
test['combined'] = list(zip(test.airline_id, test.outbound_flight))

airport_test = {k: g["combined"].tolist() for k,g in test.groupby("origin_airport")}

def HHI(airport, airline):
	N = len(airline)
	total = sum(n for _, n in airline)
	index = 0
	for _, n in airline:
		index += (float(n) / total) ** 2
	print(airport, index)

def normalized_HHI(airport, airline):
	N = len(airline)
	total = sum(n for _, n in airline)
	val = 0
	for _, n in airline:
		val += (float(n) / total) ** 2
	index = float(val - 1./N) / (1 - 1./N) if N > 1 else 1
	print(airport, ": ", index)

for l in airport_test:
	normalized_HHI(l, airport_test[l])

print("data read")


# print(df)