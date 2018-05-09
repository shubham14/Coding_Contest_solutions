#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

// function to swap the integers
void swap(int *a, int *b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

// heapify is a function to recursivley form a heap where after every heapify the 
// top element is 
void heapify(int A[], int n, int i)
{
	int largest = i;

	// intializing the left and right child
	int l = 2*i + 1;
	int r = 2*i + 2;

	if(l < n && A[largest] > A[l])
		largest = l;
	if(r < n && A[largest] > A[r])
		largest = r;
	if (largest != i)
	{
		swap(A[i], A[largest]);
		heapify(A,n,largest);
	}
}

void heapSort(int A[],int n)
{
	for(i = n/2 - 1 ;i >= 0; i--)
	{
		heapify(A,n,i);
	}
	for(int j = n - 1; j>=0; j--)
	{
		swap(A[0], A[i]);
		heapify(A, i, 0);
	}
}

int main()
{
	int A[] = {12, 11, 13, 5, 6, 7};
	int n = sizeof(A)/sizeof(A[0]);
	heapSort(A, n);
	for(int i = 0; i < n; i++)
	{
		cout<<A[i]<<" ";
	}
	return 0;
}