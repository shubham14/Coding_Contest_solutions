// Least Common Ancestor
#include <iostream>
#include <stdio.h>
#include <vector>

struct node
{
	int key;
	node *left, *right;
};

node *newNode(int k)
{
	node *temp = new node;
	temp->key = k;
	temp->left = temp->right = NULL;
	return temp;
}

// storing path from a node
bool findPath(node *root, vector<int> &path, int k)
{
	if(root == NULL)
		return false;
	if(root->key == k)
		return true;
	if((root->left && findPath(root->left, path, k)) || 
		(root->right && findPath(root->right, path, k)))
		return true;
	path.pop_back();
	return false;
}

// LCS in a single tree traversal
int findLCA(node *root, int n1, int n2)
{
	vector<int> path1, path2;
	if(!findPath(root, path1, n1) || !findPath(root, path2, n2))
		return -1;
	for(int i = 0; i < path1.size() && i < path2.size(); i++)
	{
		if(path1[i] != path2[i])
			break;
	}
	return path1[i-1];
}

int LCA2(node *root, int n1, int n2)
{
	if(root == NULL)
		return -1;
	if (root->key == n1 || root->key == n2)
		return root->key;
	if(LCA2(root->left, n1, n2) != -1 && LCA2(root->right, n1, n2) != -1)
		return root->key;
	return (LCA2(root->leftn1,n2)) ? root->left->key: root->right->key; 
}	

int main()
{
	node * root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);
    cout << "LCA(4, 5) = " << findLCA(root, 4, 5)->key;
    cout << "nLCA(4, 6) = " << findLCA(root, 4, 6)->key;
    cout << "nLCA(3, 4) = " << findLCA(root, 3, 4)->key;
    cout << "nLCA(2, 4) = " << findLCA(root, 2, 4)->key;
    return 0;

}