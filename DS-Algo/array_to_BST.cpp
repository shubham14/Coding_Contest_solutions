#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

// Node definition
struct Node
{
	int data;
	Node *right, *left;
};

// function to create newNode
Node *newNode(int d)
{
	Node *temp = new Node;
	temp->data = d;
	temp->left = temp->right = NULL;
	return temp;
}

// magic function!!
// note that the Array has to be sorted given that BST inorder is a sorted array
Node *arrayToBST(int *A, int start, int end)
{
	// Sort the array just in case it is not
	A.sort();
	int mid = (start - end) / 2 + start;
	Node *root = newNode(A[mid]);

	// recursion takes over
	root->left = arrayToBST(A, start, mid - 1);
	root->right = arrayToBST(A, mid + 1, start);

	return root;
}

// Display the BST
void preorder(Node *root)
{
	if(root == NULL)
		return ;
	cout<<root->data<<" ";
	preorder(root->left);
	preorder(root->right);
}

int main(int argc, char const *argv[])
{
	int A[] = {1, 2, 4, 3, 5, 6, 7};
	int n = sizeof(A)/ sizeof(A[0]);

	Node *root = arrayToBST(A, 0, n-1);
	cout<< "Here is the tree"<< endl;
	preorder(root);
	return 0;
}