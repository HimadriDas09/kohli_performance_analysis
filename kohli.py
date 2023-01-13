import pandas as pd

#generally define a dataframe obj as df
#pandas can read csv file

df = pd.read_csv("dataset.csv")

# print(df)
# print(df.head(10)) #to get first 10 rows
# print(df.tail(10)) #to get last 10 rows

# print(df.info())
# #we must eradicate any null values if present

# print(df.shape) #no of rows against no of cols

# print(df.describe())

print(df["Opposition"].describe())

print(df)
print(df["Runs"].value_counts())#frequency of each value => i.e from the col, finding all the unique values and finding their count of how many times those unique values occur

#create a new dataFrame using runs, BF, opposition
new_df = df[["Runs", "4s", "6s", "Opposition"]] #inside 3rd bracket put all those cols which u want to extract from the org data Frame => to create a new dataFrame
print(new_df)
print(new_df.describe())

#.loc -> to locate by name
#.iloc -> to locate by numeric index

print(new_df.iloc[2])
print(new_df.iloc[2:5])
print(new_df.iloc[2:5]["Runs"])#printing the "Runs" col from index 2 to 4

print(new_df.iloc[2:13]["6s"])

#printing details of all the matches in which kohli played against v Australia
print(df["Opposition"] == "v Australia") #for which of the rows is the opposition australia
vs_aussies = df[df["Opposition"] == "v Australia"] #is returning a DataFrame
print(vs_aussies.head(10))

#the sum of all the runs gained against Australia
print(vs_aussies["Runs"].sum())

#find entries where kohli played against australia and score century
#in pandas & is the AND operator
centuries = vs_aussies[vs_aussies["Runs"] >= 100]
print(centuries)
vs_aussies_century = df[(df["Opposition"] == "v Australia") & (df["Runs"] >= 100)]
print(vs_aussies_century)

#centuries and vs_aussies_century => contain same DataFrame

def find_centuries(x):
    if x >= 100:
        return "OG"
    else:
        return "NOOB"

#below assigning value to a key
df["Centuries"] = df["Runs"].apply(find_centuries)#for a DataFrame we can apply a function to it => so for each Run entry we call the function on it
print(df)