#include <iostream>
#include <stdio.h>
#include <queue>
#include <vector>
#include <map>
using namespace std;

struct Node
{
	int data;
	Node *right, *left;

	// constructor
	Node(int key)
	{
		data = key;
		left = right = NULL;
	}
};

// check if a node is a leafnode
bool leafNode(Node *root)
{
	if(root->left || root->right)
		return false;
	return true;
}

// check map function
vector<int> maxLevel(Node *root)
{
	vector<pair<Node *, int>> q; //for storing the level order traversal of the tree
	vector<int> max_level_val;  
	int i = 0, level = 0, j = 0;
	if (root == NULL)
		return ;
	q.push_back(make_pair(root, 1));
	Node *temp = q[i].first();
	max_level_val[j] = temp->data;
	while(temp != NULL)
	{
		if(!leafnode(temp))
		{	
			level++;
			i++;
			if(temp->left)
			{	
				q.push_back(make_pair(temp->left, level));
				if(temp-left->data > max_level_val[level])
					max_level_val[level] = temp-left->data;
			}
			if(temp->right)
			{
				q.push_back(make_pair(temp->right, level));
				if(temp-right->data > max_level_val[level])
					max_level_val[level] = temp-right->data;	
			}
			temp = q[i];
		}
		else
		{
			max_level_val[level + 1] = temp->data;
		}
	}
	return max_level_val;
}


int main()
{

	return 0;
}