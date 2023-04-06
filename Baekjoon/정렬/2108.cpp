#include <iostream>
#include <algorithm>
#include <cmath> //round, ceil, floor

using namespace std;

int main()
{
    int N;
    scanf("%d",&N);

    int A[500000]={0};
    int Cnt[8001]={0}; // 수 카운트. 절댓값 4000을 넘지 않음 => -4000~4000
    int tmp;

    for(int i=0;i<N;i++)
    {
        scanf("%d",&tmp);
        A[i]=tmp;
        Cnt[tmp+4000]+=1;
    }

    // 1. 평균
    float s=0;

    for(int i=0;i<N;i++)
    {
        s+=A[i];
    }

    s=s/N;
    s=round(s);

    printf("%d\n",int(s));

    // 2. 중앙값
    sort(A,A+N);

    printf("%d\n",A[N/2]); // N은 홀수. 배열은 0부터 시작.

    // 3. 최빈값
    int m=0;
    int m_num=0;
    int flag=0; // 최빈값 여러 개 있을 때, 두 번째로 작은 값을 출력하기 위해

    for(int i=0;i<8001;i++)
    {
        if(m<Cnt[i])
        {
            m=Cnt[i];
            m_num=i-4000;
            flag=0;
        }
        else if(m==Cnt[i] and m_num!=0 and flag==0) // 같은 최빈값 나온 것이 이번이 처음 = 두 번째로 작은 값
        {
            m_num=i-4000;
            flag=1;
        }
    }

    printf("%d\n",m_num);

    // 4. 범위
    // 배열 A가 현재 정렬되어 있으므로 최대 idx-최소 idx
    int r=0;
    r=A[N-1]-A[0];

    printf("%d\n",r);

    return 0;
}