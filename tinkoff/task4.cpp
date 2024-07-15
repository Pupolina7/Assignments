//#include <iostream>
//#include <vector>
//using namespace std;
//
//int main() {
//    int n;
//    char rotate;
//    cin >> n >> rotate;
//    vector <vector <long long>> matrix (n, vector <long long> (n));
//    vector <long long> output;
//    for (int i = 0; i < n; i++) {
//        for (int j = 0; j < n; j++) {
//            cin >> matrix[i][j];
//        }
//    }
//    if (rotate=='L') {
//        for (int i = 0; i < n; i++) {
//            for (int j = 0; j < n; j++) {
//                if(matrix[i][j] != matrix[j][n-i-1]) {
//                    output.push_back(j);
//                    output.push_back(n - i - 1);
//                    output.push_back(i);
//                    output.push_back(j);
//                    matrix[j][n-i-1] = matrix[i][j];
//                }
//            }
//        }
//    } else {
//        for (int i = 0; i < n; i++) {
//            for (int j = 0; j < n; j++) {
//                if (matrix[i][j] != matrix[n-j-1][i]) {
//                    output.push_back(n - j - 1);
//                    output.push_back(i);
//                    output.push_back(i);
//                    output.push_back(j);
//                    matrix[n-j-1][i] = matrix[i][j];
//                }
//            }
//        }
//    }
//    cout << output.size()/4 << endl;
//    for (int i = 0; i < output.size(); i = i + 4) {
//        cout << output[i] << ' ' << output[i+1] << ' ' << output[i+2] << ' '<< output[i+3] << endl;
//    }
//    return 0;
//}
