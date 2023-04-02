#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() { 
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n, idx = 0;
    string s;
    vector <pair<string, int>> record;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> s;
        if (!s.compare("ENTER"))
        {
            idx++;
        }
        else {
            record.push_back({s,idx});
        }
    }
    sort(record.begin(), record.end());
    record.erase(unique(record.begin(), record.end()),record.end());
    cout << record.size();
    return 0;
}