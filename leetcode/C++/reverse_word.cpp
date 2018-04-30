#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

class Solution
{
public:
	char *str;
	// function to reverse each word
	void reverseWord(char *start, char *end);
	// function to reverse the whole string
	void reverse(char *str);
	Solution(char *str1)
	{
		this.str = str1;
	}
};

//reverse each segment, acts as a wrapper
void Solution::reverseWord(char *start, char *end)
{
	char temp;
	while(start < end)
	{
		temp = *start;
		*start++ = *end;
		*end-- = temp; 
	}
}

//main function
void Solution::reverse(char *str)
{
	char *start = *str;
	char *temp = *str;
	while(temp)
	{
		*temp++;
		if(*temp == ' ')
		{
			reverseWord(start, temp-1);
			start = temp + 1;
		}
		else if(*temp == '\0')
		{
			reverseWord(start, temp-1);
		}
	}
}

int main()
{
	char *str = "I am Shubham Dash"
	Solution sol;
	sol.reverse(str)
	return 0;
}