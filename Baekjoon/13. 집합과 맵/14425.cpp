#include <iostream>

using namespace std;

int main()
{
    string s1[10000]={0};
    string s2[10000]={0};
    int n;
    int m;

    cin>>n;
    cin>>m;

    string tmp;
    for(int i=0;i<n;i++)
    {
        cin>>tmp;
        s1[i]=tmp;
    }

    for(int i=0;i<m;i++)
    {
        cin>>tmp;
        s2[i]=tmp;
    }

    int result=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(s1[i]==s2[j])
            {
                result++;
                break;
            }
        }
    }

    cout<<result;

    return 0;
}