#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    
    long long T;
    cin>>T;
    for(int t=0; t<T; t++){
    string s;
    cin>>s;
    int m = 0;
    bool check = false;
    for(int a = 0; a < s.size(); a++){
        if (s[a] == '0') check = true;
        else if (s[a] != '0' && check == true) {m++; check = false;}
    }
    if (s[s.size()-1] == '0'){m++;}
    int ans = min(2, m);
    cout<<ans<<"\n";
    }

return 0;
}