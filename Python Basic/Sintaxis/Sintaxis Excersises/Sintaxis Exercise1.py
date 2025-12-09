# Syntax Exercises Exercise #1
# Experiment by doing additions between different data types and write down the results.
# If you get errors, don't worry. Read them and try to understand what they mean.
# Errors are learning opportunities.

## Examples: ##
# 1. string + string = works
"Hello" + " World"
# Output would be "Hello World". This works because when you add two strings, Python concatenates them.

# 2. string + int = error
"Age: " + 25
# Python doesn't know how to mix text with a number... unless you convert the number to a string.
# Correct output should be:
"Age: " + str(25)

# 3. int + string = same as case #2 but reversed; this also produces an error.
# Correct output should be:
str(10) + " years"

# 4. list + list = works because it joins both lists
[1,2,3] + [4,5]
# Output would be:
# [1,2,3,4,5]

# 5. string + list = error
# You cannot mix a string directly with a list.
"Hello" + [1,2,3]
# If you want to join them, you would need to convert the list to text:
"Hello " + str([1,2,3])

# 6. float + int = no error
# Python automatically converts the int to a float.
3.5 + 2
# Correct output would be:
# 5.5

# 7. bool + bool = works because booleans behave like numbers (True = 1, False = 0).
True + True
# Correct output would be:
# 2

True + False
# Output:
# 1
