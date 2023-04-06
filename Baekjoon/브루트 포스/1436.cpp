#include <iostream>
#include <string> //to_string(int), s.length()

using namespace std;

int main()
{
    int N;

    cin>>N;

    int k=666;
    string s=to_string(k);

    while(1)
    {
        if(N==0)
        {
            break; // N번째 큰 수 이면, break
        }

        // '666' check
        for(int i=0;i<s.length()-2;i++)
        {
            if(s[i]=='6' and s[i+1]=='6' and s[i+2]=='6')
            {
                N--;
                break;
            }
        }
        // 1씩 증가 
        k++;
        s=to_string(k);
    }
    
    k=k-1;
    cout<<k<<endl;

    return 0;
}