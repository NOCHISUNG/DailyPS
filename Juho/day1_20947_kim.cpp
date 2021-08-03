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
bool chk[2005][2005];

// 함수
bool bomb_spot_chk(int r, int c, char direction){
    int c_cpy = c;
    int r_cpy = r;
    switch(direction){
        case 'r':
            while (true) {
                c++;
                if (c == N) {
                    for (int j = c_cpy + 1; j < c; j++) chk[r][j] = true;
                    return true;
                }
                if (board[r][c] == 'O') return false;
                if (board[r][c] == 'X'){
                    for (int j = c_cpy + 1; j < c; j++) chk[r][j] = true;
                    return true;
                }
            }
        case 'd':
            while (true) {
                r++;
                if (r == N){
                    for (int i = r_cpy + 1; i < r; i++) chk[i][c] = true;
                    return true;
                }
                if (board[r][c] == 'O') return false;
                if (board[r][c] == 'X'){
                    for (int i = r_cpy + 1; i < r; i++) chk[i][c] = true;
                    return true;
                }
            }
        case 'l':
            while (true) {
                c--;
                if (c == -1) {
                    for (int j = c_cpy - 1; j > c; j--) chk[r][j] = true;
                    return true;
                }
                if (board[r][c] == 'O') return false;
                if (board[r][c] == 'X'){
                    for (int j = c_cpy - 1; j > c; j--) chk[r][j] = true;
                    return true;
                }
            }
        case 'u':
            while (true) {
                r--;
                if (r == -1){
                    for (int i = r_cpy - 1; i > r; i--) chk[i][c] = true;
                    return true;
                }
                if (board[r][c] == 'O') return false;
                if (board[r][c] == 'X'){
                    for (int i = r_cpy - 1; i > r; i--) chk[i][c] = true;
                    return true;
                }
            }
    }
}

bool erase_bomb_spot(int r, int c, char direction){
    int c_cpy = c;
    int r_cpy = r;
    switch (direction){
        case 'r':
            while (true) {
                c++;
                if (c == N) {
                    for (int j = c_cpy + 1; j < c; j++) chk[r][j] = false;
                    return true;
                }
                if (board[r][c] == 'O' || board[r][c] == 'X'){
                    for (int j = c_cpy + 1; j < c; j++) chk[r][j] = false;
                    return true;
                }
            }
        case 'd':
            while (true) {
                r++;
                if (r == N){
                    for (int i = r_cpy + 1; i < r; i++) chk[i][c] = false;
                    return true;
                }
                if (board[r][c] == 'O' || board[r][c] == 'X'){
                    for (int i = r_cpy + 1; i < r; i++) chk[i][c] = false;
                    return true;
                }
            }
        case 'l':
            while (true) {
                c--;
                if (c == -1) {
                    for (int j = c_cpy - 1; j > c; j--) chk[r][j] = false;
                    return true;
                }
                if (board[r][c] == 'O' || board[r][c] == 'X'){
                    for (int j = c_cpy - 1; j > c; j--) chk[r][j] = false;
                    return true;
                }
            }
        case 'u':
            while (true) {
                r--;
                if (r == -1){
                    for (int i = r_cpy - 1; i > r; i--) chk[i][c] = false;
                    return true;
                }
                if (board[r][c] == 'O' || board[r][c] == 'X'){
                    for (int i = r_cpy - 1; i > r; i--) chk[i][c] = false;
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


    for (int r = 0; r < N; r++){
        for (int c = 0; c < N; c++){
            if (board[r][c] == 'X'){
                bomb_spot_chk(r, c, 'r');
                bomb_spot_chk(r, c, 'd');
                bomb_spot_chk(r, c, 'l');
                bomb_spot_chk(r, c, 'u');
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
            if (chk[r][c]) cout << 'B';
            else cout << board[r][c];
        }
        cout << '\n';
    }
    return 0;
}