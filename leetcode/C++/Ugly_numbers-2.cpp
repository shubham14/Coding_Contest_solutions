#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

struct Solution{
	int nthUglyNumber(int n)
	{
		vector <int> res (1,1);
		int i = 0, j = 0, k = 0;
		while(results.size() < n)
		{
			results.push_back(min(results[i] * 2), min(results[j] * 3, results[k] * 5));
			if (results.back() == results[i] * 2)
				++i;
			else if(results.back() == results[j] * 3)
				++j;
			else
				++k;
		} 
		return results.back();
	}
};

int main()
{
	Solution sol;
	int n;
	cout << "Enter the number" << endl;
	cin >> n;
	int ans = sol.nthUglyNumber(n);
	cout << ans << endl;
	return 0;
}