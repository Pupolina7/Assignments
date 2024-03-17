#include <bits/stdc++.h>
using namespace std;
#define Size 9
//structure representing the state of the map
struct mapCharacteristics {
    int perceptionScenario; //1 or 2
    bool capitanMarvel = false;
};
/*function that fills save cells in the visibility zones of Thanos with 0s*/
void fillFreeCellsChecked(vector<vector<int>> &map, int perceptionScenario, int x, int y) {
    for(int i = x-1; i<=x+1; i++) {
        for(int j = y-1; j<=y+1; j++) {
            if(i>=0 && i<Size && j>=0 && j<Size) {
                if (map[i][j]==-1) {
                    map[i][j] = 0;//free cell to visit next
                }
            }
        }
    }
    if(perceptionScenario == 2) {
        if(x-2>=0 && y-2>=0) {
            if(map[x-2][y-2]==-1) {
                map[x-2][y-2] = 0;//free cell to visit next
            }
        }
        if(x-2>=0 && y+2<Size) {
            if(map[x-2][y+2]==-1) {
                map[x-2][y+2] = 0;//free cell to visit next
            }
        }
        if(x+2<Size && y-2>=0) {
            if(map[x+2][y-2]==-1) {
                map[x+2][y-2] = 0;//free cell to visit next
            }
        }
        if(x+2<Size && y+2<Size) {
            if(map[x+2][y+2]==-1) {
                map[x+2][y+2] = 0;//free cell to visit next
            }
        }
    }
}
/*function that performs data scanning and fills the map with corresponding values
1 represents perception zone that can be visited with shield
5 represents cells blocked to visit in any case
6 represents unchecked perception zones
10 indicates shield
100 indicates infinity stone*/
void scanData(vector<vector<int>> &map, struct mapCharacteristics &mapCharacteristics, int x, int y) {
    int n;
    cin>>n;
    if(n!=0) {
        for (int k=0; k<n; k++) {
            int coordX, coordY;
            char item;
            cin>>coordX>>coordY>>item;
            if(coordY<0 || coordY>=Size || coordX<0 || coordX>=Size) {
                cout<<"e -1"<<endl;
                exit(0);
            }
            switch (item) {
                case 'P':
                    if(mapCharacteristics.capitanMarvel) {
                        if(map[coordX][coordY]==6 || map[coordX][coordY]== -1 || map[coordX][coordY] == 0) {
                        }
                    }
                    else if(map[coordX][coordY]==5) {
                        cout<<"e -1"<<endl;
                        exit(0);
                    }
                    else {
                        map[coordX][coordY] = 6;
                    }
                    break;
                case 'H':
                    map[coordX][coordY] = 5;
                    if (coordY + 1 < Size) {
                        if (map[coordX][coordY + 1] == -1
                            || map[coordX][coordY + 1] == 0 || map[coordX][coordY + 1] == 6
                                ) {
                            if(mapCharacteristics.capitanMarvel) {
                                map[coordX][coordY + 1] = 1;
                            } else {
                                map[coordX][coordY + 1] = 6;
                            }
                        }
                    }
                    if (coordY - 1 >= 0) {
                        if (map[coordX][coordY - 1] == -1
                            || map[coordX][coordY - 1] == 0 || map[coordX][coordY - 1] == 6
                                ) {
                            if(mapCharacteristics.capitanMarvel) {
                                map[coordX][coordY - 1] = 1;
                            } else {
                                map[coordX][coordY - 1] = 6;
                            }
                        }
                    }
                    if (coordX + 1 < Size) {
                        if (map[coordX + 1][coordY] == -1
                            || map[coordX + 1][coordY] == 0 || map[coordX + 1][coordY] == 6
                                ) {
                            if (mapCharacteristics.capitanMarvel) {
                                map[coordX + 1][coordY] = 1;
                            } else {
                                map[coordX + 1][coordY] = 6;
                            }
                        }
                    }
                    if (coordX - 1 >= 0) {
                        if (map[coordX - 1][coordY] == -1
                            || map[coordX - 1][coordY] == 0 || map[coordX - 1][coordY] == 6
                                ) {
                            if(mapCharacteristics.capitanMarvel) {
                                map[coordX - 1][coordY] = 1;
                            } else {
                                map[coordX - 1][coordY] = 6;
                            }
                        }
                    }
                    break;
                case 'T':
                    for (int i = coordX - 1; i <= coordX + 1; i++) {
                        for (int j = coordY - 1; j <= coordY + 1; j++) {
                            if (i >= 0 && i < Size && j >= 0 && j < Size) {
                                if (map[i][j] == -1
                                    || map[i][j] == 0 || map[i][j]==6
                                        ) {
                                    if(mapCharacteristics.capitanMarvel) {
                                        map[i][j]=1;
                                    } else {
                                        map[i][j] = 6;
                                    }
                                }
                            }
                        }
                    }
                    map[coordX][coordY] = 5;
                    break;
                case 'M':
                    for (int i = coordX - 1; i <= coordX + 1; i++) {
                        for (int j = coordY - 1; j <= coordY + 1; j++) {
                            if (i >= 0 && i < Size && j >= 0 && j < Size) {
                                    map[i][j] = 5;
                            }
                        }
                    }
                    map[coordX][coordY] =5;
                    if (coordX - 2 >= 0) {
                            map[coordX - 2][coordY] = 5;
                    }
                    if (coordY + 2 < Size) {
                            map[coordX][coordY + 2] = 5;
                    }
                    if (coordX + 2 < Size) {
                            map[coordX + 2][coordY] = 5;
                    }
                    if (coordY - 2 >= 0) {
                            map[coordX][coordY - 2] = 5;
                    }
                    for(int i=0; i<Size; i++) {
                        for(int j=0; j<Size; j++) {
                            if(map[i][j]==6) {
                                map[i][j]=1;
                            }
                        }
                    }
                    mapCharacteristics.capitanMarvel = true;
                    break;
                case 'S':
                    if(map[coordX][coordY] == -1 || map[coordX][coordY] == 0 || map[coordX][coordY] == 10) {
                        map[coordX][coordY] = 10; //shield position
                    } else {
                        cout<<"e -1"<<endl;
                        exit(0);
                    }
                    break;
                case 'I':
                    if(map[coordX][coordY] == -1 || map[coordX][coordY] == 0 || map[coordX][coordY] == 100) {
                        map[coordX][coordY] = 100; //infinity stone on the map
                    } else {
                        cout<<"e -1"<<endl;
                        exit(0);
                    }
                    break;
                default:
                    cout<<"e -1"<<endl;
                    exit(0);
            }
        }
    }
    fillFreeCellsChecked(map, mapCharacteristics.perceptionScenario, x, y);
}
/*structure that stores all needed data for each cell on the map*/
struct cell {
    int parent_x, parent_y;
    // f = g + h
    //indicates if the shield was included into the shortest path to the current cell
    bool shield = false;
    double f, h;
    int g;
};
typedef pair<double, pair<int, int> > pPair;
/*check on satisfactory with map size*/
bool isValid(int x, int y) {
    return x >= 0 && x < Size && y >= 0 && y < Size;
}
/*check on satisfactory with the conditions on safe move*/
bool isSafe(vector<vector<int>>& map, int x, int y,cell cellCharacteristics) {
    return isValid(x, y) && (map[x][y]==0 || map[x][y]==10 || map[x][y]==100
           || (cellCharacteristics.shield && map[x][y] == 1));
}
/*check if the current coordinate is infinity stone*/
bool isDestination(int x, int y, int destX, int destY) {
    return x == destX && y == destY;
}
/*function to calculate H for each cell*/
double calculateH(int x, int y, int destX, int destY) {
    return sqrt(pow(x - destX, 2) + pow(y - destY, 2));
}
/*function that moves the Thanos sequentially from the current cell to the next
it moves just to parent
scanning data is performed but not on the used map*/
void move(cell cells[Size][Size], int x, int y, int destX, int destY,
          vector<vector<int>>& map, mapCharacteristics& mapCharacteristics) {
    vector<vector<int>> mapNew(Size, vector<int>(Size));
    for (int i=0; i<Size; i++){
        for(int j=0; j<Size; j++){
            mapNew[i][j] = -1;//unchecked cells by default
        }
    }
    struct mapCharacteristics mapCharacteristicsNew;
    mapCharacteristicsNew.perceptionScenario = 1;
    if(isDestination(x, y, destX, destY)) {
        cout<<"m "<<x<<" "<<y<<endl;
        scanData(map, mapCharacteristics, x, y);
        return;
    }
    cell cellStart = cells[x][y];
    cout<<"m "<<x<<" "<<y<<endl;
    scanData(map, mapCharacteristics, x, y);//
    cout<<"m "<<cellStart.parent_x<<" "<<cellStart.parent_y<<endl;
    scanData(mapNew, mapCharacteristicsNew, 8, 8);
    while(cellStart.parent_x != 0 && cellStart.parent_y!=0) {
        cellStart = cells[cellStart.parent_x][cellStart.parent_y];
        cout<<"m "<<cellStart.parent_x<<" "<<cellStart.parent_y<<endl;
        scanData(mapNew, mapCharacteristicsNew, x, y);
    }
        vector<string> out;
        cellStart = cells[destX][destY];
        string add = "m " + to_string(destX) + " " + to_string(destY);
        out.push_back(add);
        add = "m " + to_string(cellStart.parent_x) + " " + to_string(cellStart.parent_y);
        out.push_back(add);
        while (cellStart.parent_x != 0 && cellStart.parent_y != 0) {
            cellStart = cells[cellStart.parent_x][cellStart.parent_y];
            add = "m " + to_string(cellStart.parent_x) + " " + to_string(cellStart.parent_y);
            out.push_back(add);
        }
        for (int i = out.size() - 1; i > 0; i--) {
            cout << out[i] << endl;
            scanData(mapNew, mapCharacteristicsNew, x, y);
        }
    cout << out[0] << endl;
    scanData(map, mapCharacteristics, destX, destY);
}
/*function that sorts the list of cells possible to visit next by f and then by h
it returns the element with the shortest f and h*/
pPair sortByFH(vector<pPair>& openList, cell cells[Size][Size]){
    sort(openList.begin(), openList.end());
    double minF = openList[0].first;
    double minH = FLT_MAX;
    pPair out;
    for(int i=0; i<openList.size(); i++) {
        if(openList[i].first == minF) {
            if(cells[openList[i].second.first][openList[i].second.second].h<minH) {
                minH = cells[openList[i].second.first][openList[i].second.second].h;
                out = openList[i];
            }
        }
        else {
            break;
        }
    }
    return out;
};
/*A* algorithm*/
int aStar(vector<vector<int>> &map, int x, int y, int destX, int destY, struct mapCharacteristics& mapCharacteristics) {
    //default data filling
    bool closedList[Size][Size];
    for(auto & i : closedList) {
        for(bool & j : i) {
            j = false;
        }
    }
    cell cells[Size][Size];
    for (auto & cell : cells) {
        for (auto & j : cell) {
            j.f = FLT_MAX;
            j.g = INT_MAX;
            j.h = FLT_MAX;
            j.parent_x = -1;
            j.parent_y = -1;
        }
    }
    //filling the data for the first cell
    cells[x][y].f = 0;
    cells[x][y].g = 0;
    cells[x][y].h = calculateH(0, 0, destX, destY);
    cells[x][y].parent_x = x;
    cells[x][y].parent_y = y;
    vector <pPair> openList;
    openList.push_back(make_pair(0.0, make_pair(x, y)));
    bool found = false;
    int prevX = x, prevY = y;
    while (!openList.empty()) {
        pPair p = sortByFH(openList, cells);
        for(int i = 0; i<openList.size(); i++) {
            if(openList[i].first==p.first) {
                if(openList[i].second.first==p.second.first) {
                    if(openList[i].second.second==p.second.second) {
                        openList.erase(openList.begin()+i);
                    }
                }
            } else {
                break;
            }
        }
        closedList[p.second.first][p.second.second] = true;
        x = p.second.first;
        y = p.second.second;
        double hNew, fNew;
        int gNew;
        move(cells, prevX, prevY, x, y, map, mapCharacteristics);
        if (isValid(x - 1, y)) {
            if (isDestination(x - 1, y, destX, destY)) {
                cells[x - 1][y].parent_x = x;
                cells[x - 1][y].parent_y = y;
                found = true;
                return cells[x][y].g + 1;
            }
            if (isSafe(map, x - 1, y,cells[x][y])) {
                cout<<"m "<<x-1<<" "<<y<<endl;
                scanData(map, mapCharacteristics, x-1, y);
                gNew = cells[x][y].g + 1;
                hNew = calculateH(x - 1, y, destX, destY);
                fNew = gNew + hNew;
                if (cells[x - 1][y].f == FLT_MAX || cells[x - 1][y].f >= fNew) {
                    bool prevShield = false;
                    if (cells[x - 1][y].f == fNew) {
                        prevShield = cells[x-1][y].shield;
                    }
                    openList.push_back(make_pair(fNew, make_pair(x - 1, y)));
                    cells[x - 1][y].f = fNew;
                    cells[x - 1][y].g = gNew;
                    cells[x - 1][y].h = hNew;
                    cells[x - 1][y].parent_x = x;
                    cells[x - 1][y].parent_y = y;
                    cells[x-1][y].shield = cells[x][y].shield || prevShield;
                    if(map[x-1][y]==10) {
                        cells[x-1][y].shield = true;
                    }
                }
            }
            cout<<"m "<<x<<" "<<y<<endl;
            scanData(map, mapCharacteristics, x, y);
        }
        if (isValid(x + 1, y)) {
            if (isDestination(x + 1, y, destX, destY)) {
                cells[x + 1][y].parent_x = x;
                cells[x + 1][y].parent_y = y;
                found = true;
                return cells[x][y].g + 1;
            }
            if (isSafe(map, x + 1, y,cells[x][y])) {
                cout<<"m "<<x+1<<" "<<y<<endl;
                scanData(map, mapCharacteristics, x+1, y);
                gNew = cells[x][y].g + 1;
                hNew = calculateH(x + 1, y, destX, destY);
                fNew = gNew + hNew;
                if (cells[x + 1][y].f == FLT_MAX || cells[x + 1][y].f >= fNew) {
                    bool prevShield = false;
                    if (cells[x + 1][y].f == fNew) {
                        prevShield = cells[x+1][y].shield;
                    }
                    openList.push_back(make_pair(fNew, make_pair(x + 1, y)));
                    cells[x + 1][y].f = fNew;
                    cells[x + 1][y].g = gNew;
                    cells[x + 1][y].h = hNew;
                    cells[x + 1][y].parent_x = x;
                    cells[x + 1][y].parent_y = y;
                    cells[x+1][y].shield = cells[x][y].shield || prevShield;
                    if(map[x+1][y]==10) {
                        cells[x+1][y].shield = true;
                    }
                }
            }
            cout<<"m "<<x<<" "<<y<<endl;
            scanData(map, mapCharacteristics, x, y);
        }
        if (isValid(x, y + 1)) {
            if (isDestination(x, y + 1, destX, destY)) {
                cells[x][y + 1].parent_x = x;
                cells[x][y + 1].parent_y = y;
                found = true;
                return cells[x][y].g + 1;
            }
            if (isSafe(map, x, y + 1,cells[x][y])) {
                cout<<"m "<<x<<" "<<y+1<<endl;
                scanData(map, mapCharacteristics, x, y+1);
                gNew = cells[x][y].g + 1;
                hNew = calculateH(x, y + 1, destX, destY);
                fNew = gNew + hNew;
                if (cells[x][y + 1].f == FLT_MAX || cells[x][y + 1].f >= fNew) {
                    bool prevShield = false;
                    if (cells[x][y + 1].f == fNew) {
                        prevShield = cells[x][y+1].shield;
                    }
                    openList.push_back(make_pair(fNew, make_pair(x, y + 1)));
                    cells[x][y + 1].f = fNew;
                    cells[x][y + 1].g = gNew;
                    cells[x][y + 1].h = hNew;
                    cells[x][y + 1].parent_x = x;
                    cells[x][y + 1].parent_y = y;
                    cells[x][y + 1].shield = cells[x][y].shield || prevShield;
                    if(map[x][y + 1]==10) {
                        cells[x][y + 1].shield = true;
                    }
                }
            }
            cout<<"m "<<x<<" "<<y<<endl;
            scanData(map, mapCharacteristics, x, y);
        }
        if (isValid(x, y - 1)) {
            if (isDestination(x, y - 1, destX, destY)) {
                cells[x][y - 1].parent_x = x;
                cells[x][y - 1].parent_y = y;
                found = true;
                return cells[x][y].g + 1;
            }
            if (isSafe(map, x, y - 1,cells[x][y])) {
                cout<<"m "<<x<<" "<<y-1<<endl;
                scanData(map, mapCharacteristics, x, y-1);
                gNew = cells[x][y].g + 1;
                hNew = calculateH(x, y - 1, destX, destY);
                fNew = gNew + hNew;
                if (cells[x][y - 1].f == FLT_MAX ||
                        cells[x][y - 1].f >= fNew) {
                    bool prevShield = false;
                    if (cells[x][y - 1].f == fNew) {
                        prevShield = cells[x][y-1].shield;
                    }
                    openList.push_back(make_pair(fNew, make_pair(x, y - 1)));
                    cells[x][y - 1].f = fNew;
                    cells[x][y - 1].g = gNew;
                    cells[x][y - 1].h = hNew;
                    cells[x][y - 1].parent_x = x;
                    cells[x][y - 1].parent_y = y;
                    cells[x][y - 1].shield = cells[x][y].shield || prevShield;
                    if(map[x][y - 1]==10) {
                        cells[x][y - 1].shield = true;
                    }
                }
            }
            cout<<"m "<<x<<" "<<y<<endl;
            scanData(map, mapCharacteristics, x, y);
        }
        cout<<"m "<<x<<" "<<y<<endl;
        scanData(map, mapCharacteristics, x, y);
        prevX = x;
        prevY = y;
    }
    //-1 in case of absence of a path
    if(!found) {
        return -1;
    }
}
int main() {
    struct mapCharacteristics mapCharacteristics{};
    cin>>mapCharacteristics.perceptionScenario;
    int x, y;
    cin>>x>>y;//coordinates of infinity stone
    vector<vector<int>> map(Size, vector<int>(Size));
    //0 means that the cell if safe for the next move
    for (int i=0; i<Size; i++){
        for(int j=0; j<Size; j++){
            map[i][j] = -1;//unchecked cells by default
        }
    }
    //the first move is always the same
    cout<<"m 0 0"<<endl;
    scanData(map, mapCharacteristics, 0, 0);
    int path = aStar(map, 0, 0, x, y, mapCharacteristics);
    cout<<"e "<<path<<endl;
    return 0;
}
