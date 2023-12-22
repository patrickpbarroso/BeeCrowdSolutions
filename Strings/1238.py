N = int(input())

for i in range(0, N):
    string1, string2 = input().split()
    # Make it so that 'string1' is always the greater in length
    if len(string2) > len(string1):
        maior = string2
        menor = string1
    else:
        maior = string1
        menor = string2
    # New permutated string
    new_string = ''

    # Fill new string with all intercalated values until the size of the lesser string
    for i in range(0, len(menor)):
        new_string += string1[i] + string2[i]
    
    # Fill the rest with the values of the greater string
    if len(string1) != len(string2):
        for j in range(len(menor), len(maior)):
            new_string += maior[j]

    print(new_string)