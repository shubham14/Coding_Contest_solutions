// Bucket sort in C++

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <list>

void Bucket_Sort(float A[],int n)
{
	list<float> b[n];
	for(int i=0;i<n;i++)
	{
		int b_new = n*A[i];
		b[b_new].push_back(A[i]);
	}
	for(int i = 0; i < n; i++)
	{
		sort(b[i].begin(), b[i].end())
	}
	int ind = 0;
	for (int i=0;i<n;i++)
	{
		for(int j=0;j<b[i].size;j++)
		{
			A[ind++] = b[i][j];
		}
	}
}

int main()
{
	float A[] = {0.12, 0.21, 0.39, 0.17, 0.94, 0.26, 0.23, 0.39, 0.68, 0.72, 0.78}
	int n = sizeof(A)/sizeof(A[0]);
	bucketsort(A, n);
	cout<<"Sorted Array is: "<< endl;
	for(int i = 0; i < n; i++)
	{
		cout<<A[i]<<endl;
	}
	return 0;
}