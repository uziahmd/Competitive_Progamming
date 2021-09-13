#include <fstream>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

ofstream output("output.txt");
ifstream input("input.txt");
const int m =1000000007;
std::vector<string> subs;

int main()
{
int N, T;
input >> T;
    for(int t=1; t <= T; t++)
    {
        int N;
        input >> N;
        string s;
        input>>s;
        long long final_count=0;
        for(int j=0;j<N;j++){
        long long count1=0;
        long long count2=0;
        bool flag1= false;
        bool flag2= false;
        
        for(int i=j;i<s.length();i++)
        {
            if(flag1==false &&s[i]=='O')
            {
                flag1=true;
                count1++;
            }
            if(flag1== true && s[i]=='X')
            {
                flag1=false;
                count1++;
            }
            if(flag2 == false && s[i] =='X')
            {
                flag2 = true;
                count2++;
            }
            if(flag2 == true && s[i] == 'O')
            {
                flag2 = false;
                count2++;
            }
            long long count = min(count1,count2);
            final_count += count;
            final_count %= m;
        }
    }
    output << "Case #" << t << ": " << final_count << "\n";
    cout << "Case #" << t << ": " << final_count << "\n";
}

return 0;
}