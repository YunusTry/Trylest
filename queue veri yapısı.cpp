#include <stdio.h>
#include <stdlib.h>

typedef struct node{
	int data ;
	node *prev ;
}; 
node *first, *last ;

void ekleme(int x){
	node *temp = (node *)malloc(1*sizeof(node));
	temp->data = x;
	temp->prev = NULL ;
	
	if (!first){
		first = temp;
		last = temp;
		return ;
	}
	last->prev = temp ;
	last = temp ;
	return;
}

int pop(){
	int postala;
	postala = first->data;
	node *temp = first;
	first = first->prev;
	temp->prev = NULL;
	free (temp);
	
	return postala;
	
}

void listele(){
	node *temp = first ;
	while (temp){
	
		printf(" %d ", temp->data);
		temp = temp->prev ;
		
		
	}
}


int main(){
	ekleme(10);
	ekleme(20);
	ekleme(30);
	pop();
	listele();
	
	return 0;
}

