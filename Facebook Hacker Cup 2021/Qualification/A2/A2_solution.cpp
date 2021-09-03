#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;
ifstream input("input.txt");

const int INF = 1e6;

string S;
int K;
int dist[26][26];

int solve() {
  for (int i = 0; i < 26; i++) {
    for (int j = 0; j < 26; j++) {
      dist[i][j] = (i == j) ? 0 : INF;
    }
  }
  input >> S >> K;
  for (int i = 0; i < K; i++) {
    char a, b;
    input >> a >> b;
    dist[a - 'A'][b - 'A'] = 1;
  }
  for (int k = 0; k < 26; k++) {
    for (int i = 0; i < 26; i++) {
      for (int j = 0; j < 26; j++) {
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
      }
    }
  }
  int ans = INF;
  for (int i = 0; i < 26; i++) {
    int curr = 0;
    for (char c : S) {
      curr += dist[c - 'A'][i];
    }
    ans = min(ans, curr);
  }
  return ans == INF ? -1 : ans;
}

int main() {

  int T;
  input >> T;
  ofstream output("output.txt");
  for (int t = 1; t <= T; t++) {
    output << "Case #" << t << ": " << solve() << endl;
  }
  return 0;
}