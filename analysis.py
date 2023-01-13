import numpy as np
import pandas as pd
import matplotlib.pylab as plt

# Read the CSV file
df = pd.read_csv("dataset.csv")
print(df.head(10))

# Find the total number of runs Kohli has scored
total_runs = df["Runs"].sum()
no_of_matches = len(df["Runs"])
print(f"total no of runs kohli has scored in {no_of_matches} matches: ", total_runs)

# Average of number of runs he has scored
avg_runs = df["Runs"].mean()
print(f"Average score of Kohli in {no_of_matches} matches is: ", int(avg_runs))

# Number of matches he has played at different positions
# note -> .uniques() method on a list returns a list of all unique elem
# .map({create a dict that maps something with something})
positions = df["Pos"].unique()
print(positions)

df["Pos"] = df["Pos"].map({
    3.0 : "Batting at 3",
    4.0 : "Batting at 4",
    2.0 : "Batting at 2",
    1.0 : "Batting at 1",
    7.0 : "Batting at 7",
    5.0 : "Batting at 5",
    6.0 : "Batting at 6",
})
print(df[["Runs", "Pos", "Opposition"]].head())


# => i.e freq calculation e.g "Pos" == 3.0 how many times
pos_counts = df["Pos"].value_counts()
print(pos_counts)
print(type(pos_counts))#is a series object

pos_values = pos_counts.values #we'll get all the values in a list
pos_labels = pos_counts.index
print(pos_values)

fig = plt.figure(figsize = (10,7))
plt.pie(pos_values, labels=pos_labels)#takes a list of values, respective labels
# plt.show()

# create a pi char for 1)which opponents has he played against 2)on which grounds has he played, 3) chart for dismissals
#for opposition
opponent_count = df["Opposition"].value_counts()#all the no of times he has played against diff opposition
# print(opponent_count)
#creates a list of above column
opponent_values = opponent_count.values
# print(opponent_values)
#create a list of labels which is list of index
opponent_label = opponent_count.index
fig = plt.figure(figsize=(10,7))
plt.pie(opponent_values, labels = opponent_label)
# plt.show()

#for ground
ground_count = df["Ground"].value_counts()
ground_value = ground_count.values
ground_label = ground_count.index
fig = plt.figure(figsize=(10,7))
plt.pie(ground_value, labels=ground_label)
# plt.show()

#for Dismissal => using functions
def show_pie_plot(df, key):
    counts = df[key].value_counts()
    counts_values = counts.values
    counts_label = counts.index
    
    fig = plt.figure(figsize=(10,7))
    plt.pie(counts_values, labels=counts_label)
    plt.show()

# calling for dismissal's plot using functions =>
# show_pie_plot(df, "Dismissal")

# Total Runs scored in different positions 
# eg => wrt each unique "Pos" => how many runs scored => so group acc to "Pos"
runs_at_pos = df.groupby("Pos")["Runs"].sum()
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index
# print(runs_at_pos)
fig = plt.figure(figsize=(10,7))
plt.pie(runs_at_pos_values, labels=runs_at_pos_labels)
# plt.show()

# Total 6s scored against different oppositions & create pie chart
# => so groupby(6s) and then sum the 6s
six_count = df.groupby("Opposition")["6s"].sum()
print(six_count)
# NOTE => show_pie_plot(six_count) => we cannot pass it as a key bcz it doesn't exists in the csv file
six_count_values = six_count.values
six_count_label = six_count.index
fig = plt.figure(figsize=(10,7))
plt.pie(six_count_values, labels=six_count_label)
# plt.show()

# No of centuries scored by Kohli in first and second innings
centuries = df.query("Runs >= 100") #.query() returns a data frame => all the rows printed that matches with this condition 
print(centuries)

innings = centuries["Inns"]
tons = centuries["Runs"]
#create a vertical bar char => in 1st inns => how many centuries and in 2nd inns => how many centuries
fig = plt.figure(figsize=(10,7))#taking blank chart
plt.bar(innings, tons, color='blue', width=0.2)
# plt.show()


# Calculate the dismissals of Kohli 
dismissals = df["Dismissal"].value_counts()
print(dismissals)

dismissals_count = dismissals.values
dismissals_label = dismissals.index
fig = plt.figure(figsize=(7,7))
plt.pie(dismissals_count, labels=dismissals_label)
plt.show()

# Against which teams he has scored the most runs => other method exists so get it
runs = df.groupby("Opposition")["Runs"].sum()
runs_values = runs.values
runs_label = runs.index

fig = plt.figure(figsize=(10, 7))
plt.bar(runs_values, runs_label, color='red', width=0.2)
plt.show()


# Against which teams he has scored most centuries
fig = plt.figure(figsize=(10,7))
plt.bar(
    centuries["Opposition"], centuries["Runs"], color = 'red', width = 0.2
)
plt.show()
# Analyze the strike rate

# Kohli's strkie rate in first innings vs second innings

# Runs scored by him vs 4s played

# Runs scored by him and 6s played

