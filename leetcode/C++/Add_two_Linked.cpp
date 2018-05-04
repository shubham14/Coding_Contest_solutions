#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

// structure of a linked list node
struct ListNode
{
	int val;
	ListNode *next;
};

// function to create new nodes with 
ListNode *newNode(int val)
{
	ListNode *temp = new ListNode;
	temp->val = val;
	temp->next = NULL;
	return temp;
}

// function to insert numbers in the linked list
void push(ListNode **head, int val)
{
	ListNode *temp = newNode(val);
	temp->next = *head;
	*head = temp;
}

// class containing the solution function
class Solution
{
public:
	ListNode* addTwoNumbers(ListNode *l1, ListNode *l2)
	{
		ListNode *res, *temp1 = l1, *temp2 = l2;
		int carry = 0, count = 0;
		while(temp1 != NULL && temp2 != NULL)
		{
			int data = temp1->val + temp2->val + carry;
			if (count==0)
				res = newNode(data);
			else
			{
				res->next = newNode(data);
			}
			// move forward the result, list 1 and list 2 pointers
			res = res->next;
			carry = data / 10;
			temp1 = temp1->val;
			temp2 = temp2->val;
		}
		if(temp1 == NULL)
		{
			while(temp2)
			{
				int data = temp2->val + carry;
				res->next = newNode(data);
				// move forward the result, list 1 and list 2 pointers
				res = res->next;
				temp2 = temp2->next;
				carry = data / 10;
			}
		}
		else if(temp2 == NULL)
		{
			while(temp1)
			{
				int data = temp1->val + carry;
				res->next = newNode(data);
				// move forward the result, list 1 and list 2 pointers
				res = res->next;
				temp1 = temp1->next;
				carry = data / 10;
			}
		}
		return res;
	}
	void printList(ListNode *head)
	{
		while(head->next)
		{
			cout<<head->val<<"->";
			head = head->next;
		}
		cout<<head->val<<endl;
	}
};

int main()
{
	Solution Sol;
	struct ListNode* res = NULL;
    struct ListNode* first = NULL;
    struct ListNode* second = NULL;
 
    // create first list 7->5->9->4->6
    push(&first, 6);
    push(&first, 4);
    push(&first, 9);
    push(&first, 5);
    push(&first, 7);
    printf("First List is ");
    printList(first);
 
    // create second list 8->4
    push(&second, 4);
    push(&second, 8);
    printf("Second List is ");
    printList(second);
 
    // Add the two lists and see result
    res = Sol.addTwoNumbers(first, second);
    printf("Resultant list is ");
    printList(res);
 
   return 0;
}
