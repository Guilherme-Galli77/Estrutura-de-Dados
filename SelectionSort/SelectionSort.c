#include <math.h>
#include <stdio.h>


/*
void selection_sort(int∗ v, int n){ //n é tamanho do vetor
    int i, j, min, aux;
    for (i = 0; i < (n−1); i++){
        min = i;
        for (j = (i + 1); j < n; j++){
            if (v[j] < v[min])
                min = j;
        }

        if (v[i] != v[min]){
            aux = v[i];
            v[i] = v[min];
            v[min] = aux;
        }
    }
}
*/

void troca(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
  
void selectionSort(int vet[], int n)
{
    int i, j, min;
  
    for (i = 0; i < n-1; i++)
    {
        min = i;
        for (j = i+1; j < n; j++)
          if (vet[j] < vet[min])
            min = j;
  
        troca(&vet[min], &vet[i]);
    }
}

void printArray(int vet[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", vet[i]);
    printf("\n");
}
  
// Driver program to test above functions
int main()
{
    int vet[] = {64, 25, 12, 22, 11};
    int n = sizeof(vet)/sizeof(vet[0]);
    selectionSort(vet, n);
    printf("Sorted array: \n");
    printArray(vet, n);
    return 0;
}
