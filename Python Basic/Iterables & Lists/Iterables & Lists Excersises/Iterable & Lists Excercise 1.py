first_list = ['There', 'are', 'some', 'iteration', 'index', 'very']
second_list = ['cases', 'where', 'the', 'through', 'is', 'useful']

# Since both lists have the same size, we use range() to loop through the indexes
for i in range(len(first_list)):
    print(first_list[i], second_list[i])