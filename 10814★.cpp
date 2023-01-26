#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <tuple>

using namespace std;

bool cmp(tuple<int, string,int> t1, tuple<int, string,int> t2)
{
    if (get<0>(t1) == get<0>(t2))
    {
        return get<2>(t1) < get<2>(t2);
    }
    return get<0>(t1)<get<0>(t2);
}

int main()
{
    int N;
    cin >> N;

    vector <tuple<int, string,int>> v; 
    //idx를 추가로 저장하는 자료구조 tuple 생성
    //tuple은 get<index>(tuple)을 통해 값을 가져올 수 있다.

    int age;
    string name;
    for (int i = 0; i < N; i++)
    {
        cin >> age;
        cin >> name;
        v.push_back(make_tuple(age, name,i));
    }

    sort(v.begin(), v.end(), cmp);

    for (auto&e:v)
    {
        cout << get<0>(e) << " " << get<1>(e) << '\n';
    }

    return 0;
}