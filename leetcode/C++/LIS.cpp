#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

// intialise class to 
class Solution
{
public:
	int *A;
	int lis(int *A, int n);
};

int Solution::lis(int arr[], int n)
{
    int *lis, i, j, max = 0;
    lis = (int*) malloc ( sizeof( int ) * n );
    A = arr;
    for (i = 0; i < n; i++ )
        lis[i] = 1;
 
    for (i = 1; i < n; i++ )
        for (j = 0; j < i; j++ ) 
            if ( A[i] > A[j] && lis[i] < lis[j] + 1)
                lis[i] = lis[j] + 1;
 
    // Extract the maximum of all the values
    for (i = 0; i < n; i++ )
        if (max < lis[i])
            max = lis[i];
 
    // Free allocated memory
    free(lis);
    return max;
}

int main()
{
    // instantiate class variable 
	Solution Sol;
	int B[] = {10, 22, 9, 33, 21, 50, 41, 60 };
	int m = sizeof(B)/sizeof(B[0]);
	int ans;
	ans = Sol.lis(B, m);
	cout << ans;
}