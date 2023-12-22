def gambler(EV1, EV2, AT):
    # i've used gambler's ruin formulation to solve this problem: https://en.wikipedia.org/wiki/Gambler%27s_ruin
    if AT == 3:
        # Case in which the roll is fair
        return EV1 / (EV1 + EV2)
    else:
        # Case in which the roll is unfair
        p = AT / 6
        q = 1 - p
        return (1 - (q/p)**EV1)/(1 - (q/p)**(EV1 + EV2))

while True:
    EV1, EV2, AT, D = [int(x) for x in input().split()]
    
    if EV1 == EV2 == AT == D == 0:
        break

    # From the initial health points of each vampire, we get how much loss can it take till it gets lesser or equal to zero
    # For example, if D = 2 and the health of vampire 1 is 8, then it takes 4 losses to lost the combat
    # These amounts of possible losses considering the initial state is what we are interested in, to make it similar to the coin flipping example
    aux = EV1 
    EV1 = 0
    while aux > 0:
        aux -= D
        EV1 += 1
    
    aux = EV2 
    EV2 = 0
    while aux > 0:
        aux -= D
        EV2 += 1
    
    p = gambler(EV1, EV2, AT) * 100

    print(round(p, 1))

