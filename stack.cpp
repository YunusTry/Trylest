#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
     node *prev; 
} node;

node *first ;
node *last ;

void push(int x) {
    node *temp = (node *)malloc(sizeof(node));
    temp->data = x;
    temp->prev = first; // Düðümün bir sonraki düðümü, mevcut "first" düðümünü gösterir.

    first = temp;
}

int pop() {
    int postala;
    postala = first->data;
    node *temp = first;
    first = first->prev;
    free(temp);

    return postala;
}


void listele() {
    node *temp = first;
    while (temp) {
        printf(" %d ", temp->data);
        temp = temp->prev;
    }
    printf("\n");
}

int main() {
    push(1);
    push(2);
    push(3);
    pop();
    listele();

    return 0;
}

