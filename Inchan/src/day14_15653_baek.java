import java.io.*;
import java.util.*;
public class day14_15653_baek {
    static char[][] board;
    static int N, M;
    static boolean[][][][] visited;
    // 상 하 좌 우
    static int[] mx = {0, 0, -1, 1};
    static int[] my = {-1, 1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer init = new StringTokenizer(br.readLine());
        N = Integer.parseInt(init.nextToken());
        M = Integer.parseInt(init.nextToken());
        board = new char[N][M];
        visited = new boolean[N][M][N][M];
        int redI = 0, redJ = 0, blueI = 0, blueJ = 0;
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) {
                board[i][j] = s.charAt(j);
                if (board[i][j] == 'R') {
                    redI = i;
                    redJ = j;
                } else if (board[i][j] == 'B') {
                    blueI = i;
                    blueJ = j;
                }
            }
        }
        int ret = bfs(redI, redJ, blueI, blueJ);
        bw.write(ret + "\n");
        bw.flush();
        bw.close();
    }
    static int move(Position REDorBLUE, int dir) {
        int i = REDorBLUE.i;
        int j = REDorBLUE.j;
        int count = 0;
        while(board[i+my[dir]][j+mx[dir]] != '#' && board[i][j] != 'O') {
            i += my[dir];
            j += mx[dir];
            count++;
        }
        REDorBLUE.i = i;
        REDorBLUE.j = j;
        return count;
    }
    static int bfs(int redI, int redJ, int blueI, int blueJ) {
        // 움직일 수 있는 위치가 다음 가능한 노드들인 것 -> bfs
        Queue<Balls> q = new LinkedList<>();
        q.add(new Balls(new Position(redI, redJ), new Position(blueI, blueJ), 0));
        visited[redI][redJ][blueI][blueJ] = true;

        while(!q.isEmpty()) {
            Balls b = q.remove();
            int count = b.count;
            Position red = b.red;
            Position blue = b.blue;

            for (int i = 0; i < 4; i++) {
                Position tmpR = new Position(red.i, red.j);
                Position tmpB = new Position(blue.i, blue.j);
                int redM = move(tmpR, i);
                int blueM = move(tmpB, i);
                if(board[tmpB.i][tmpB.j] == 'O') {
                    continue;
                }
                if (board[tmpR.i][tmpR.j] == 'O') {
                    return count + 1;
                }
                if(tmpR.i == tmpB.i && tmpR.j == tmpB.j) {
                    if(redM > blueM) {
                        tmpR.i -= my[i];
                        tmpR.j -= mx[i];
                    }
                    else {
                        tmpB.i -= my[i];
                        tmpB.j -= mx[i];
                    }
                }
                if(!visited[tmpR.i][tmpR.j][tmpB.i][tmpB.j]) {
                    visited[tmpR.i][tmpR.j][tmpB.i][tmpB.j] = true;
                    q.add(new Balls(tmpR, tmpB, count + 1));
                }
            }
        }
        return -1;
    }
}

class Position {
    int i, j;

    public Position(int i, int j) {
        this.i = i;
        this.j = j;
    }
}

class Balls {
    Position red;
    Position blue;
    int count;

    public Balls(Position red, Position blue, int count) {
        this.red = red;
        this.blue = blue;
        this.count = count;
    }
}