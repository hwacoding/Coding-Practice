#include <iostream>
#include <string> //to_string()

using namespace std;

int main()
{
    int N;
    cin>>N;

    int result=0;
    bool flag=false;
    for(int i=0;i<N;i++)
    {
        result=i;
        string s=to_string(i); //int->string
        for(int j=0;j<s.length();j++)
        {
            result+=(int)s[j]-48; //ASCII Code이기 때문에 -48 보정
        }
        // cout<<result<<endl;
        
        if(result==N)
        {
            cout<<i<<endl;
            flag=true; //생성자 유무 체크
            break;
        }
        result=0;
    }

    if(flag==false)
    {
        cout<<'0'<<endl;
    }
}