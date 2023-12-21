N = int(input())
words = []
for i in range(0, N):
    word = input()
    new_word = ''

    for letter in word:
        unicode_char = ord(letter)
        if unicode_char >= 65 and unicode_char <= 122:
            new_char = chr(unicode_char + 3)
        else:
            new_char = letter
        new_word += new_char          

    new_new_word = ''
    for i in range(1, len(new_word)+1):
        new_new_word += new_word[len(new_word) - i]

    new_new_new_word = ''
    metade = int(len(new_word)/2)
    for i in range(0, len(new_new_word)):
        if i < metade:
            new_new_new_word += new_new_word[i]
        else:
            new_new_new_word += chr(ord(new_new_word[i]) - 1)

    words.append(new_new_new_word)

for word in words:
    print(word)