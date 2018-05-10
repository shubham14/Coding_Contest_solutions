#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

struct TNode
{
	int data;
	TNode *next;
};

TNode *newNode(int n)
{
	TNode *temp = new TNode;
	temp->data = n;
	TNode->next = NULL;
	return TNode;
}

TNode *insert(TNode *root, int n)
{
	if(root == NULL)
	{
		root = newNode(n);
		return root;
	}
	else if(root->left == NULL)
		return insert(root->right, n);
	else
		return insert(root->left, n);
}

int *TraverseTree(TNode *root, int size)
{
	int *A = new int[size];
	int i = 0;
	if(root == NULL)
		return 0;
	else
	{
		while(i < size)
		{
			A[i++] = root->data;
			if(root->left)
				A[i++] = root->left->data;
			if(root->right)
				A[i++] = root->right->data;
		}	
	}
	return A;
}

// logic is that the XOR of all the elements shpuld be zero if it is the same elements
bool SameTree(TNode *root1, TNode *root2, int size1, int size2)
{
	int A[] = TraverseTree(root1,size1);
	int B[] = TraverseTree(root2,size2);
	int ans = 0;
	for(int i = 0; i < size1; i++)
	{
		ans ^ = A[i];
	}
	for(int j = 0; j < size2; j++)
	{
		ans ^ = B[j];
	}
	if(ans == 0)
		return true;
	else
		return false;
}

int main()
{
	//First Tree
	TNode *root1 = newNode(1);
	root1->right = newNode(3);
	root1->left = newNode(2);

	//Second Tree
	TNode *root2 = newNode(2);
	root2->right = newNode(1);
	root2->left = newNode(3);

	bool ans = SameTree(root1, root2, 3, 3);
	cout<<ans<<endl;
	return 0;
}