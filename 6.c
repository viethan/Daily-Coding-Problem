#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node {
	int value;
	struct node *both;
} node;

node *new(int value) {
	node *new = (node *)malloc(sizeof(struct node));
	new->value = value;
	new->both = NULL;

	return new;
}

void add(int element, node *head) {
	// I'll know that I reached the last node 
	// when the BOTH pointer points exactly to the previous node
	// meaning that the xor will result in 0
	node *current = head, *prev = NULL;
	node *next, *temp;
	while (current != NULL) {
		next = (node *)((long)prev ^ (long)current->both); 

		temp = prev;
		prev = current;
		current = next;
	}
	current = prev; 
	prev = temp;

	node *new_node = new(element);
	new_node->both = current;
	current->both = (node *)((long)prev ^ (long)new_node); 
}

void print(node *head) {
	node *current = head, *prev = NULL;
	node *next;
	while (current != 0) {
		next = (node *)((long)prev ^ (long)current->both); 
		printf("val: %d both: %p\n", current->value, current->both);

		prev = current;
		current = next;
	}
}


void freeAll(node *head) {
	node *current = head, *prev = NULL;
	node *next;
	while (current != 0) {
		next = (node *)((long)prev ^ (long)current->both); 
		free(current);

		prev = current;
		current = next;
	}
}

int get(int index, node *head) {
	node *current = head, *prev = NULL;
	node *next;
	bool printed = false;

	while (current != 0) {
		next = (node *)((long)prev ^ (long)current->both); 
		if (index == 1) 
			return current->value;

		index--;
		prev = current;
		current = next;
	}


	fprintf(stderr, "Error.\n");
	exit(1);
}

void test() {
	node *head = new(7);
	add(4, head);
	add(5, head);
	add(6, head);
	add(1, head);
	print(head);
	int val = get(4, head);
	printf("%d\n", val);
	freeAll(head);
}

int main(void) {
	test();
}
