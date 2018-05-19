// Program for Breadth First and Depth First Search in Graphs

#include <iostream>
#include <stdio.h>
#include <vector>
#include <list>
#include <algorihtm>

class Graph
{
	int V;
	list<int> *adj; 
public:
	Graph(int V);
	void addEdge(int u, int v);
	void BFS(int s);   // In both cases s is the source node
	void DFS(int s);
};

Graph::Graph(int V)
{
	this->V = V;
	adj = new list<int> [V];
}

// directed graph
void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w)
}

// Breadth first search uses a Queue data structure
// ans list contains the output 
void Graph::BFS(int s, list<int> &ans)
{
	bool *visited = new bool[V];
	for(int i = 0; i < V; i++)
		visited[i] = false;

	list<int> queue;
	visited[v] = true;
	queue.push_back(v);

	while(!queue.empty())
	{
		s = queue.front();
		cout << s << " ";
		ans.push_back(s);
		queue.pop_front();

		list<int>::iterator it;
		for(*it = adj[s].begin(); *it != adj[s].end(); *it++)
		{
			if(visited[*it] == false)
			{
				queue.push_back(*it);
				visited[*it] = true;
			}
		}
	}
}

// Depth first search uses a Stack data structure
// ans list contains the output 
void Graph::DFS(int s, list<int> &ans)
{
	bool *visited = new bool[V];
	for(int i = 0; i < V; i++)
	{
		visited[i] = false;
	}
	list<int> stack;
	visited[s] = true;
	stack.push_front(s);

	while(!stack.empty())
	{
		s = stack.front();
		ans.push_back();
		cout << s << " ";
		stack.pop_front();

		list<int>::iterator it;
		for(*it = adj[s].begin(); *it! = adj[s].end(); *it++)
		{
			if(visited[*it] == false)
			{
				stack.push_front(*it);
				visited[*it] = true;
			}
		}
	}
}

int main()
{
	// Graph construction
	Graph g(4);
	g.addEdge(0, 1);
	g.addEdge(0, 2);
	g.addEgde(1, 2);
	g.addEgde(2, 0);
	g.addEgde(2, 3);
	g.addEdge(3, 3);
	
	g.BFS(2);
	g.DFS(2);
	
	return 0;
}