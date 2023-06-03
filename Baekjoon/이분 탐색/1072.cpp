//1. 아이디어
// - 처음 승률 구한다.
// - 승률이 100%면, -1 출력
// - 1~X 안에서 승률 변화는 부분 찾는다. : 이진 탐색
//
//2. 시간복잡도
// - O(log(X)) 
// - 2^10 ~= 1000
// - O(log(X)) ~= 30

#include <iostream>

using namespace std;

long long x,y;
int z;
int result = 0;

void recur(int left,int right)
{
	
	if (left > right)
	{
		return;
	}

	int mid=(left+right)/2;
 
	long long nx=x + mid;
	long long ny=y + mid;
	int nz = ny * 100 / nx;
	//cout << left << " " << right << endl;
	//cout << nx<<" "<<ny <<" "<< nz << endl;
	if (nz == z)
	{
		recur(mid + 1, right);
	}
	else
	{
		result = mid;
		recur(left, mid-1);
	}
}

int main()
{
	cin >> x >> y;

	z = y*100 / x; // y*100을 하게 되면, int(20억) 초과.
				   // long long으로 변수 선언해야 한다.

	//cout <<"z : "<< z<<endl;

	if (z >= 99)
	{
		cout << "-1";
	}
	else
	{
		recur(1,x);
		cout << result;
	}

	return 0;
}