import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv
import pandas as pd
df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()
def randommean(counter):
	dataset = []
	for i in range(counter):
		randomindex = random.randint(0,len(data)-1)
		value = data[randomindex]
		dataset.append(value)
	mean = statistics.mean(dataset)
	return mean
meanlist = []
for i in range(100):
	setofmeans = randommean(30)
	meanlist.append(setofmeans)
standarddeviation = statistics.stdev(meanlist)
mean = statistics.mean(meanlist)
print ("Standard Deviation:", standarddeviation)
print ("Mean:", mean)
firststdev, firststdevend = mean - standarddeviation, mean + standarddeviation
secondstdev, secondstdevend = mean - (2*standarddeviation), mean + (2*standarddeviation)
thirdstdev, thirdstdevend = mean - (3*standarddeviation), mean + (3*standarddeviation)
