# Busca Binaria Recursiva em Python
# Retorna o índice de x em vet se presente, senão retorna -1

def busca_binaria(vet, menor, maior, x):
    # Verifica o caso base
    if maior >= menor:

        md = (maior + menor) // 2

        # Verifica se o elemento está presente no meio
        if vet[md] == x:
            return md

        # Se o elemento for menor do que md, ele só pode estar presente no subvetor a esquerda
        elif vet[md] > x:
            return busca_binaria(vet, menor, md - 1, x)

        # Caso contrário, o elemento só pode estar presente no subvetor a direita
        else:
            return busca_binaria(vet, md + 1, maior, x)

    else:
        # Elemento não está presente no vetor
        return -1


# Vetor de teste
vet = [1, 3, 5, 13, 58, 67, 123, 459, 3000, 29435]
x = 3000

# Chamada da função
resultado = busca_binaria(vet, 0, len(vet) - 1, x)

# Exibe a posição do item (0,1,2,3,4,5,.....) caso ele esteja no vetor
if resultado != -1:
    print("O elemento está presente na posição: ", str(resultado))
else:
    print("O elemento não está presente no vetor!")
