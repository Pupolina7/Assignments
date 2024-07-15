#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Point {
    int x, y, steps;
    bool knight;
};

int main() {
    int n;
    cin >> n;

    vector<vector<char>> board(n, vector<char>(n));
    int startX, startY, endX, endY;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> board[i][j];
            if (board[i][j] == 'S') {
                startX = i;
                startY = j;
            } else if (board[i][j] == 'F') {
                endX = i;
                endY = j;
            }
        }
    }
    vector<pair<int, int>> knightMoves = {
            {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2},
            {1, -2}, {2, -1}, {2, 1}, {1, 2}
    };
    vector<pair<int, int>> kingMoves = {
            {-1, -1}, {-1, 0}, {-1, 1},
            {0, -1},           {0, 1},
            {1, -1}, {1, 0}, {1, 1}
    };
    queue<Point> q;
    q.push({startX, startY, 0, true});
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    while (!q.empty()) {
        Point current = q.front();
        q.pop();
        if (current.x == endX && current.y == endY) {
            cout << current.steps + 1;
            return 0;
        }
        if (current.knight){
            for (auto &move: knightMoves) {
                int newX = current.x + move.first;
                int newY = current.y + move.second;

                if (newX >= 0 && newX < n && newY >= 0 && newY < n &&
                    !visited[newX][newY]) {
                    visited[newX][newY] = true;
                    if (board[newX][newY] != 'G') {
                        q.push({newX, newY, current.steps + 1, false});
                    } else {
                        q.push({newX, newY, current.steps + 1, true});
                    }
                }
            }
        }
        vector<pair<int, int>> moves = current.knight ? knightMoves : kingMoves;

        for (auto& move : moves) {
            int newX = current.x + move.first;
            int newY = current.y + move.second;

            if (newX >= 0 && newX < n && newY >= 0 && newY < n &&
                !visited[newX][newY]) {
                visited[newX][newY] = true;
                if (board[newX][newY] != 'G') {
                    q.push({newX, newY, current.steps + 1, false});
                } else {
                    q.push({newX, newY, current.steps + 1, true});
                }
            }
        }
    }
    cout << -1;
    return 0;
}