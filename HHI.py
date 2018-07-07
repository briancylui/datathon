import csv, itertools, random, math,sys
import pandas as pd
import numpy as np
import collections
import pickle


df = pd.read_csv(r"../datasets/flight_traffic.csv",usecols=[3, 5, 4, 1])
# Change the months for relevant quarter

def data_process(start, end):
	test_data = df[(df['month'] >= start) & (df['month'] <= end)]
	test = test_data.groupby(["origin_airport", "destination_airport", "airline_id"]).size().reset_index(name="outbound_flight")
	test1 = test_data.groupby(["origin_airport", "destination_airport"]).size().reset_index(name="total")
	test1['zip'] = list(zip(test1.origin_airport, test1.destination_airport))
	test['combined'] = list(zip(test.origin_airport, test.destination_airport, test.outbound_flight))
	test['zip'] = list(zip(test.origin_airport, test.destination_airport))
	airport_test1 = {k: g["combined"].tolist() for k,g in test.groupby("zip")}
	airport_test_total1 = {k: g["total"] for k,g in test1.groupby("zip")}
	return airport_test1, airport_test_total1

HHIs = collections.defaultdict(list)

# print(airport_test4)

def HHI(airport, airline):
	N = len(airline)
	total = sum(n for _, n in airline)
	index = 0
	for _, n in airline:
		index += (float(n) / total) ** 2
	print(airport, index)

def normalized_HHI(k, v, dic):
	N = len(v)
	total = dic[k]
	val = 0
	for elem in v:
		val += (float(elem[2]) / total) ** 2
	index = float(val - 1./N) / (1 - 1./N) if N > 1 else 1
	return (k, index)

a, b = data_process(0, 12)

for i in range(0, 4):
	data, dic = data_process(3*i, 3+3*i)
	for k, v in a.iteritems():
		if tuple(k) in data:
			res = normalized_HHI(k, data[k], dic)
			HHIs[k].append(res[1])
		else:
			HHIs[k].append(-1)


print(HHIs)
with open('HHI_route.pickle', 'wb') as handle:
    pickle.dump(HHIs, handle, protocol=pickle.HIGHEST_PROTOCOL)