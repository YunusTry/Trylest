#include <stdio.h>
#include <stdlib.h>

typedef struct node{
	int data;
	struct node *next;
};
node *head;
node *tail;

void add(int x){
	node *temp =(node *)malloc(1*sizeof(node));
	temp->data = x;
	temp->next = NULL;
	
	if (head==NULL){
		head = temp;
		tail = temp;
	}else{
		tail->next = temp;
		tail = temp;
	}
	return ;
}

void print(){
	node *temp = head;
	while (temp){
		printf(" \n%d",temp->data);
		temp = temp->next;
		
	}
	
}

void remove(){
	int x;
    printf("Enter the data you want to delete:");
    scanf("%d", &x);

    node *temp = head;
    node *prev = NULL;
    
    if (head->data == x){
    	head = head->next;
    	free(temp);
    	return ;
    	
	}
	while (temp!=NULL && temp->data!=x){
		prev = temp;
		temp = temp->next;
	}
	if (head->data ==NULL){
		printf("It is not available when you search");
		return ;
	}
	prev->next = temp->next;
    free(temp);
	
}
int main(){
	printf("welcome to linked list");
	add(1);
	add(2);
	add(3);
	print();
	remove();
	print();
}
