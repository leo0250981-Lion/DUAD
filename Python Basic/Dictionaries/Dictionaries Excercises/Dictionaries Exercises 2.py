list_a = ["first_name", "last_name", "role"]
list_b = ["Leonardo", "Escalona", "IT"]

# Create an empty dictionary
result = {}

# Use range() to iterate through both lists by index
for i in range(len(list_a)):
    key = list_a[i]
    value = list_b[i]
    result[key] = value

print(result)