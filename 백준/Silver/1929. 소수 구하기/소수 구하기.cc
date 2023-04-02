#include <iostream>
using namespace std;
void prime(int start, int end) {
    bool isPrime = true;
    for (int i = start; i <= end; i++)
    {
        if (i < 2)
            continue;
        for (int j = 2; j * j <= i ; j++)
        {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime)
            cout << i << '\n';
        isPrime = true;
    }
}
int main() { 
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n, m;
    cin >> n >> m;
    prime(n, m);
    return 0;
}