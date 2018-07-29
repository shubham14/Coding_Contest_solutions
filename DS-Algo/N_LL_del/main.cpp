#include <iostream>
#include <stdio.h>
using namespace std;

struct Node
{
    int data;
    Node *next;
};

Node *newNode(int n)
{
    Node *temp = new Node;
    temp->data = n;
    temp->next = NULL;
    return temp;
}

Node *deleteNthNode(Node *head, int n)
{
    if (head == NULL)
        return NULL;
    Node *ref1=head, *temp=head, temp1;
    int count = 0;
    while(count <= n)
    {
        ref1 = ref1->next;
    }
    while(ref1->next!=NULL)
    {
        temp = temp->next;
        temp1->next = temp;
        ref1 = ref1->next;
    }
    temp1->next = temp->next;
    free(temp);
    return head;
}

int main()
{
    Node *head = newNode(1);
    head->next = newNode(2);
    head->next->next = newNode(3);
    head->next->next->next = newNode(4);
    head->next->next->next->next = newNode(5);

    return 0;
}
