#include <iostream>
#include <set> //set, set.insert('a')
#include <string>
#include <algorithm>

using namespace std;

struct cmp {
    bool operator() (const string& s1, const string& s2) const // 기존 구조체에서 const였기에 유지하지 않으면, 한정자 손실됨.
    {
        if (s1.length() == s2.length())
        {
            return s1 < s2;
        }
        return s1.length() < s2.length();
    }
};

int main()
{
    int N;
    cin >> N;

    set <string, cmp> S;
    // set template = type, struct(bool operator())


    string s;

    for (int i = 0; i < N; i++)
    {
        cin >> s;
        S.insert(s);
    }

    for (auto& e : S)
    {
        cout << e << "\n";
    }

    return 0;
}