#include <iostream>
#include <stdio.h>
using namespace std;

struct Interval
{
	int start, end;
};

bool compareIntervals(const Interval &e1, const Interval &e2)
{
	return e1.start < e2.start;
}

class Solution
{
public:
	vector<Interval> merge(vector<Interval> &intervals)
	{
		vector<Interval> ans;
		if(intervals.empty())
			return ans;

		sort(intervals.begin(), intervals.end(), compareIntervals);
		int s = intervals[0].start;
		int e = intervals[0].end;
		for(int i = 1; i < intervals.size(); i++)
		{
			if(intervals[i].start <= e)
			{
				e = max(e, intervals[i].end);
			}
			else{
				ans.push_back(Interval(s, e));
				s = intervals[i].start;
				e = intervals[i].end;
			}
		}
		ans.push_back(Interval(s, e));
		return ans;
	}
};