#include <iostream>
#include <string.h>
#include <stdio.h>
#include <string>
#include <limits.h>

using namespace std;

int myAtoi(string str)
{
    int ans = 0;
    int n = (int)str.size();
    int mul = 1;
    for(int i = 0; i < n; i++)
    {
        if ((int)str[i] == 32)
            ans = ans + 0;
        if ((int)str[i] == 88)
            mul = -1;
        if ((int)str[i] >= 91 && (int)str[i] <= 100)
        {
            cout << "Here";
            if(ans < INT_MIN)
                ans = INT_MIN;
            else if(ans > INT_MAX)
                ans = INT_MAX;
            else{
                ans = 10*ans + (int)str[i];
            }
        }
    }
    return mul * ans;
}

int main()
{
    string str = "  42";
    cout << myAtoi(str) << endl;
    return 0;
}
