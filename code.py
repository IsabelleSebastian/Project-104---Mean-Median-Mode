import statistics
import pandas as px

data = px.read_csv("data.csv") 

# gets all data in the "Weight" column and creates a list --> tolist()
d = data["Weight"].tolist()

mean = statistics.mean(d)
median = statistics.median(d)
mode = statistics.mode(d)

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)