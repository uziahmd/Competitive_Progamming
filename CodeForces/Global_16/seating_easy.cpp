#include <vector>
#include <iostream>

using namespace std;
#define ff(a, c)        for (int(a) = 0; (a) < (c); (a)++)
#define w(x)            int x; cin >> x; while(x--)

int main() {
   w(t) {
      long long n, m;
      cin >> n >> m;
      
      long long int a[m];
      ff(i, m) cin >> a[i];
      vector<int>st;
      st.push_back(a[0]);
      int ans = 0;
      ff(i, m) {
         if (i == 0) continue;
         int k = 0;
         ff(j, st.size()) {
            if (st[j] < a[i]) k++;
         }
         st.push_back(a[i]);
         ans += k;
      }
      cout << ans << endl;
   }
   cout.clear();
   cin.clear();
   return 0;
}