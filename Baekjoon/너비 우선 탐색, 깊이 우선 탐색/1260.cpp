#include <iostream>
#include <queue>
#include <memory.h> //memset

using namespace std;

int n, m, v;
bool visited[1001] = { false };
int mp[1001][1001] = { 0 };

void dfs(int& v)
{
    cout << v << " ";
    visited[v] = true;

    for (int i = 1; i < n+1; i++)
    {
        if (mp[v][i] == 1 && visited[i] == 0)
        {
            dfs(i);
        }
    }
}

void bfs(int& v)
{
    queue <int> q;
    q.push(v);
    visited[v] = true;
    cout << v << " ";

    while (!q.empty())
    {
        int nv = q.front();
        q.pop();
        
        for (int i = 0; i < n+1; i++)
        {
            if (mp[nv][i] == 1 && visited[i] == false)
            {
                q.push(i);
                cout << i << " ";
                visited[i] = true;
            }
        }
    }
}

int main()
{
    cin >> n>>m>>v;

    for (int i = 0; i < m; i++)
    {
        int a,b;
        cin >> a>>b;

        mp[a][b] = 1;
        mp[b][a] = 1;
    }

    dfs(v);

    cout << endl;

    memset(visited, false, sizeof(bool) * 1001); //초기화

    bfs(v);

    return 0;
}