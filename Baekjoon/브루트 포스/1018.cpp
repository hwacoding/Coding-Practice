#include <iostream>
#include <vector>

using namespace std;

int main()
{
    //case 1 : 왼쪽 맨 위 칸이 Black
    //case 2 : 왼쪽 맨 위 칸이 White

    int n;
    int m;
    cin >> n;
    cin >> m;

    vector <string> v;
    string s;

    for (int i = 0; i < n; i++)
    {
        cin >> s;
        v.push_back(s);
    }

    int min = 64;
    int result1 = 0;
    int result2 = 0;

    //case 1, 2를 각각 비교하여 다른 곳마다 1씩 증가.
    for (int k = 0; k <= n - 8; k++) // 입력 받은 보드 행 이동
    {
        for (int l = 0; l <= m - 8; l++) // 입력 받은 보드 열 이동
        {
            for (int i = k; i < k + 8; i++) // case 1
            {
                for (int j = l; j < l+8; j++)
                {
                    if (i % 2 == 0 and j % 2 == 0 and v[i][j] != 'B') 
                    {
                        result1++;
                    }
                    else if (i % 2 == 0 and j % 2 == 1 and v[i][j] != 'W')
                    {
                        result1++;
                    }
                    else if (i % 2 == 1 and j % 2 == 1 and v[i][j] != 'B')
                    {
                        result1++;
                    }
                    else if (i % 2 == 1 and j % 2 == 0 and v[i][j] != 'W')
                    {
                        result1++;
                    }
                }
            }

            for (int i = k; i < k+8; i++) //case 2
            {
                for (int j = l; j < l+8; j++)
                {
                    if (i % 2 == 0 and j % 2 == 0 and v[i][j] != 'W')
                    {
                        result2++;
                    }
                    else if (i % 2 == 0 and j % 2 == 1 and v[i][j] != 'B')
                    {
                        result2++;
                    }
                    else if (i % 2 == 1 and j % 2 == 1 and v[i][j] != 'W')
                    {
                        result2++;
                    }
                    else if (i % 2 == 1 and j % 2 == 0 and v[i][j] != 'B')
                    {
                        result2++;
                    }
                }
            }

            if (result1 < result2)
            {
                if (min > result1)
                {
                    min = result1;
                }
            }
            else
            {
                if (min > result2)
                {
                    min = result2;
                }
            }

            result1 = 0;
            result2 = 0;
        }
    }

    cout << min << endl;

    return 0;
}