//1. 아이디어
// - 정렬 후, 맨 앞과 맨 뒤 포인터를 활용.
// - 합이 M보다 크면, 맨 뒤 포인터를 앞으로
// - 합이 M보다 작으면, 맨 앞 포인터를 뒤로 옮긴다.
//
//2. 시간복잡도
// - O(nlog(n)+n) = 15000*15 = 225000

#include <iostream>
#include <algorithm> // sort

using namespace std;

int main()
{
	int n, m;
	cin >> n >> m;

	int A[15001] = { 0 };
	int tmp;

	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		A[i] = tmp;
	}

	sort(A, A + n);
	//for (int i=0;i<n;i++)
	//{
	//	cout << A[i] << " ";
	//}
	//cout << "\n";

	int left=0;
	int right = n - 1;
	int sum = 0;
	int result = 0;

	while (1)
	{
		//cout << A[left] << " "<<A[right] << " "<<sum<<"\n";
		//cout << result<<"\n";
		if (left == right)
		{
			break;
		}

		sum = A[left] + A[right];
		if (sum == m)
		{
			result++;
			left++;
		}
		else if(sum<m)
		{
			left++;
		}
		else if (sum > m)
		{
			right--;
		}
	}

	cout << result;

	return 0;
}