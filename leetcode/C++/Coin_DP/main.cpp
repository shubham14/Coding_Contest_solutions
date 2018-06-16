#include <iostream>
#include <stdio.h>
#include <vector>
#include <limits.h>
#include <algorithm>
#include <stack>
#include <math.h>

using namespace std;

// reverse number using stack
int reverse_num(int x)
{
    if(x > INT_MAX - 1 || x < INT_MIN)
        return 0;
    int mul = 1;
    if (x < 0)
    {
        mul = -1;
        x *= -1;
    }
    int ans = 0;
    while(x != 0)
    {
        int res = x % 10;
        ans = 10*ans + res;
        x = x/10;
    }
    return mul * ans;
}

// recursive solution
int rod_cut(int price[], int n)
{
    if(n <= 0)
        return 0;
    int max_val = INT_MIN;
    for(int i = 0; i < n; i++)
    {
        max_val = max(max_val, price[i] + rod_cut(price, n-i-1));
    }
    return max_val;
}

// DP solution
int cut_rod(int price[], int n)
{
    int val[n+1];
    val[0] = 0;
    int i, j;
    for(i = 1; i <= n; i++)
    {
        int max_val = INT_MIN;
        for(j = 0; j < i; j++)
        {
            max_val = max(max_val, price[j] + val[i-j-1]);
        }
        val[i] = max_val;
    }
    return val[n];
}

int coin_count(int S[], int m, int n)
{
    int i,j;
    int table[n+1][m];
    for(i = 0; i < m; i++)
    {
        table[0][i] = 1;
    }
    for(i = 1; i < n + 1; i++)
    {
        for(j = 0; j < m; j++)
        {
            int x, y;
            x = (i - S[j] >= 0)? table[i-S[j]][j]:0;
            y = (j >= 1)? table[i][j-1]: 0;
            table[i][j] = x + y;
        }
    }
    return table[n][m-1];
}


int main()
{
    int num = 901000;
    cout<<reverse_num(num)<<endl;
    return 0;
}
