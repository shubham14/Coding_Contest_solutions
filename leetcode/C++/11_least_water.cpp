#include<iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
	int maxArea(vector<int> &height)
	{
		int l = 0;
		int r = (int)height.size()-1;
		area = 0;
		while(l < r)
		{
			area = max(area, min(height[l], height[r])*r);
			if (height[l] < height[r])
				l++;
			else
				r--;
	    }
	    return area;
	}
};