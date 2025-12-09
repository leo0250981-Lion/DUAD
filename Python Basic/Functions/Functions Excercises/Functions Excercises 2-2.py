counter = 0  # global variable

def increase_counter():
    global counter
    counter += 1
    print("Value inside the function:", counter)

increase_counter()
increase_counter()
print("Value outside the function:", counter)