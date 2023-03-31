#include <iostream>
using namespace std;
int nPrime(unsigned int n);
bool isPrime(unsigned int n);
int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);
    unsigned int n;
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>n;
        unsigned int a=nPrime(n);
        cout<<a<<'\n';
    }
    return 0;
}
int nPrime(unsigned int n){
    if(n<=2)
        return 2;
    while(1){
        bool check=isPrime(n);
        if(check){
            break;
        }
        ++n;
    }
    return n;
}
bool isPrime(unsigned int n){
    for(unsigned int i=2;i*i<=n;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}