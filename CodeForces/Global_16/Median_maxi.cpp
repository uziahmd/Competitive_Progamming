#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    
    long long T;
    cin>>T;
    for(int t=0; t<T; t++){
    long long n,s,y;
    
    cin>>n>>s;
    
    y=s/((n/2)+1);
    
    cout<<y<<"\n";
    }

return 0;
}