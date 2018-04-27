#include <iostream> 
#include <stdio.h>
#include <algorithm>
#include <limits.h>

using namespace std;

class Tree_Node
{
public:
	int data;
	Tree_Node *left, *right;
	Tree_Node* newNode(int data)
	{
		Tree_Node* temp = new Tree_Node;
		temp->data = data;
		temp->right = temp -> left = NULL;
		return temp;
	}
};

class Solution
{
	// Utility function for maximum subtree sum
	int max_subtree_sum_Util(Tree_Node* root, int &ans)
	{
		// base case
		if(root == NULL)
			return 0;

		// Pre-order traversal of the tree
		int current_sum = root->data +
						max_subtree_sum_Util(root->left, ans) +
						max_subtree_sum_Util(root->right, ans);

		ans = max(ans, current_sum);
		return current_sum;
	}

	int Largest_subtree_sum(Tree_Node* root)
	{
		int ans = INT_MIN;
		max_subtree_sum_Util(root, ans);
		return ans;
	}
};

int main()
{
	// solution class instantiation
	Solution sol;
	// Tree structure
	Tree_Node node;
	node* root = node.newNode(1);
    root->left = node.newNode(-2);
    root->right = node.newNode(3);
    root->left->left = node.newNode(4);
    root->left->right = node.newNode(5);
    root->right->left = node.newNode(-6);
    root->right->right = node.newNode(2);

    int ans = sol.Largest_subtree_sum(node->root);
    cout << ans << endl; 
    return 0;
}