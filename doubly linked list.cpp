#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *next;
    struct node *prev;
} node;

node *head;
node *tail;

void add(int x) {
    node *temp = (node *)malloc(1 * sizeof(node));
    temp->data = x;
    temp->next = NULL;
    temp->prev = NULL;

    if (head == NULL) {
        head = temp;
        tail = temp;
    } else {
        tail->next = temp;
        temp->prev = tail;
        tail = temp;
    }
}

void print() {
    node *temp = head;
    while (temp) {
        printf(" \n%d", temp->data);
        temp = temp->next;
    }
}

void removeNode() {
    int x;
    printf("\nEnter the data you want to delete:");
    scanf("%d", &x);

    node *temp = head;
    if (head->data == x) {
        head = head->next;
        if (head != NULL) {
            head->prev = NULL;
        }
        free(temp);
        return;
    }

    while (temp != NULL && temp->data != x) {
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("The data you searched for is not available.\n");
        return;
    }

    temp->prev->next = temp->next;
    if (temp->next != NULL) {
        temp->next->prev = temp->prev;
    }
    free(temp);
}

int main() {
    printf("Welcome to linked list\n");
    add(1);
    add(2);
    add(3);
    print();
    removeNode();
    print();

    return 0;
}
