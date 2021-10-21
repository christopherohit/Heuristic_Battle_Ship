#include <stdio.h>
#include <queue>
#include <conio.h>
using namespace std;

// dinh nghia lop do thi
class Graph
{
private:
	int n;
	int **edge;
public:
	Graph(int size = 2);
	~Graph();
	bool isConnected(int, int);
	void addEdge(int, int);
	void breadthFirstSearch(int, int);
};

Graph::Graph(int size)
{
	int i, j;

	// xac dinh so dinh cua do thi
	n = size < 2 ? 2 : size;

	// tao ra cac dinh trong do thi
	edge = new int*[n];
	for (i = 0; i < n; i++)
		edge[i] = new int[n];
	
	// mac dinh giua cac dinh khong co ket noi voi nhau (= 0)
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			edge[i][j] = 0;
}

Graph::~Graph()
{
	for (int i = 0; i < n; ++i)
		delete[] edge[i];
	delete[] edge;
}

// kiem tra giua hai dinh co ke nhau hay khong
bool Graph::isConnected(int x, int y)
{
	return edge[x - 1][y - 1] == 1;
}

// tao canh noi giua hai dinh, lam cho hai dinh ke nhau
void Graph::addEdge(int x, int y)
{
	if (x < 1 || x > n || y < 1 || y > n)
		return;

	edge[x - 1][y - 1] = edge[y - 1][x - 1] = 1;
}

void Graph::breadthFirstSearch(int s, int g)
{
	if (s > n || s < 0 || g > n || g < 0)
	{
		printf("Could not traverse this graph with your request\n");
		return;
	}

	queue<int> open;
	bool *close = new bool[n];
	int i;
	int p;

	// mac dinh cac dinh chua duoc duyet
	for (i = 0; i < n; i++)
		close[i] = false;

	// dua dinh goc s vao queue open, chuan bi duyet
	open.push(s);

	printf("With Breadth first Search , we have vertex(s):\n");

	while (!open.empty())
	{
		// lay mot dinh ra khoi open tro thanh dinh dang xet p
		do
		{
			if (open.empty())
				break;

			p = open.front();
			open.pop();
		} while (close[p - 1] == true);

		// in ra dinh dang xet
		printf("%d ", p);

		// p da duyet qua
		close[p - 1] = true;

		// ket thuc duyet khi tim ra ket qua can tim
		if (p == g)
			break;
		
		// tim dinh ke voi dinh dang xet, dinh nao chua duoc duyet dua vao open
		for (i = 1; i <= n; i++)
		{
			if (isConnected(p, i) && !close[i - 1])
			{
				open.push(i);
			}
		}
	}
	printf("\n");

	delete[] close;
}
int main()
{
	// khoi tao do thi
	Graph g(7);

	// tao canh noi giua cac dinh ke
	g.addEdge(1, 2);
	g.addEdge(1, 3);
	g.addEdge(1, 5);
	g.addEdge(2, 6);
	g.addEdge(2, 4);
	g.addEdge(3, 7);
	g.addEdge(3, 4);
	g.addEdge(5, 4);
	g.addEdge(6, 6);
	g.addEdge(7, 7);
	
g.breadthFirstSearch(1, 7);
	return 0;
}
