while True:
    try:
        sentence = input()
        dancing_sentence = ''
        previous_is_upper = False

        for letter in sentence:
            if ord(letter) == 32:
                dancing_sentence += letter
            elif not previous_is_upper:
                dancing_sentence += letter.upper()
                previous_is_upper = not previous_is_upper
            else:
                dancing_sentence += letter.lower()
                previous_is_upper = not previous_is_upper     

        print(dancing_sentence)
    except EOFError:
        break