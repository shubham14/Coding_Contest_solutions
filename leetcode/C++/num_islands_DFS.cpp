#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

#define COL 5

bool isSafe(int A[][COL],int m,int n, int visited[][COL])
{
	return (m < ROW) && (n < COL) && 
		   (m >= 0) && (n >= 0) &&
		   (A[i][j]) && !visited[m][n];
}

void DFS(int M[][COL], int m, int n, int visited[][COL])
{
	int x[] = {-1, -1, -1, 0, 0, 1, 1, 1};
	int y[] = {-1, 0, 1, -1, 1, -1, 0, 1};

	visited[m][n] = true;
	for(int i = 0; i < 8; i++)
	{
		if(isSafe(M, m + x[i], n + y[i] visited))
			DFS(M, m + x[i], n + y[i] visited);
	}
}

int countIslands(int M[][COL])
{
	bool visited[10][ROW];
	memset(visited, 0, sizeof(visited));

	int count = 0;
	for(int i=0;i<10;i++)
	{
		for(int j=0;j<COL;j++)
		{
			if(M[i][j] && !visited[i][j])
			{
				DFS(M, i, j, visited);
				count += 1;
			}
		}
	}
	return count;
}

int main()
{
	int M[][COL] = {  {1, 1, 0, 0, 0},
        {0, 1, 0, 0, 1},
        {1, 0, 0, 1, 1},
        {0, 0, 0, 0, 0},
        {1, 0, 1, 0, 1}
    };
 
    cout<<countIslands(M)<<endl;
 
    return 0;
}