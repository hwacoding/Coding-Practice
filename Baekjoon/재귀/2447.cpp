#include <iostream>
#include <cmath>

using namespace std;

char result[2187][2187]={{'*','*','*'},{'*',' ','*'},{'*','*','*'}};

void star(int N)
{
    //0~2 옆으로 3 복사
    //3~5 비우기
    //6~8 첫 번째꺼 복사
    //index가 중요!


    if(N/3==1)
    {
        return; //break point
    }
    else
    {
        star(N/3); //재귀

        for(int k=0;k<N/3;k++)
        {
            for(int i=N/3;i<N;i++)
            {
                result[k][i]=result[k][i%3]; // 첫 번째
            }
        }

        for(int k=N/3;k<2*N/3;k++)
        {
            for(int i=0;i<N/3;i++)
            {
                result[k][i]=result[k-N/3][i];
            }
            for(int i=N/3;i<2*N/3;i++)
            {
                result[k][i]=' ';
            }
            for(int i=2*N/3;i<N;i++)
            {
                result[k][i]=result[k-N/3][i];
            }
        }

    }



//     return tmp;
}

int main()
{
    
    star(27);

    cout<<result[0]<<endl;
    cout<<result[1]<<endl;
    cout<<result[2]<<endl;
    cout<<result[3]<<endl;
    cout<<result[4]<<endl;
    cout<<result[5]<<endl;
    cout<<result[6]<<endl;



    return 0;
}