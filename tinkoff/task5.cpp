#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
   int n;
   cin >> n;
   vector<vector<char>> field (n, vector<char> (3));
   vector<vector<int>> dp (n, vector<int> (3));
   int max_mushrooms = 0;
   for (int i = 0; i < n; i++) {
       for (int j = 0; j < 3; j++) {
           cin >> field[i][j];
           dp[i][j] = 0;
       }
   }
   if (field[0][0] == 'W' && field[0][1] == 'W' && field[0][2] == 'W') {
       cout << max_mushrooms;
       return 0;
   }
   if (field[0][0] == 'C') {
       dp[0][0] = 1;
   }
   if (field[0][1] == 'C') {
       dp[0][1] = 1;
   }
   if (field[0][2] == 'C') {
       dp[0][2] = 1;
   }
   for (int i = 1; i < n; i++) {
       for (int j = 0; j < 3; j++) {
           for (int k = j - 1; k <= j + 1; k++) {
               if(k >= 0 && k < 3 && field[i][j] != 'W' && dp[i - 1][k] != -1) {
                   int mush = 0;
                   if(field[i][j] == 'C') {
                       mush = 1;
                   }
                   dp[i][j] = max(dp[i][j], dp[i-1][k] + mush);
                   }
               }
           }
       }
   for (int i = 0; i < n; i++) {
       for (int j = 0; j < 3; j++) {
           max_mushrooms = max(max_mushrooms, dp[i][j]);
       }
   }
   cout << max_mushrooms;
   return 0;
}
