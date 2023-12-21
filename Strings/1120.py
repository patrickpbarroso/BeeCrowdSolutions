while True:
    D, N = input().split()
    if int(D) == 0 and int(N) == 0:
        break
    
    wrong = ''
    for i in N:
        if i != D:
            wrong += i
    
    if not wrong:
        wrong = '0'

    print(int(wrong))