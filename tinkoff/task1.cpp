#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector <int> marks(n);
    for (int i = 0; i < n; i++) {
        cin >> marks[i];
    }
    int number_excellent = -1;
    for (int i = 6; i < n; i++) {
        bool satisfy = true;
        int count = 0;
        for (int j = i - 6; j <= i; j++) {
            if (marks[j] == 2 || marks[j] == 3){
                satisfy = false;
                break;
            }
            if (marks[j] == 5) {
                count++;
            }
        }
        if (satisfy) {
            number_excellent = max(number_excellent, count);
        }
    }
    cout << number_excellent;
    return 0;
}
