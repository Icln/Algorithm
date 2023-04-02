#include <iostream>
using namespace std;
int prime(int start, int end) {
    bool isPrime = true;
    int result = 0;
    for (int i = start; i <= end; i++)
    {
        if (i == 1 || i == 2 || i == 3)
            return 1;
        for (int j = 2; j * j <= i ; j++)
        {
            if (i == start || i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime)
            result++;
        isPrime = true;
    }
    return result;
}
int main() { 
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;
    do
    {
        cin >> n;
        if (n)
        {
            cout << prime(n, 2 * n) << '\n';
        }
    } while (n);
       
    return 0;
}