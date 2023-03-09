#include <iostream>

using namespace std;

int main()
{
    int h;
    int m;

    string s1;
    string s2;

    int result=0;

    for(int i=0;i<5;i++)
    {
        cin>>s1;
        cin>>s2;

        h=(s2[0]*10+s2[1])-(s1[0]*10+s1[1]);
        m=(s2[3]*10+s2[4])-(s1[3]*10+s1[4]);

        result+=60*h+m;
    }

    cout<<result<<endl;
    
    return 0;
}