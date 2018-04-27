#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

struct Node
{
    int data;
    struct Node* left, *right;
};
 
int minDepth(Node *root)
{
    int depth = 0;
    if(root == NULL)
        return 0;
    // leaf nodes (corner cases)
    else if(root->right == NULL && root-> left == NULL)
        depth = depth + 1;
    else{
        depth = max(minDepth(root->right) + 1, minDepth(root->left) + 1);
    }
    return depth;
}
 
 
// Utility function to create new Node
Node *newNode(int data)
{
    Node *temp = new Node;
    temp->data  = data;
    temp->left  = temp->right = NULL;
    return (temp);
}
 
int main()
{
    // Let us construct the Tree shown in the above figure
    Node *root        = newNode(1);
    root->left        = newNode(2);
    root->right       = newNode(3);
    root->left->left  = newNode(4);
    root->left->right = newNode(5);
    cout << minDepth(root);
    return 0;
}
