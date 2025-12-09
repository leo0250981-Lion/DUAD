list_of_keys = ["access_level", "age"]

employee = {
    "name": "Leonardo Escalona",
    "email": "leo0205981@icloud.com",
    "access_level": 5,
    "age": 28
}

# Loop through the list and remove those keys from the dictionary
for key in list_of_keys:
    if key in employee:
        del employee[key]

print(employee)