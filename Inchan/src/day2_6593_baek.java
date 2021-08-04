import java.io.*;
import java.util.*;

public class day2_6593_baek {
    static int L,R, C;
    static char[][][] building;
    static boolean[][][] visited;
    static Queue<Kan> q;
    // 동 서 남 북 상 하
    static final int[] mx = {1, -1, 0, 0, 0, 0};
    static final int[] my = {0, 0, 1, -1, 0, 0};
    static final int[] mz = {1, -1};

    static Kan dest;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        while(true) {
            StringTokenizer  st = new StringTokenizer(br.readLine());
            L = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            if(L == 0 && R == 0 && C == 0) break;

            building = new char[L][R][C];
            visited = new boolean[L][R][C];
            q = new LinkedList<>();
            int added = 0, temp = 0;
            for (int i = 0; i < L; i++) {
                for (int j = 0; j < R; j++) {
                    String s = br.readLine();
                    for (int k = 0; k < C; k++) {
                        building[i][j][k] = s.charAt(k);
                        if(building[i][j][k] == 'S') {
                            q.add(new Kan(i, j, k));
                            visited[i][j][k] = true;
                            added++;
                        }
                        if(building[i][j][k] == 'E') dest = new Kan(i, j, k);
                    }
                }
                br.readLine();
            }
            int days = 0;
            boolean found = false;

            while (!q.isEmpty()) {
                for (int t = 0; t < added; t++) {
                    Kan next = q.remove();
                    // 1. 체크인
                    // 2. 목적지인가?
                    if(next.floor == dest.floor && next.row == dest.row && next.col == dest.col) {
                        found = true;
                        break;
                    }
                    // 3. 갈 수 있는 곳 순회
                    // 동 서 남 북
                    for (int i = 0; i < 4; i++) {
                        int ty = next.row + my[i];
                        int tx = next.col + mx[i];
                        // 4. 갈 수 있는가?
                        if(ty >= 0 && ty < R && tx >= 0 && tx < C) {
                            if(building[next.floor][ty][tx] != '#' && !visited[next.floor][ty][tx]) {
                                q.add(new Kan(next.floor, ty, tx));
                                visited[next.floor][ty][tx] = true;
                                temp++;
                            }
                        }
                    }
                    // 상 하
                    for (int i = 0; i < 2; i++) {
                        int tz = next.floor + mz[i];

                        if(tz >= 0 && tz < L) {
                            if(building[tz][next.row][next.col] != '#' && !visited[tz][next.row][next.col]) {
                                q.add(new Kan(tz, next.row, next.col));
                                visited[tz][next.row][next.col] = true;
                                temp++;
                            }
                        }
                    }
                }
                days++;
                if(found) break;
                added = temp;
                temp = 0;
            }
            days--;
            if(found) {
                bw.write("Escaped in " + days + " minute(s).\n");
            }
            else {
                bw.write("Trapped!\n");
            }
        }
        bw.flush();
        bw.close();
    }
}

class Kan {
    int floor;
    int row, col;

    Kan(int floor, int row, int col) {
        this.floor = floor;
        this.row = row;
        this.col = col;
    }
}