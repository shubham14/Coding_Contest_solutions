
#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#include <queue>
using namespace std;

// struture defining the node of a tree
struct TreeNode{
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

// level order traversal of the tree to find an empty place
void insert(TreeNode* temp, int key)
{
    queue<struct TreeNode*> q;
    q.push(temp);
 
    while (!q.empty()) {
        struct TreeNode* temp = q.front();
        q.pop();
 
        if (!temp->left) {
            temp->left = newNode(key);
            break;
        } else
            q.push(temp->left);
 
        if (!temp->right) {
            temp->right = newNode(key);
            break;
        } else
            q.push(temp->right);
    }
}

// check if a node is a leafnode or not
bool leafNode(TreeNode *root)
{
    if (root->left == NULL and root->right == NULL)
        return true;
    return false;
}

// recursive function to display the leftview of the tree
vector<int> leftView(TreeNode *root, vector<int> &ans)
{
    if(root == NULL)
        ans.push_back(-1);
    else if(leafNode(root))
    {    
        ans.push_back(root->data);
        return ans;
    }
    if(root->left)
    {
        ans.push_back(root->data);
        ans = leftView(root->left, ans);
    }
    if(root->right)
    {
        ans.push_back(root->data);
        ans = leftView(root->right, ans);
    }
    return ans;
}

int main()
{
    TreeNode* root = newNode(10);
    root->left = newNode(11);
    root->left->left = newNode(7);
    root->right = newNode(9);
    root->right->left = newNode(15);
    root->right->right = newNode(8);
    
    vector<int> ans;
    ans = leftView(root, ans);
    
    for(int i=0; i < ans.size(); i++)
    {
        cout<<ans[i]<<" ";
    }
    cout<<endl;
    return 0;
}