#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

int main()
{
	int num, k;
	if (k > (int)log2(num) + 1)
		return -1;

	// forming the number with which the number has to be XORed
	int base_num = (int)pow(2,k);

	//  kth bit toggled
	int ans =  num ^ base_num;
	cout<< ans<< endl;
	return 0;
}