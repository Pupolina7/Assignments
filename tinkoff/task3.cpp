#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> to_words(string s) {
    vector<string> words;
    int idx = 0;
    while ((idx = s.find('/')) != -1){
        words.push_back(s.substr(0, idx));
        s.erase(0, idx+1);
    }
    words.push_back(s);
    return words;
}

int main() {
    int n;
    cin >> n;
    string root;
    vector<vector<string>> directories;
    vector<string> words;
    for (int i = 0; i < n; i++) {
        string input;
        cin >> input;
        directories.push_back(to_words(input));
        root = directories[i][0];
        directories[i][0] = "/";
    }
    sort(directories.begin(), directories.end());
    for (int i = 0; i < directories.size(); i++) {
        for (int j = 0; j < directories[i].size() - 1; j++) {
            cout << "  ";
        }
        string out = directories[i].back();
        if (out == "/") {
            cout << root << endl;
        } else {
            cout << out << endl;
        }
    }
    return 0;
}