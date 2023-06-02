//1. 아이디어
// - 주어진 바구니 바꾼다.
// - 반복.
//
//2. 시간복잡도
// - O(n*m) = 10000

#include <iostream>

using namespace std;

int main()
{
	int n, m;
	cin >> n >> m;

	int a, b, c;
	int result[101] = { 0 };
	for (int i = 0; i < m; i++)
	{
		cin >> a >> b >> c;
		for (int j = a; j < b + 1; j++)
		{
			result[j] = c;
		}
	}

	for (int i = 1; i < n + 1; i++)
	{
		cout << result[i] << " ";
	}

	return 0;
}