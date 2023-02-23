#include <iostream>
 
using namespace std;
 
int main() {
 
    int a[101]={0,};    
    int n;
    int target;
    int max=0;
    int sum=0;
 
    cin>>n>>target;
 
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
 
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            for(int k=j+1; k<n; k++){
                sum=a[i]+a[j]+a[k];
                if(sum<=target&&sum>max)
                max=sum;
            }
        }
    }
 
    cout<<max;
}