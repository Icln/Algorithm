#include <iostream>
using namespace std;
int main() {
    int ans[10000] = { 10000 }, N , K, cnt = 0, p = 0;
    cin >> N >> K;
    for(int i = 1; i < 10000; i++)
    {
        if (i > N)
            break;
        if (N % i == 0)
        {
            cnt++;
            ans[p++] = i;
        }
    }
    if (cnt < K)
        cout << "0";
    else
        cout << ans[K - 1];
}