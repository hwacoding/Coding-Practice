#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int N;
    int M;
    int arr[500000]={0};

    cin>>N;

    int tmp;
    for(int i=0;i<N;i++)
    {  
        cin>>tmp;
        arr[i]=tmp;
    }

    bool flag=false;
    cin>>M;
    for(int i=0;i<M;i++)
    {
        cin>>tmp;
        for(int j=0;j<N;j++)
        {
            if(tmp==arr[j])
            {
                flag=true;
                printf("1 ");
                break;
            }
        }
        
        if(flag==false)
        {
            printf("0 ");
        }
        flag=false;
    }

    return 0;
}