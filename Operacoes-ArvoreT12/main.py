#1. Implementar um programa que implemente a seguinte árvore binária:

# Classe que aloca um novo nó

class getNode:
    def __init__(self, data, unidade):
        self.data = data
        self.unidade = unidade
        self.left = self.right = None


if __name__ == '__main__':
    # Formação da arvore binaria
    root = getNode(0, 1)
    root.left = getNode(1, 1)
    root.right = getNode(2, 1)
    root.right.right = getNode(4, 1)
    root.right.left = getNode(3, 1)
    root.right.left.left = getNode(5, 1)
    root.right.left.right = getNode(6, 1)


print("2. Percorrer a árvore binária, imprimindo os valores dos nós segundo as estratégias de busca: preOrder, postOrder e inOrder\n")


# Funcao PreOrder
def printPreorder(root):
    if root:
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)


# Funcao PostOrder
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)


# Funcao InOrder
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data),
        printInorder(root.right)


print("Preorder da arvore é: ")
printPreorder(root)
print("\nPostorder da arvore é:")
printPostorder(root)
print("\nInorder da arvore é: ")
printInorder(root)



print("\n3. Escrever uma função que verifica se um dado valor inteiro K está presente na árvore\n")


# Função para percorrer a árvore usando PreOrder e verificar a existencia de determinado nó nela

def verificaExistenciaNo(node, K):
    if (node == None):
        return False

    if (node.data == K):
        return True

    x1 = verificaExistenciaNo(node.left, K)
    # Nó encontrado,sendo assim fim de busca
    if x1:
        return True

    # Nó não encontrado, verifica o outro lado da arvore
    x2 = verificaExistenciaNo(node.right, K)

    return x2


K = int(input("\nDigite o valor do nó (K) que deseja procurar!:\n"))

if (verificaExistenciaNo(root, K)):
    print("\nO Nó está presente na arvore\n")
else:
    print("\nInfelizmente o nó não está presente na arvore\n")



print("\n4. Escrever uma função que irá retornar o maior valor armazenado na árvore: ")


def encontrarMaximo(root):
    # Base case
    if (root == None):
        return float('-inf')
    r = root.data
    lr = encontrarMaximo(root.left)
    rr = encontrarMaximo(root.right)
    if (lr > r):
        r = lr
    if (rr > r):
        r = rr
    return r

print("\n O maior elemento é: ", encontrarMaximo(root))

print("\n5. Escrever uma função que irá retornar o menor valor armazenado na árvore: ")

def encontrarMinimo(root):
    if root is None:
        return float('inf')
    rmin = root.data
    lrmin = encontrarMinimo(root.left)
    rrmin = encontrarMinimo(root.right)
    if lrmin < rmin:
        rmin = lrmin
    if rrmin < rmin:
        rmin = rrmin
    return rmin

print("\n O menor elemento é: ", encontrarMinimo(root))





print("\n6. Escrever uma função que irá retornar a média aritmética dos valores armazenados na árvore: ")

#Calculo do tamanho total da arvore, foi atribuido um valor unidade = 1 para cada nó
def TamanhoTotal(root):
    if (root == None):
        return 0
    return (root.unidade + TamanhoTotal(root.left) +
            TamanhoTotal(root.right))

#Calculo da soma do conteudo de todos os nós
def SomaTot(root):
    if (root == None):
        return 0
    return (root.data + SomaTot(root.left) +
            SomaTot(root.right))


Media = (SomaTot(root)/TamanhoTotal(root))

print("A média aritmética dos valores armazenados na árvore é:", Media)


print("\n7. Escrever uma função que irá retornar o número de NULL’s armazenados na árvore: \n")


# Função para percorrer a árvore usando PreOrder e verificar a existencia de NULL nela

def verificaExistenciaNULL(node, N):
    if (node == None or node == ""):
        return True
N = ""

if (verificaExistenciaNULL(root, N)):
    print("\nO NULL está presente na arvore\n")
else:
    print("\nNULL não está presente na arvore\n")


print("\n8. Escrever uma função que irá retornar a quantidade de nós armazenados na árvore \n")


def totalDeNos(root):
    if (root == None):
        return 0
    return (root.unidade + totalDeNos(root.left) + totalDeNos(root.right))

total = totalDeNos(root)
print("O total de nós da arvore é de:", totalDeNos, "nós\n")



print("\n9. Escrever uma função que irá retornar a quantidade de folhas armazenadas na árvore; \n")

def quantidadeFolhas(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return quantidadeFolhas(node.left) + quantidadeFolhas(node.right)

print("A quantidade de folhas é: %d" % (quantidadeFolhas(root)))



print("\n10. Escrever uma função que irá retornar a altura da árvore \n")

def altura(node):
    if node is None:
        return 0;

    else:

        # Profundidade de cada sub arvore
        profundidadeEsq = altura(node.left)
        profundadeDir = altura(node.right)


        if (profundidadeEsq > profundadeDir):
            return profundidadeEsq + 1
        else:
            return profundadeDir + 1


print ("A altura da arvore é: %d" %(altura(root)))