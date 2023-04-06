#include <iostream>
#include <vector>
#include <algorithm> //unique

using namespace std;

int main()
{
    vector <int> v;
    int a[1000000];
    int N;
    cin >> N;

    int tmp;
    for (int i = 0; i < N; i++)
    {
        cin >> tmp;
        v.push_back(tmp);
        a[i] = tmp;
    }

    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    // unique 함수는 중복된 원소를 제거하며 앞에서부터 원소를 채워나간다.
    // unique한 값들 다음의 위치를 return하기 때문에 erase를 사용하여 정리할 수 있다.

    //for (auto& e : v)
    //{
    //    cout << e << endl;
    //}
    for (int i = 0; i < N; i++)
    {
        cout << find(v.begin(),v.end(),a[i])-v.begin() << " ";
    }

    return 0;
}