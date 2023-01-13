import pandas as pd

data = {
    "apples" : [3,4,6,9],
    "oranges" : [1,5,6,8]
}

purchases = pd.DataFrame(data)
print(purchases)
print(type(purchases))

#print the col
print(purchases["oranges"])

index = ['Aaron', 'Lee', 'Steve', 'Shaun']
purchases = pd.DataFrame(
    data, index = index #so in the index parameter we assign the values we want
)
print(purchases)
print(type(purchases))

print(purchases["apples"])
#what if you want to extract the row of 'Aaron'
print(purchases.loc["Aaron"])