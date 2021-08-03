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
void erase_bomb_spot(int r, int c, char direction){
    switch (direction){
        case 'r':
            for (int j = c + 1; j < N; j++){
                if (board[r][j] == 'O' || board[r][j] == 'X') return;
                bomb_spots[r][j] = false;
            }
            break;
        case 'd':
            for (int i = r + 1; i < N; i++){
                if (board[i][c] == 'O' || board[i][c] == 'X') return;
                bomb_spots[i][c] = false;
            }
            break;
        case 'l':
            for (int j = c - 1; j >= 0; j--){
                if (board[r][j] == 'O' || board[r][j] == 'X') return;
                bomb_spots[r][j] = false;
            }
            break;
        case 'u':
            for (int i = r - 1; i >= 0; i--){
                if (board[i][c] == 'O' || board[i][c] == 'X') return;
                bomb_spots[i][c] = false;
            }
            break;
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