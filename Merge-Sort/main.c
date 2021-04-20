#include <stdlib.h>
#include <stdio.h>


void merge_sort(int i, int j, int vet[], int aux[]) {
    if (j <= i) {
        return;
    }
    int metade = (i + j) / 2;



    merge_sort(i, metade, vet, aux);
    merge_sort(metade + 1, j, vet, aux);

    int ponteiro_esquerda = i;
    int ponteiro_direita = metade + 1;
    int k;


    for (k = i; k <= j; k++) {
        if (ponteiro_esquerda == metade + 1) {
            aux[k] = vet[ponteiro_direita];
            ponteiro_direita++;
        } else if (ponteiro_direita == j + 1) {
            aux[k] = vet[ponteiro_esquerda];
            ponteiro_esquerda++;
        } else if (vet[ponteiro_esquerda] < vet[ponteiro_direita]) {
            aux[k] = vet[ponteiro_esquerda];
            ponteiro_esquerda++;
        } else {
            aux[k] = vet[ponteiro_direita];
            ponteiro_direita++;
        }
    }

    for (k = i; k <= j; k++) {
        vet[k] = aux[k];
    }
}


int main() {
  int vet[100], aux[100], n, i, d;

  printf("Digite o numero de elementos do vetor:\n");
  scanf("%d", &n);

  printf("Digite %d inteiros\n", n);

  for (i = 0; i < n; i++)
    scanf("%d", &vet[i]);

  merge_sort(0, n - 1, vet, aux);

  printf("Vetor ordenado:\n");

  for (i = 0; i < n; i++)
     printf("%d\n", vet[i]);

  return 0;
}
