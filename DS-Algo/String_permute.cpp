#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

void swap(char *x, char *y)
{
	char temp = *x;
	*x = *y;
	*y = temp;
}

vector<char*> permute(char *str, int l, int r)
{
	vector<char *> ans;
	if(l == r)
		ans.append(str);
	else
	{
		for(int i = l; i <= r; i++)
		{
			swap(str + l, str + i);
			permute(str, l+1, r);
			swap(str + i, str + l);
		}
	}
	return ans;

}