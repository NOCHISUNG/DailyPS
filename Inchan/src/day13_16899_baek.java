import java.io.*;
import java.util.*;

public class day13_16899_baek {
    static int N, M, checkCount = 0, max = -1;
    static int[][] board;
    // 상 하 좌 우
    static int[] mx = {0, 0, -1, 1};
    static int[] my = {-1, 1, 0, 0};
    static List<Coord> twos = new ArrayList<>(), zeros = new ArrayList<>();
    static boolean[][] visited, checked;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer init = new StringTokenizer(br.readLine());
        N = Integer.parseInt(init.nextToken());
        M = Integer.parseInt(init.nextToken());
        board = new int[N][M];
        visited = new boolean[N][M];
        checked = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if(board[i][j] == 2) {
                    twos.add(new Coord(i, j));
                }
                else if (board[i][j] == 0) {
                    zeros.add(new Coord(i, j));
                }
            }
        }
        int len = zeros.size();
        for (int i = 0; i < len - 1; i++) {
            for (int j = i + 1; j < len; j++) {
                Coord f = zeros.get(i);
                Coord s = zeros.get(j);
                board[f.i][f.j] = 1;
                board[s.i][s.j] = 1;
                count();
                board[f.i][f.j] = 0;
                board[s.i][s.j] = 0;
            }
        }
        if(max == -1) max = 0;
        bw.write(max + "\n");
        bw.flush();
        bw.close();
    }
    static boolean bfs(int i, int j) {
        Queue<Coord> q = new LinkedList<>();
        q.add(new Coord(i, j));
        checked[i][j] = true;
        checkCount++;
        boolean fail = false;
        while(!q.isEmpty()) {
            Coord cur = q.remove();

            for (int k = 0; k < 4; k++) {
                int ty = cur.i + my[k];
                int tx = cur.j + mx[k];
                if (ty >= 0 && ty < N && tx >= 0 && tx < M) {
                    if(!checked[ty][tx]) {
                        if(board[ty][tx] == 2) {
                            q.add(new Coord(ty, tx));
                            checked[ty][tx] = true;
                            checkCount++;
                        }
                        else if(board[ty][tx] == 0) {
                            fail = true;
                        }
                    }
                }
            }
        }
        if(fail) {
            checkCount = 0;
            return false;
        }
        return true;
    }
    static void count() {
        checked = new boolean[N][M];
        checkCount = 0;
        int com = 0;
        for (Coord coord : twos) {
            if(!checked[coord.i][coord.j]) {
                if (bfs(coord.i, coord.j)) {
                    com += checkCount;
                    checkCount = 0;
                }
            }
        }
        max = Math.max(com, max);
    }
}

class Coord {
    int i, j;

    public Coord(int i, int j) {
        this.i = i;
        this.j = j;
    }
}