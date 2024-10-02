#include <stdio.h>
#include <stdlib.h>

#define INF 9999
#define V 5

int key[V];

int parent[V];
int cost[V][V] = {
    {0, 2, 0, 6, 0},
    {2, 0, 3, 8, 5},
    {0, 3, 0, 0, 7},
    {6, 8, 0, 0, 9},
    {0, 5, 7, 9, 0}
};
int visited[V] = {0};

void display() {
    int i, j;
    printf("\nThe cost of adjacency matrix\n\n");
    for (i = 0; i < V; i++) {
        for (j = 0; j < V; j++) {
            if (cost[i][j] == INF) {
                printf("INF\t");
            } else {
                printf("%d\t", cost[i][j]);
            }
        }
        printf("\n");
    }
}

int minKey() {
    int min = INF, min_index;
    int v;
    for ( v = 0; v < V; v++) {
        if (visited[v] == 0 && key[v] < min) {
            min = key[v];
            min_index = v;
        }
    }
    return min_index;
}

void prims() {
	int i;
    for (i = 0; i < V; i++) {
        key[i] = INF;
        visited[i] = 0;
        parent[i] = -1;
    }

    key[0] = 0;

int count ;
    for ( count = 0; count < V - 1; count++) {
        int u = minKey();
        visited[u] = 1;
int v;
        for (v = 0; v < V; v++) {
            if (cost[u][v] !=0 && visited[v] == 0 && cost[u][v] < key[v]) {
                parent[v] = u;
                key[v] = cost[u][v];
            }
        }
    }

    printf("\nEdge \tWeight\n");
   
    for (i = 1; i < V; i++) {
        printf("%d - %d \t%d \n", parent[i], i, cost[i][parent[i]]);
    }
}

int main() {
    printf("Prim's Algorithm\n");
    display();
    prims();
    return 0;
}

