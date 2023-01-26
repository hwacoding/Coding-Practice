#include <iostream>
#include <vector> // vector<pair<int,int>> 2차원 정렬을 위해 vector 활용.
#include <algorithm> //sort

using namespace std;

bool cmp(pair<int,int> p1,pair<int,int> p2)
{
    if(p1.first==p2.first)
    {
        return p1.second<p2.second; // 같으면, 두 번째 값 기준으로 오름차순
    }
    else
    {
        return p1.first<p2.first; // 다르면, 오름차순
    }
}

int main()
{
    int N;
    cin>>N;

    vector <pair<int,int>> v; //pair -> first, second

    int a,b;

    for(int i=0;i<N;i++)
    {
        scanf("%d",&a);
        scanf("%d",&b);
        v.push_back(make_pair(a,b));
    }

    sort(v.begin(),v.end(),cmp);
    
    for(auto& e:v)
    {
        cout<<e.first<<" "<<e.second<<"\n";
    }
}