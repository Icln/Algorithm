#include<iostream>
#include<stack>
#include<string>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    while (true)
    {
        stack<char>st;
        string str;
        bool check = true;
        getline(cin, str);
        if (str.length() == 1 && str[0] == '.')
            break;
        for (int i = 0; i < str.size(); i++)
        {
            if (str[i] == '(' || str[i] == '[')
                st.push(str[i]);
            else if (str[i] == ')')
            {
                if (st.empty() || st.top() != '(')
                {
                    check = false;
                    break;
                }
                st.pop();
            }
            else if (str[i] == ']')
            {
                if (st.empty() || st.top() != '[')
                {
                    check = false;
                    break;
                }
                st.pop();
            }
        }
        if (!check || !st.empty())
            cout << "no" << endl;
        else
            cout << "yes" << endl;
    }
}