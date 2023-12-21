def preenche_matriz():
    M = []
    for i in range(0, 12):
        L = []
        for j in range(0, 12):
            x = float(input())
            L.append(x)
        M.append(L)
    return M

def calcula_soma_ou_media(operacao, M):
    soma = 0
    linha = 1
    aux = linha
    count = 0
    for i in range(0,12):
        for j in range(linha, 12):
            soma += M[linha][i]
            count += 1
            linha += 1
        linha = aux + 1
        aux = linha
    if operacao == 'M':
        soma = soma/count 
    print("{:.1f}".format(soma))

O = input()
M = preenche_matriz()
calcula_soma_ou_media(O, M)