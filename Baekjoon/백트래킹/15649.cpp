#include <iostream>
#include <vector>

using namespace std;

int m, n;
bool visited[9] = { false };
vector <int> v;

void recur(int lev)
{
	if (lev == 0)
	{
		for (auto& e : v)
		{
			cout << e << " ";
		}
		cout << '\n'; //endl 출력 버퍼 비워주기 때문에 속도 느림.
		return;
	}
	
	for (int i = 1; i < m+1; i++)
	{
		if (visited[i] == false)
		{
			visited[i] = true;
			v.push_back(i);
			recur(lev - 1);
			visited[i] = false;
			v.pop_back();
		}
	}

}

int main()
{
	cin >> m >> n;

	recur(n);

	return 0;
}