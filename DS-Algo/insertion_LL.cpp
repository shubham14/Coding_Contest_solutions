#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

struct node
{
	int data;
	node *next;
};

node *newnode(int n)
{
	node *temp = new node;
	node->data = n;
	node->next = NULL;
	return node;
}

node *insertionSort(node *head)
{
	node *start = head, *temp = head->next;
	node *tmp_prev;
	node *start_prev;
	while(temp != NULL)
	{
		tmp_prev->next = temp;
		while(start->data != temp->data)
		{
			start_prev->next = start;
			if(start->data > temp->data)
			{
				start->next = temp->next;
			}
			start = start->next;
		}
		tmp_prev = tmp_prev->next;
		temp = temp -> next;
	}
	return head;
}

void sortedInsert(struct Node** head_ref, struct Node* new_node)
{
    struct Node* current;
    /* Special case for the head end */
    if (*head_ref == NULL || (*head_ref)->data >= new_node->data)
    {
        new_node->next = *head_ref;
        *head_ref = new_node;
    }
    else
    {
        /* Locate the node before the point of insertion */
        current = *head_ref;
        while (current->next!=NULL &&
               current->next->data < new_node->data)
        {
            current = current->next;
        }
        new_node->next = current->next;
        current->next = new_node;
    }
}

int main()
{
	struct Node *a = NULL;
    push(&a, 5);
    push(&a, 20);
    push(&a, 4);
    push(&a, 3);
    push(&a, 30);
 
    printf("Linked List before sorting \n");
    printList(a);
 
    insertionSort(&a);
 
    printf("\nLinked List after sorting \n");
    printList(a);
 
    return 0;
}