#include <iostream>
#include <string> //string, str.length()
#include <algorithm> //sort
#include <cmath> //pow

using namespace std;

int main()
{
    int A[10]={0};

    string s;
    cin>>s;
    
    for(int i=0;i<s.length();i++)
    {
        A[i]=int(s[i])-48; // ASCII Code -> integer
    }

    sort(A,A+s.length());

    int result=A[0];
    
    for(int i=1;i<s.length();i++)
    {
        result+=A[i]*pow(10,i);
    }

    cout<<result;
}