word_file = open('./store/input.txt', 'r')
search_words = ["Python", "C", "OOP", "Hello", "Java"]

word_lists = word_file.readlines()

found = ''

for search in search_words:
    counter = 0
    for word in word_lists:
        if search.lower() in word.lower():
            counter += 1
    found += '{} -> {}\n'.format(search, counter)
print(found)