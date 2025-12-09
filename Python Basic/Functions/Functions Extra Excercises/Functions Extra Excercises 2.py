def filter_words_by_length(words, n):
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    return result

# Example
words_list = ["sky", "sun", "marvelous", "day"]
n = 4

print(filter_words_by_length(words_list, n))
# → ["sky", "marvelous"]