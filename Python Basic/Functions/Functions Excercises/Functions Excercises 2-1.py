def scope_function():
    x = 10
    print("x inside the function:", x)

scope_function()

print(x)  # ❌ Error: x does not exist outside the function