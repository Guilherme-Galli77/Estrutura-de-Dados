#include <stdio.h>
#include <stdlib.h>

struct Node{
 int num;
 struct Node *next;
}; 
typedef struct Node node;

int tamanho;

void inicia(node *LISTA);
int menu(void);
void opcao(node *LISTA, int op);
node *criaNo();
void insereFim(node *LISTA);
void insereInicio(node *LISTA);
void exibe(node *LISTA);
void libera(node *LISTA);
void insere (node *LISTA);
node *retiraInicio(node *LISTA);
node *retiraFim(node *LISTA);
node *retira(node *LISTA);


int main(void)
{
 node *LISTA = (node *) malloc(sizeof(node));
 if(!LISTA){
  printf("Sem memoria disponivel!\n");
  exit(1);
 }else{
 inicia(LISTA);
 int opt;
 
 do{
  opt=menu();
  opcao(LISTA,opt);
 }while(opt);

 free(LISTA);
 return 0;
 }
}

void inicia(node *LISTA)
{
 LISTA->next = NULL;
 tamanho=0;
}

int menu(void)
{
 int opt;
 
 printf("Escolha a opcao\n");
 printf("0. Sair\n");
 printf("1. Zerar lista\n");
 printf("2. Exibir lista\n");
 printf("3. Adicionar node no inicio\n");
 printf("4. Adicionar node no final\n");
 printf("5. Escolher onde inserir\n");
 printf("6. Retirar do inicio\n");
 printf("7. Retirar do fim\n");
 printf("8. Escolher de onde tirar\n");
 printf("Opcao: "); scanf("%d", &opt);
 
 return opt;
}

void opcao(node *LISTA, int op)
{
 node *tmp;
 switch(op){
  case 0:
   libera(LISTA);
   break;
   
  case 1:
   libera(LISTA);
   inicia(LISTA);
   break;
  
  case 2:
   exibe(LISTA);
   break;
  
  case 3:
   insereInicio(LISTA);
   break;  
   
  case 4:
   insereFim(LISTA);
   break;
   
  case 5:
   insere(LISTA);
   break;
  
  case 6:
   tmp= retiraInicio(LISTA);
   printf("Retirado: %3d\n\n", tmp->num);
   break;
   
  case 7:
   tmp= retiraFim(LISTA);
   printf("Retirado: %3d\n\n", tmp->num);
   break;
  
  case 8:
   tmp= retira(LISTA);
   printf("Retirado: %3d\n\n", tmp->num);
   break;
  
  default:
   printf("Comando invalido\n\n");
 }
}

int vazia(node *LISTA)
{
 if(LISTA->next == NULL)
  return 1;
 else
  return 0;
}

node *aloca()
{
 node *novo=(node *) malloc(sizeof(node));
 if(!novo){
  printf("Sem memoria disponivel!\n");
  exit(1);
 }else{
  printf("Novo elemento: "); scanf("%d", &novo->num);
  return novo;
 }
}


void insereFim(node *LISTA)
{
 node *novo=aloca();
 novo->next = NULL;
 
 if(vazia(LISTA))
  LISTA->next=novo;
 else{
  node *tmp = LISTA->next;
  
  while(tmp->next != NULL)
   tmp = tmp->next;
  
  tmp->next = novo;
 }
 tamanho++;
}

void insereInicio(node *LISTA)
{
 node *novo=aloca(); 
 node *oldHead = LISTA->next;
 
 LISTA->next = novo;
 novo->next = oldHead;
 
 tamanho++;
}

void exibe(node *LISTA)
{
 system("clear");
 if(vazia(LISTA)){
  printf("Lista vazia!\n\n");
  return ;
 }
 
 node *tmp;
 tmp = LISTA->next;
 printf("Lista:");
 while( tmp != NULL){
  printf("%5d", tmp->num);
  tmp = tmp->next;
 }
 printf("\n        ");
 int count;
 for(count=0 ; count < tamanho ; count++)
  printf("  ^  ");
 printf("\nOrdem:");
 for(count=0 ; count < tamanho ; count++)
  printf("%5d", count+1);
 
  
 printf("\n\n");
}

void libera(node *LISTA)
{
 if(!vazia(LISTA)){
  node *proxNode,
     *atual;
  
  atual = LISTA->next;
  while(atual != NULL){
   proxNode = atual->next;
   free(atual);
   atual = proxNode;
  }
 }
}

void insere(node *LISTA)
{
 int posicao,
  count;
if (tamanho == 0){
  insereInicio(LISTA);
}
else{

 printf("Em que posicao, [de 1 ate %d] voce deseja inserir: ", tamanho);
 scanf("%d", &posicao);
 
 if(posicao>0 && posicao <= tamanho){
  if(posicao==1)
   insereInicio(LISTA);
  else{
   node *atual = LISTA->next,
     *prev=LISTA; 
   node *novo=aloca();
     
   for(count=1 ; count < posicao ; count++){
     prev=atual;
     atual=atual->next;
   }
   prev->next=novo;
   novo->next = atual;
   tamanho++;
  }
   
 }else
  printf("Elemento invalido\n\n");  
}
}

node *retiraInicio(node *LISTA)
{
 if(LISTA->next == NULL){
  printf("Lista ja esta vazia\n");
  return NULL;
 }else{
  node *tmp = LISTA->next;
  LISTA->next = tmp->next;
  tamanho--;
  return tmp;
 }
    
}

node *retiraFim(node *LISTA)
{
 if(LISTA->next == NULL){
  printf("Lista ja vazia\n\n");
  return NULL;
 }else{
  node *ultimo = LISTA->next,
    *penultimo = LISTA;
    
  while(ultimo->next != NULL){
   penultimo = ultimo;
   ultimo = ultimo->next;
  }
    
  penultimo->next = NULL;
  tamanho--;
  return ultimo;  
 }
}

node *retira(node *LISTA)
{
 int opt,
 count;
 if (tamanho == 0){
   printf("Não há elementos na lista para retirar.\n");
 }
 else
 {printf("Que posicao, [de 1 ate %d] voce deseja retirar: ", tamanho);
 scanf("%d", &opt);
 
 if(opt>0 && opt <= tamanho){
  if(opt==1)
   return retiraInicio(LISTA);
  else{
   node *atual = LISTA->next,
     *prev=LISTA; 
     
   for(count=1 ; count < opt ; count++){
    prev=atual;
    atual=atual->next;
   }
   
  prev->next=atual->next;
  tamanho--;
  return atual;
  }
   
 }else{
  printf("Elemento invalido\n\n");
  
 }
}return NULL;}