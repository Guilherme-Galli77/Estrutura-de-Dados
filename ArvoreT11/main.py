
import time

# Classe que aloca um novo nó

class getNode:
    def __init__(self, data, tamanho):
        self.data = data
        self.tamanho = tamanho
        self.left = self.right = None


# Retorna verdadeiro se houver um caminho da raiz para o nó fornecido.
def temCaminho(raiz, vet, x):
    # Se a raiz for nula não há cnenhum caminho
    if (not raiz):
        return False


    vet.append(raiz.data)

    # se for o nó buscado return true
    if (raiz.data == x):
        return True

    # senão verifique se o nó necessário encontra-se na subárvore esquerda ou direita do nó atual
    if (temCaminho(raiz.left, vet, x) or
            temCaminho(raiz.right, vet, x)):
        return True

    # nó necessário não se encontra na subárvore esquerda ou direita do nó.
    # Assim, remova o valor do nó atual de e, em seguida, retorne falso
    vet.pop(-1)
    return False


# função para imprimir o caminho da raiz para o nó fornecido caso o nó esteja na árvore binária
def imprimeCaminho(root, x):
    # vetor que armazena o caminho
    vet = []

    # se o nó necessário estiver presente, então imprima o caminho
    if (temCaminho(root, vet, x)):
        for i in range(len(vet) - 1):
            print(vet[i], end="->")
        print(vet[len(vet) - 1])

    # se o nó não estiver presente na arvore binaria
    else:
        print("Erro!! Caminho ou nó não encontrados!!")



if __name__ == '__main__':
    # Formação da arvore binaria
    root = getNode('/user/rt/cursos', 1)
    root.left = getNode('/java/', 2)
    root.right = getNode('/ruby/', 1)
    root.left.left = getNode('', 0)
    root.left.right = getNode('', 0)
    root.left.left.left = getNode('Grades1', 8)
    root.left.right.right = getNode('Exercicios/', 1)
    root.left.right.right.left = getNode('', 0)
    root.left.right.right.right = getNode('', 0)
    root.left.right.right.right.left = getNode('Exerc02', 2)
    root.left.right.right.right.right = getNode('Exerc03', 4)
    root.left.right.right.left.left = getNode('Exerc01', 3)
    root.left.right.left = getNode('Slides/', 2)
    root.left.right.left.left = getNode('', 0)
    root.left.right.left.right = getNode('', 0)
    root.left.right.left.left.left = getNode('Slide01', 3)
    root.left.right.left.left.right = getNode('Slide02', 2)
    root.left.right.left.right.right = getNode('Slide03', 4)
    root.right.left = getNode('Grades2', 5)
    root.right.right = getNode('Projetos', 1)
    root.right.right.right = getNode('Demos/', 1)
    root.right.right.right.right = getNode('Market', 7)
    root.right.right.left = getNode('Papers/', 2)
    root.right.right.left.right = getNode('Buy', 8)
    root.right.right.left.left = getNode('Thread', 9)

#Imprime o caminho até o nó desejado pelo usuario
x = 'Exerc01'  # Nó escolhido

print("O caminho até o nó escolhido é: ")
imprimeCaminho(root, x)
print("===================================")
print("===================================")
print("===================================")

time.sleep(1.5)
print("Calculando...")
time.sleep(2)

print("===================================")
print("===================================")
print("===================================")


# Funcao que calcula o tamanho a partir de um nó determinado

def TamanhoTotal(root):
    if (root == None):
        return 0
    return (root.tamanho + TamanhoTotal(root.left) +
            TamanhoTotal(root.right))


# questão A) Função que imprime o total de arquivos em Kbytes do diretório /ruby/.

somaTotalA = TamanhoTotal(root.right)

print("O tamanho total de arquivos em Kbytes do diretório /ruby/ é de:", somaTotalA, "Kbytes")
print("===================================\n")
time.sleep(1.5)

# questão B) Função que imprime o total de arquivos em Kbytes do diretório /java/.

somaTotalB = TamanhoTotal(root.left)

print("O tamanho total de arquivos em Kbytes do diretório /java/. é de:", somaTotalB, "Kbytes")
print("===================================\n")
time.sleep(1.5)

# questão C) Função que imprime o total de arquivos em Kbytes de toda a estrutura de diretórios.

somaTotalC = TamanhoTotal(root)

print("O tamanho total da arvore de diretórios é de:", somaTotalC, "Kbytes")
print("===================================\n")
time.sleep(1.5)