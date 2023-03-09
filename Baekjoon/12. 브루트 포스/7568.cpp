#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N;
    int x,y;

    vector <pair<int,int>> v;

    cin>>N;

    for(int i=0;i<N;i++)
    {
        cin>>x;
        cin>>y;
        v.push_back(make_pair(x,y));
    }

    int result=1;
    //자신보다 큰 사람 있으면, result 증가.
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            if(v[i].first<v[j].first and v[i].second<v[j].second) //pair -> first, second
            {
                result++;
            }
        }
        cout<<result<<" ";
        result=1;
    }

    return 0;
}