/*
input :
5
...XO
..XOO
...XO
O....
OXX..

output:
.B.XO
..XOO
..BXO
O....
OXX..
*/

#include <iostream>
#include <string>
using namespace std;

// 전역변수
int N;
string line;
char board[2005][2005];
bool bomb_spots[2005][2005];

// 함수
bool erase_bomb_spot(int r, int c, char direction){
    int c_cpy = c;
    int r_cpy = r;
    switch (direction){
        case 'r':
            while (true) {
                c++;
                if (c == N) {
                    for (int j = c_cpy + 1; j < c; j++) bomb_spots[r][j] = false;
                    return true;
                }
                if (board[r][c] == 'O' || board[r][c] == 'X'){
                    for (int j = c_cpy + 1; j < c; j++) bomb_spots[r][j] = false;
                    return true;
                }
            }
        case 'd':
            while (true) {
                r++;
                if (r == N){
                    for (int i = r_cpy + 1; i < r; i++) bomb_spots[i][c] = false;
                    return true;
                }
                if (board[r][c] == 'O' || board[r][c] == 'X'){
                    for (int i = r_cpy + 1; i < r; i++) bomb_spots[i][c] = false;
                    return true;
                }
            }
        case 'l':
            while (true) {
                c--;
                if (c == -1) {
                    for (int j = c_cpy - 1; j > c; j--) bomb_spots[r][j] = false;
                    return true;
                }
                if (board[r][c] == 'O' || board[r][c] == 'X'){
                    for (int j = c_cpy - 1; j > c; j--) bomb_spots[r][j] = false;
                    return true;
                }
            }
        case 'u':
            while (true) {
                r--;
                if (r == -1){
                    for (int i = r_cpy - 1; i > r; i--) bomb_spots[i][c] = false;
                    return true;
                }
                if (board[r][c] == 'O' || board[r][c] == 'X'){
                    for (int i = r_cpy - 1; i > r; i--) bomb_spots[i][c] = false;
                    return true;
                }
            }
    }
}


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> line;
        for (int j = 0; j < N; j++){
            board[i][j] = line[j];
        }
    }

    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            if (board[i][j] == '.'){
                bomb_spots[i][j] = true;
            }
        }
    }

    for (int r = 0; r < N; r++){
        for (int c = 0; c < N; c++){
            if (board[r][c] == 'O'){
                erase_bomb_spot(r, c, 'r');
                erase_bomb_spot(r, c, 'd');
                erase_bomb_spot(r, c, 'l');
                erase_bomb_spot(r, c, 'u');
            }
        }
    }

    // print out
    for (int r = 0; r < N; r++){
        for (int c = 0; c < N; c++){
            if (bomb_spots[r][c]) cout << 'B';
            else cout << board[r][c];
        }
        cout << '\n';
    }
    return 0;
}