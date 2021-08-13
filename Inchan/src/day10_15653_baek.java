import java.io.*;
import java.util.*;

public class day10_15653_baek {
    // 상 하 좌 우
    static final int[] mx = {0, 0, -1, 1};
    static final int[] my = {-1, 1, 0, 0};
    static char[][] map;
    static int N, M, min = Integer.MAX_VALUE;
    static boolean[] visited = new boolean[4];
    static Position red, blue, goal;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new char[N][M];
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = s.charAt(j);
                if (map[i][j] == 'R') {
                    red = new Position(i, j);
                } else if (map[i][j] == 'B') {
                    blue = new Position(i, j);
                } else if (map[i][j] == 'O') {
                    goal = new Position(i, j);
                }
            }
        }
        backtracking(-1, 0);

        if (min == Integer.MAX_VALUE) {
            min = -1;
        }
        bw.write(min + "\n");
        bw.flush();
        bw.close();
    }
    static void backtracking(int now, int count) { // direction : 0,1,2,3 상 하 좌 우

        int ret;
        for (int i = now+1; i < 4; i++) {
//            if(visited[i]) continue;
            int RtempI = red.i;
            int RtempJ = red.j;
            int BtempI = blue.i;
            int BtempJ = blue.j;
            ret = moveWrapper(i);
            if(ret == 1) {
                min = Math.min(count + 1, min);
                return;
            }
            if(ret == -1) {
                backtracking(i, count);
            }
            else{
                backtracking(i, count + 1);
            }
            red.i = RtempI;
            red.j = RtempJ;
            blue.i = BtempI;
            blue.j = BtempJ;
        }
    }
    static int move(boolean isRed, int direction) { // return : 0 - completed, 1 - red goes to goal, 2 - blue goes to goal, -1 - cannot go(wall)
        if(isRed) {
            if (red.i == goal.i && red.j == goal.j) {
                return 1;
            }
            int ty = red.i + my[direction];
            int tx = red.j + mx[direction];
            if(ty >= 0 && ty < N && tx >= 0 && tx < M) {
                if(map[ty][tx] != '#') {
                    red.i = ty;
                    red.j = tx;
                }
                else {
                    return -1;
                }
            }
        }
        else {
            if (blue.i == goal.i && blue.j == goal.j) {
                return 2;
            }
            int ty = blue.i + my[direction];
            int tx = blue.j + mx[direction];
            if(ty >= 0 && ty < N && tx >= 0 && tx < M) {
                if(map[ty][tx] != '#') {
                    blue.i = ty;
                    blue.j = tx;
                }
                else {
                    return -1;
                }
            }
        }
        return move(isRed, direction);
    }
    // return 2 - FAIL : blue goes to goal, 1 - SUCCESS : red goes to goal, 0 - DONE : move complete, -1 - DIDN'T MOVE : both wall
    static int moveWrapper (int direction) {
        int retR, retB;
        switch (direction) {
            case 0: // 상 : 파랑이 빨강보다 위에 있으면 파랑먼저
                if(blue.i < red.i) {
                    retB = move(false, direction);
                    retR = move(true, direction);
                }
                else {
                    retR = move(true, direction);
                    retB = move(false, direction);
                }
                break;
            case 1: // 하 : 파랑이 빨강보다 아래 있으면 파랑먼저
                if (blue.i > red.i) {
                    retB = move(false, direction);
                    retR = move(true, direction);
                }
                else {
                    retR = move(true, direction);
                    retB = move(false, direction);
                }
                break;
            case 2: // 좌 : 파랑이 빨강보다 왼쪽에 있으면 파랑먼저
                if(blue.j < red.j) {
                    retB = move(false, direction);
                    retR = move(true, direction);
                }
                else {
                    retR = move(true, direction);
                    retB = move(false, direction);
                }
                break;
            case 3: // 우 : 파랑이 빨강보다 오른쪽에 있으면 파랑먼저
                if(blue.j > red.j) {
                    retB = move(false, direction);
                    retR = move(true, direction);
                }
                else {
                    retR = move(true, direction);
                    retB = move(false, direction);
                }
                break;
            default:
                retB = -1;
                retR = -1;
                break;
        }
        // 파랑이 구멍
        if(retB == 2) {
            return 2;
        }
        else if(retR == 1) {
            return 1;
        }
        else if(retR == -1 && retB == -1) {
            return -1;
        }
        else {
            return 0;
        }
    }
}

class Position{
    int i, j;

    public Position(int i, int j) {
        this.i = i;
        this.j = j;
    }
}