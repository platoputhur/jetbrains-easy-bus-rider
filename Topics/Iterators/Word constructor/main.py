first_word = input()
second_word = input()
name = ''
for x, y in zip(first_word, second_word):
    name += x
    name += y
print(name)
