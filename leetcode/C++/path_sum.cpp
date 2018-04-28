#include <iostream>
#include <stdio.h>
#include <algorithm>

struct node
{
	int data;
	node *right, *left;
};

// function to form a new node
node *newNode(int data)
{
	node *temp = new node;
	temp -> right = temp -> left = NULL;
	temp -> data = data;
	return temp;
}

class Solution
{
public:
	bool hasPathSum(node* root, int sum)
	{
		// base cases
		if(root == NULL)
			return false;
		if(root->right == NULL && root->left == NULL)
			return sum == root->val;

		// recursively check all the paths in the tree
		return hasPathSum((root -> right, sum - root->data) || (root -> left, sum - root->data));
	}
};

int main()
{
	// Tree formulation
	Solution sol;
	int sum = 10;
	Treenode *root = newNode(3);
	root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    cout << sol.hasPathSum(root, sum) << endl;
}