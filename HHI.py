import csv, itertools, random, math,sys
import pandas as pd
import numpy as np
import collections
import pickle


df = pd.read_csv(r"../datasets/flight_traffic.csv",usecols=[3, 4, 1])
# Change the months for relevant quarter
test1 = df[(df['month'] >= 1) & (df['month'] <= 3)]
test2 = df[(df['month'] >= 3) & (df['month'] <= 6)]
test3 = df[(df['month'] >= 6) & (df['month'] <= 9)]
test4 = df[(df['month'] >= 9) & (df['month'] <= 12)]
test_a = test1.groupby(["origin_airport", "airline_id"]).size().reset_index(name="outbound_flight")
test_a['combined'] = list(zip(test_a.airline_id, test_a.outbound_flight))
airport_test1 = {k: g["combined"].tolist() for k,g in test_a.groupby("origin_airport")}

test_b = test2.groupby(["origin_airport", "airline_id"]).size().reset_index(name="outbound_flight")
test_b['combined'] = list(zip(test_b.airline_id, test_b.outbound_flight))
airport_test2 = {k: g["combined"].tolist() for k,g in test_b.groupby("origin_airport")}

test_c = test3.groupby(["origin_airport", "airline_id"]).size().reset_index(name="outbound_flight")
test_c['combined'] = list(zip(test_c.airline_id, test_c.outbound_flight))
airport_test3 = {k: g["combined"].tolist() for k,g in test_c.groupby("origin_airport")}

test_d = test4.groupby(["origin_airport", "airline_id"]).size().reset_index(name="outbound_flight")
test_d['combined'] = list(zip(test_d.airline_id, test_d.outbound_flight))
airport_test4 = {k: g["combined"].tolist() for k,g in test_d.groupby("origin_airport")}
HHIs = collections.defaultdict(list)



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
	return (airport, index)

for l in airport_test1:
	res = normalized_HHI(l, airport_test1[l])
	HHIs[res[0]].append(res[1])
for l in airport_test2:
	res = normalized_HHI(l, airport_test2[l])
	HHIs[res[0]].append(res[1])

for l in airport_test3:
	res = normalized_HHI(l, airport_test3[l])
	HHIs[res[0]].append(res[1])

for l in airport_test4:
	res = normalized_HHI(l, airport_test4[l])
	HHIs[res[0]].append(res[1])

with open('HHI.pickle', 'wb') as handle:
    pickle.dump(HHIs, handle, protocol=pickle.HIGHEST_PROTOCOL)