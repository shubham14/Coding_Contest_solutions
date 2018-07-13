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
			// backtracking step
			swap(str + i, str + l);
		}
	}
	return ans;
}

// pretty printing of the contents of the vector
void pretty_print_vector(vector<char*> v)
{
	int n = v.size();
	for(int i = 0; i < n; i++)
	{
		cout<<v[i]<<"-"
	}
	cout<<endl;
}

int main()
{
	char *str = "permutation";
	int n = sizeof(str)/sizeof(str[0]);
	int r = 0;
	int l = n-1;
	vector<char*> ans;
	ans = permute(str, l, r);
	
	// Display the readings
	pretty_print_vector(ans);
	return 0;
}