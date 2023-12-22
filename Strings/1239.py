while True:
    try:
        text = input()

        i_flag = False
        b_flag = False
        new_text = ''

        for char in text:
            if char == '*':
                if not b_flag:
                    new_text += '<b>'
                else:
                    new_text += '</b>'
                b_flag = not b_flag
            elif char == '_':
                if not i_flag:
                    new_text += '<i>'
                else:
                    new_text += '</i>'
                i_flag = not i_flag
            else:
                new_text += char

        print(new_text)
    except EOFError:
        break