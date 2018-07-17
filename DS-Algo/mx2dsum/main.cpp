#include <iostream>
#include <stdio.h>
#include <vector>
#include <string.h>
#include <limits.h>
using namespace std;

#define MAX 10

int kadane(int *A, int *atart, int *finish, int n)
{
    int sum=0, maxSum=INT_MIN, i;
    *finish = -1;
    int st1 = 0;
    for(i=0; i<n; i++)
    {
        sum+ = A[i];
        if(sum<0)
        {
            sum = 0;
            st1 = i+1;
        }
        else if(sum>maxSum)
        {
            maxSum = sum;
            *start = st1;
            *finish = i;
        }
    }
    if(*finish != -1)
        return maxSum;
    maxSum = arr[0];
    *start = *finish = 0;

    for(i = 1; i < n; i++)
    {
        if(maxSum < A[i])
        {
            maxSum = A[i];
            *start = *finish = i;
        }
    }
    return maxSum;
}

void findMaxSum(int M[][MAX], int n, int m)
{
    int maxSum = INT_MIN, finalLeft, finalTop, finalBottom, finalRight;
    int left, right, i;
    int temp[n], sum, start, finish;
    for(left = 0; left < m; left++)
    {
        memset(temp, 0, sizeof(temp));
        for(right = left, right < m; right++)
        {
            for(i = 0; i < n; i++)
                temp[i]+=M[i][right];
            sum = kadane(temp, &start, &finish, n);
            if(sum > maxSum)
            {
                finalLeft = left;
                finalRight = right;
                finalTop = start;
                finalBottom = finish;
            }
        }
    }
    return maxSum;
}


int main()
{
    // Program to find maximum sum subarray in a given 2D array
#include <stdio.h>
#include <string.h>
#include <limits.h>
#define ROW 4
#define COL 5

// Implementation of Kadane's algorithm for 1D array. The function
// returns the maximum sum and stores starting and ending indexes of the
// maximum sum subarray at addresses pointed by start and finish pointers
// respectively.
int kadane(int* arr, int* start, int* finish, int n)
{
    // initialize sum, maxSum and
    int sum = 0, maxSum = INT_MIN, i;

    // Just some initial value to check for all negative values case
    *finish = -1;

    // local variable
    int local_start = 0;

    for (i = 0; i < n; ++i)
    {
        sum += arr[i];
        if (sum < 0)
        {
            sum = 0;
            local_start = i+1;
        }
        else if (sum > maxSum)
        {
            maxSum = sum;
            *start = local_start;
            *finish = i;
        }
    }

     // There is at-least one non-negative number
    if (*finish != -1)
        return maxSum;

    // Special Case: When all numbers in arr[] are negative
    maxSum = arr[0];
    *start = *finish = 0;

    // Find the maximum element in array
    for (i = 1; i < n; i++)
    {
        if (arr[i] > maxSum)
        {
            maxSum = arr[i];
            *start = *finish = i;
        }
    }
    return maxSum;
}

// The main function that finds maximum sum rectangle in M[][]
void findMaxSum(int M[][COL])
{
    // Variables to store the final output
    int maxSum = INT_MIN, finalLeft, finalRight, finalTop, finalBottom;

    int left, right, i;
    int temp[ROW], sum, start, finish;

    // Set the left column
    for (left = 0; left < COL; ++left)
    {
        // Initialize all elements of temp as 0
        memset(temp, 0, sizeof(temp));

        // Set the right column for the left column set by outer loop
        for (right = left; right < COL; ++right)
        {
           // Calculate sum between current left and right for every row 'i'
            for (i = 0; i < ROW; ++i)
                temp[i] += M[i][right];

            // Find the maximum sum subarray in temp[]. The kadane()
            // function also sets values of start and finish.  So 'sum' is
            // sum of rectangle between (start, left) and (finish, right)
            //  which is the maximum sum with boundary columns strictly as
            //  left and right.
            sum = kadane(temp, &start, &finish, ROW);

            // Compare sum with maximum sum so far. If sum is more, then
            // update maxSum and other output values
            if (sum > maxSum)
            {
                maxSum = sum;
                finalLeft = left;
                finalRight = right;
                finalTop = start;
                finalBottom = finish;
            }
        }
    }

    // Print final values
    printf("(Top, Left) (%d, %d)\n", finalTop, finalLeft);
    printf("(Bottom, Right) (%d, %d)\n", finalBottom, finalRight);
    printf("Max sum is: %d\n", maxSum);
}

// Driver program to test above functions
int main()
{
    int M[ROW][COL] = {{1, 2, -1, -4, -20},
                       {-8, -3, 4, 2, 1},
                       {3, 8, 10, 1, 3},
                       {-4, -1, 1, 7, -6}
                      };

    int ans = findMaxSum(M);
    cout << ans <<endl;
}
