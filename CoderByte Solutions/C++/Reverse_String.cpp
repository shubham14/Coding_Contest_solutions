#include <iostream>
#include <string.h>
using namespace std;

string FirstReverse(string str) { 
  // code goes here   
  int n = str.size();
  int end = n - 1;
  int start = 0;
  // swap characters
  while(start <= end)
  {
      char temp = str[start];
      str[start++] = str[end];
      str[end--] = temp;
  }
  return str; 
            
}

int main() { 
  
  // keep this function call here
  cout << FirstReverse(gets(stdin));
  return 0;
    
}