#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

struct TreeNode
{
    int data;
    TreeNode *right, *left;
};

TreeNode *newNode(int data)
{
    TreeNode *temp = new TreeNode;
    temp->data = data;
    temp->right = temp->left = NULL;
    return temp;
}

// Use BFS for this
TreeNode *invertTree(TreeNode *root)
{
    if(root == NULL)
        return root;
    queue<TreeNode *> Tree;
    Tree.push(root);
    while(!Tree.empty())
    {
        TreeNode *node = Tree.front();
        Tree.pop();
        if(node->left != NULL)
            Tree.push(node->left);
        if(node->right != NULL)
            Tree.push(node->right);
        TreeNode *temp = node->left;
        node->left = node->right;
        node->right = temp;
    }
    return root;
}

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
