#include <iostream>

using namespace std;

//브루트 포스 : 무식한 힘 : 완전 탐색 알고리즘

int main()
{
    int a[100];
    int N;
    int M;

    cin>>N>>M;
    
    int tmp;
    for(int i=0;i<N;i++)
    {
        cin>>tmp;
        a[i]=tmp;
    }

    int sum=0;
    int first;
    int second;
    int third;

    int result=0;
    for(int i=0;i<N-2;i++)
    {
        first=a[i];
        for(int j=i+1;j<N-1;j++)
        {
            second=a[j];
            for(int k=j+1;k<N;k++)
            {
                third=a[k];
                sum=first+second+third;
                // cout<<first<<" "<<second<<" "<<third<<endl;
                // cout<<sum<<endl;

                if(sum<=M and M-sum<M-result)
                {
                    result=sum;
                }
            }
        }
    }

    cout<<result<<endl;

    return 0;
}