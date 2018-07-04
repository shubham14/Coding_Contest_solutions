#include <iostream>
#include <string.h>
#include <stdio.h>
#include <vector>
using namespace std;

bool permute_palindrome(char *str)
{
    char H[123];
    int counteven = 0;
    int countodd = 0;
    for(int i = 0; i < 123; i++)
    {
        H[(int)tolower(str[i])]++;
    }
    int n = sizeof(str)/sizeof(str[0]);
    for(int i = 0; i < n; i++)
     {
         if(H[(int)tolower(str[i])] % 2 == 0)
            counteven ++;
         else
            countodd ++;
     }
     if(n % 2 == 0)
        if(counteven == n && countodd % 2 == 0)
            return true;
     else if
        if(counteven == n-1 && countodd % 2 == 1)
            return true;
     return false;
}

int main()
{
    char *str = "civic";
    bool ans = permute_palindrome(str);
    cout<<ans<<endl;
    return 0;
}
