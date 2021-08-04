import java.io.*;
import java.util.*;

public class day2_17141_baek {
    static int N, M, twoCount = 0, min = Integer.MAX_VALUE, wallCount = 0;
    static int[][] map, daysMap;
    static boolean[] BacktrackingVisited;
    static boolean[][] visited;
    static List<VirusPoint> candidate = new ArrayList<>();
    static Queue<VirusPoint> q;
    // 동 서 남 북
    static final int[] mx = {1, -1, 0, 0};
    static final int[] my = {0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st2.nextToken());
                if(map[i][j] == 2) {
                    twoCount++;
                    candidate.add(new VirusPoint(i, j));
                }
                else if (map[i][j] == 1) {
                    wallCount++;
                }
            }
        }
        BacktrackingVisited = new boolean[twoCount];
        getCombination(0, 0);
        if(min == Integer.MAX_VALUE) {
            bw.write("-1\n");
        } else bw.write(min + "\n");
        bw.flush();
        bw.close();

    }
    static void getCombination(int n, int cnt) {
        if(cnt == M) {
            // 위치에 바이러스 놓고 bfs 실행해서 카운트 구하기
            daysMap = new int[N][N];
            buildMap();
            q = new LinkedList<>();
            visited = new boolean[N][N];
            int added = 0, temp = 0, viruses = 0;
            for (int i = 0; i < twoCount; i++) { // 바이러스 놓기
                if(BacktrackingVisited[i]) {
                    VirusPoint virusPoint = candidate.get(i);
                    q.add(virusPoint);
                    daysMap[virusPoint.row][virusPoint.col] = -1;
                    visited[virusPoint.row][virusPoint.col] = true;
                    added++;
                    viruses++;
                }
            }
            int days = 0;
            while (!q.isEmpty()) {
                for (int i = 0; i < added; i++) {
                    VirusPoint cur = q.remove();
                    // 1. 체크인
                    // 3. 갈 수 있는 곳 순회
                    for (int j = 0; j < 4; j++) {
                        int ty = cur.row + my[j];
                        int tx = cur.col + mx[j];
                        // 4. 갈 수 있는가?
                        if(ty >= 0 && ty < N && tx >= 0 && tx < N) {
                            if(daysMap[ty][tx] != -5 && !visited[ty][tx]) {
                                q.add(new VirusPoint(ty, tx));
                                daysMap[ty][tx] = days + 1;
                                visited[ty][tx] = true;
                                viruses++;
                                temp++;
                            }
                        }
                    }
                }
                added = temp;
                temp = 0;
                days++;
            }
            if (viruses + wallCount == N * N) {
                min = Math.min(min, days - 1);
            }
        }
        for (int i = n; i < twoCount; i++) {
            if(BacktrackingVisited[i]) continue;
            BacktrackingVisited[i] = true;
            getCombination(i, cnt + 1);
            BacktrackingVisited[i] = false;
        }
    }
    static void buildMap() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(map[i][j] == 1) { // 벽
                    daysMap[i][j] = -5;
                }
            }
        }
    }
}

class VirusPoint {
    int row, col;

    VirusPoint (int row, int col) {
        this.row = row;
        this.col = col;
    }
}
