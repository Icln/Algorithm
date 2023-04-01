#include <iostream>
using namespace std;
bool isPrime(unsigned int n) {
    for (unsigned int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}
unsigned int nPrime(unsigned int n) {
    if (n <= 2)
        return 2;
    while (true) {
        bool check = isPrime(n);
        if (check) {
            break;
        }
        ++n;
    }
    return n;
}
int main() { 
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    unsigned int  n;
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        unsigned int a = nPrime(n);
        cout << a << '\n';
    }
    return 0;
}