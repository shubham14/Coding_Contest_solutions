#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
	int *A, *B;
	int min_swaps(int *A, int *B, int n);
};

// function to calculate minimum number of swaps required 
// to make the two arrays increasing
int Solution::min_swaps(int *A, int *B, int n)
{
	int i, j;
	int count = 0;
	for(i = 0; i < n; i++)
	{
		// corner cases for the begining and the end elements of the array
		if(i == 0)
		{
			if(A[i] < B[i + 1] && B[i] < A[i + 1] && A[i] > A[i + 1] && B[i] > B[i + 1])
				count += 1;
		}
		else if (i == n - 1)
		{
			if(A[i] > B[i - 1] && A[i] > B[i - 1] && A[i] < A[i - 1] && B[i] < B[i - 1])
				count += 1;
		}
		else 
		{
			if((A[i] < B[i + 1] && A[i] > B[i - 1]) || (B[i] < A[i + 1] && B[i] > A[i - 1]) && ((A[i] > A[i + 1] && A[i] < A[i - 1]) || (B[i] > B[i + 1] && B[i] < B[i - 1])))
				count += 1;
		}
	}
	return count;
}

int main()
{
	Solution Sol;
	int A[] =  {1,3,5,4};
	int B[] =  {1,2,3,7};
	// since both A and B have to be of the same size
	int n = sizeof(A)/sizeof(A[0]);
	int ans;
	ans = Sol.min_swaps(A, B, n);
	cout<<ans<<endl;
}