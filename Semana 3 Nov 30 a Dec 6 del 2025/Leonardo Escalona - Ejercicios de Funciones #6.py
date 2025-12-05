def sort_hyphen_string(text):
    words = text.split("-")
    words.sort()
    return "-".join(words)

print(sort_hyphen_string("python-variable-function-computer-monitor"))
# → computer-function-monitor-python-variable