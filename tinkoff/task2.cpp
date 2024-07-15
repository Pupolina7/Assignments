#include <iostream>
#include <vector>
using namespace std;

int main() {
   int n, m;
   cin >> n >> m;
   vector <vector <long long>> matrix (m, vector <long long> (n) );
   for (int i = n - 1; i >= 0; i--) {
       for (int j = 0; j < m; j++) {
           cin >> matrix[i][j];
       }
   }
   for (int i = 0; i < m; i++) {
       for (int j = 0; j < n; j++) {
           cout << matrix[j][i] << ' ';
       }
       cout << endl;
   }
   return 0;
}
