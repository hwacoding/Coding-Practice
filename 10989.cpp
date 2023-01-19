//시간 제한 5초
//메모리 제한 8MB

//주어지는 수의 개수 10,000,000로 많다.
//수의 범위인 10,000보다 작거나 같은 자연수임을 활용해야 한다.

#include <iostream>

using namespace std;

int main()
{
	int n;
	scanf("%d",&n);

	const int size = 10001;

	int arr[size] = { 0 }; 
	//idx를 주어진 수라고 생각. 배열 안에는 주어진 수의 중복 수를 저장.

	int idx = 0;

	for (int i = 0; i < n; i++)
	{
		scanf("%d",&idx);
		arr[idx] += 1;
	}

	for (int i=1;i<=10000;i++)
	{
			for (int j = 0; j < arr[i]; j++)
			{
				printf("%d\n",i);
			}
	}

	return 0;
}