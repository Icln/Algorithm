#include <iostream>
using namespace std;
long long fiboarr[100] = {0,1,};
long long fibo(int N)
{
    if(N == 0 || N == 1)
        return fiboarr[N];
    else if(fiboarr[N] == 0)
        fiboarr[N] = fibo(N-1) + fibo(N-2);
    return fiboarr[N];
}
int main() {
    int N;
    cin >> N;
    cout << fibo(N);
}