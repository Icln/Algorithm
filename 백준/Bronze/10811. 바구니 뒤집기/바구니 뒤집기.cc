#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n, m, i, j;
    cin >> n >> m;
    int *a = new int[n+1];
    for (int i = 1; i <= n; i++)
        a[i] = i;
    while (m--)
    {
        cin >> i >> j;
        for (int t = 0; t <= (j - i) / 2; t++)
        {
            swap(a[t + i], a[j - t]);
        }
    }
    for (int i = 1; i <= n; i++)
        cout << a[i] << ' ';
}