import java.io.*;
import java.util.*;

public class day15_9328_baek {
    static boolean[] keys;
    static int T, W, H;
    static char[][] map;
    static Queue<Pos> q;
    static List[] doors;
    static boolean[][] visited;
    // 상 하 좌 우
    static int[] mx = {0, 0, -1, 1};
    static int[] my = {-1, 1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            H = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            keys = new boolean[26];
            visited = new boolean[H][W];
            map = new char[H][W];
            q = new LinkedList<>();
            doors = new List[26];
            for (int i = 0; i < 26; i++) {
                doors[i] = new ArrayList<Pos>();
            }
            int docCount = 0;
            for (int i = 0; i < H; i++) {
                String s = br.readLine();
                for (int j = 0; j < W; j++) {
                    map[i][j] = s.charAt(j);
                    if (i == 0 || i == H - 1) {
                        if(map[i][j] == '.') {
                            q.add(new Pos(i, j));
                            visited[i][j] = true;
                        }
                        // 가장자리에 키가 있을 경우
                        if(map[i][j] >= 'a' && map[i][j] <= 'z') {
                            q.add(new Pos(i, j));
                            visited[i][j] = true;
                            keys[map[i][j] - 'a'] = true;
                        }
                        // 가장자리에 문서가
                        if(map[i][j] == '$') {
                            q.add(new Pos(i, j));
                            visited[i][j] = true;
                            docCount++;
                        }
                    }
                }
                if (i != 0 && i != H - 1) {
                    if (map[i][0] == '.') {
                        q.add(new Pos(i, 0));
                        visited[i][0] = true;
                    }
                    if (map[i][W - 1] == '.') {
                        q.add(new Pos(i, W - 1));
                        visited[i][W - 1] = true;
                    }
                    if (map[i][0] == '$') {
                        q.add(new Pos(i, 0));
                        visited[i][0] = true;
                        docCount++;
                    }
                    if (map[i][W - 1] == '$') {
                        q.add(new Pos(i, W - 1));
                        visited[i][W - 1] = true;
                        docCount++;
                    }
                    if (map[i][0] >= 'a' && map[i][0] <= 'z') {
                        q.add(new Pos(i, 0));
                        visited[i][0] = true;
                        keys[map[i][0] - 'a'] = true;
                    }
                    if (map[i][W - 1] >= 'a' && map[i][W - 1] <= 'z') {
                        q.add(new Pos(i, W - 1));
                        visited[i][W - 1] = true;
                        keys[map[i][W - 1] - 'a'] = true;
                    }
                }
            }
            // 주어진 키 정보 설정
            String s = br.readLine();
            if(s.charAt(0) != '0') {
                int len = s.length();
                for (int i = 0; i < len; i++) {
                    keys[s.charAt(i) - 'a'] = true;
                }
            }
            checkDoors();

            while(!q.isEmpty()) {
                Pos cur = q.remove();

                for (int i = 0; i < 4; i++) {
                    int ty = cur.i + my[i];
                    int tx = cur.j + mx[i];

                    if(ty >= 0 && ty < H  && tx >= 0 && tx < W && !visited[ty][tx]) {
                        // . 일 때
                        if(map[ty][tx] == '.') {
                            q.add(new Pos(ty, tx));
                            visited[ty][tx] = true;
                        }
                        // 문서일 때
                        if(map[ty][tx] == '$') {
                            q.add(new Pos(ty, tx));
                            visited[ty][tx] = true;
                            docCount++;
                        }
                        // 문일 때
                        if (map[ty][tx] >= 'A' && map[ty][tx] <= 'Z') {
                            if(keys[map[ty][tx]-'A']) {
                                q.add(new Pos(ty, tx));
                                visited[ty][tx] = true;
                            }
                            else doors[map[ty][tx] - 'A'].add(new Pos(ty, tx));
                        }
                        // 열쇠일 때
                        if(map[ty][tx] >= 'a' && map[ty][tx] <= 'z') {
                            keys[map[ty][tx] - 'a'] = true;
                            q.add(new Pos(ty, tx));
                            visited[ty][tx] = true;
                            if (doors[map[ty][tx] - 'a'].size() != 0) {
                                int size = doors[map[ty][tx] - 'a'].size();
                                for (int j = 0; j < size; j++) {
                                    Pos p = (Pos) doors[map[ty][tx] - 'a'].get(j);
                                    q.add(p);
                                    visited[p.i][p.j] = true;
                                }
                            }
                        }
                    }
                }

            }
            sb.append(docCount).append("\n");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
    static void checkDoors() {
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (i == 0 || i == H - 1) {
                    // 가장자리에 문이 있을 경우
                    if(map[i][j] >= 'A' && map[i][j] <= 'Z') {
                        if (keys[map[i][j] - 'A']) {
                            q.add(new Pos(i, j));
                            visited[i][j] = true;
                        }
                        else doors[map[i][j] - 'A'].add(new Pos(i, j));
                    }

                }
            }
            if (i != 0 && i != H - 1) {
                if (map[i][0] >= 'A' && map[i][0] <= 'Z') {
                    if (keys[map[i][0] - 'A']) {
                        q.add(new Pos(i, 0));
                        visited[i][0] = true;
                    }
                    else doors[map[i][0] - 'A'].add(new Pos(i, 0));
                }
                if (map[i][W - 1] >= 'A' && map[i][W - 1] <= 'Z') {
                    if (keys[map[i][W - 1] - 'A']) {
                        q.add(new Pos(i, W - 1));
                        visited[i][W - 1] = true;
                    } else {
                        doors[map[i][W - 1] - 'A'].add(new Pos(i, W - 1));
                    }
                }
            }
        }
    }
}
class Pos {
    int i, j;

    public Pos(int i, int j) {
        this.i = i;
        this.j = j;
    }
}
