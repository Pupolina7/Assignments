#include <iostream>
#include <vector>
#define Size 9
//https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/
using namespace std;
struct mapCharacteristics {
    int perceptionScenario; //1 or 2
    bool shield = false;
};
void scanData(vector<vector<int>> &map, struct mapCharacteristics &mapCharacteristics, int x, int y) {
    int n;
    cin>>n;
    if(n==0) {
        if(mapCharacteristics.perceptionScenario == 1) {
            for(int i = x-1; i<x+1; i++) {
                for(int j=y-1; j<y+1; j++) {
                    if(x>0 && x<Size && y>0 && y<Size) {
                        map[i][j] = 0;//free cell to visit next
                    }
                }
            }
        } else if(mapCharacteristics.perceptionScenario == 2) {
            for(int i = x-1; i<x+1; i++) {
                for(int j=y-1; j<y+1; j++) {
                    if(x>0 && x<Size && y>0 && y<Size) {
                        map[i][j]=0; //free cell to visit next
                    }
                }
            }
            if(x-2>0 && y-2>0) {
                map[x-2][y-2]=0;//free cell to visit next
            }
            if(x-2>0 && y+2<Size) {
                map[x-2][y+2]=0;//free cell to visit next
            }
            if(x+2<Size && y-2>0) {
                map[x+2][y-2]=0;//free cell to visit next
            }
            if(x+2<Size && y+2<Size) {
                map[x+2][y+2]=0;//free cell to visit next
            }
        }
    } else {
        for (int i=0; i<n; i++) {
            int coordX, coordY;
            char item;
            cin>>coordX>>coordY>>item;
            switch (item) {
                case 'P':
                    map[coordX][coordY]=1; //perception zone, dangerous without shield
                    break;
                case 'H':
                    map[coordX][coordY]=2; //enemy whose perception zone is limited by shield
                    break;
                case 'T':
                    map[coordX][coordY]=2; //enemy whose perception zone is limited by shield
                    break;
                case 'M':
                    map[coordX][coordY]=3; //enemy whose perception zone is not limited by shield
                    break;
                case 'S':
                    mapCharacteristics.shield = true;
                    break;
                case 'I':
                    map[coordX][coordY] = 100; //infinity stone on the map
                    break;
            }
        }
    }
}
bool isSafe(const vector<vector<int>>& map, const vector<vector<bool>>& isVisited, int x, int y) {
    return x>=0 && y>=0 && x<Size && y<Size && !isVisited[x][y] && map[x][y]==0;
}

void findShortestPath(vector<vector<int>> &map, vector<vector<bool>> &isVisited,
                      int posX, int posY, int destX, int destY, int &min_dist, int dist,
                      struct mapCharacteristics& mapCharacteristics){
    if (posX == destX && posY == destY){
        min_dist = min(dist, min_dist);
        return;
    }
    isVisited[posX][posY] = true;
    if (isSafe(map, isVisited, posX + 1, posY)) {
        cout<<"m "<<posX+1<<" "<<posY;
        scanData(map, mapCharacteristics, posX+1, posY);
        findShortestPath(map, isVisited, posX + 1, posY, destX, destY, min_dist, dist + 1, mapCharacteristics);
    }
    if (isSafe(map, isVisited, posX, posY + 1)) {
        cout<<"m "<<posX<<" "<<posY + 1;
        scanData(map, mapCharacteristics, posX, posY+1);
        findShortestPath(map, isVisited, posX, posY + 1, destX, destY, min_dist, dist + 1, mapCharacteristics);
    }
    if (isSafe(map, isVisited, posX - 1, posY)) {
        cout<<"m "<<posX-1<<" "<<posY;
        scanData(map, mapCharacteristics, posX-1, posY);
        findShortestPath(map, isVisited, posX - 1, posY, destX, destY, min_dist, dist + 1, mapCharacteristics);
    }
    if (isSafe(map, isVisited, posX, posY - 1)) {
        cout<<"m "<<posX<<" "<<posY-1;
        scanData(map, mapCharacteristics, posX, posY-1);
        findShortestPath(map, isVisited, posX, posY - 1, destX, destY, min_dist, dist + 1, mapCharacteristics);
    }
    isVisited[posX][posY] = false;
}

int findShortestLength(vector<vector<int>> &map, int curX, int curY, int destX, int destY, struct mapCharacteristics &mapCharacteristics){
    if (map.empty() || map[curX][curY] != 0 || map[destX][destY] == 0) {
        return -1;
    }
    vector<vector<bool>> isVisited (Size, vector<bool>(Size));
    int dist = INT_MAX;
    findShortestPath(map, isVisited, curX, curY, destX, destY,dist, 0, mapCharacteristics);
    if (dist != INT_MAX)
        return dist;
    return -1;
}

int main() {
    struct mapCharacteristics mapCharacteristics{};
    cin>>mapCharacteristics.perceptionScenario;
    int x, y;
    bool found = false;
    cin>>x>>y;
    int pathLength = INT_MAX;
    vector<vector<int>> map(Size, vector<int>(Size));
    //0 means that the cell if safe for the next move
    vector<vector<bool>> isVisited(Size, vector<bool>(Size));
    for (int i=0; i<Size; i++){
        for(int j=0; j<Size; j++){
            map[i][j] = -1;//unchecked cells by default
            isVisited[i][j] = false;
        }
    }
    map[x][y] = 100;//infinity stone is here
    cout<<"m 0 0";

    if(pathLength == INT_MAX) {
        cout<<"e -1";
        return 0;
    }
    cout<<"e "<<pathLength;
    return 0;
}
