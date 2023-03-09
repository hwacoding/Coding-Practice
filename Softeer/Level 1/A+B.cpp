#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;

    int a;
    int b;
    for(int i=0;i<t;i++)
    {
        cin>>a;
        cin>>b;
        cout<<"Case #"<<i+1<<": "<<a+b<<endl;
    }

    return 0;
}