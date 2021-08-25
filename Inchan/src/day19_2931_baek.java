import java.io.*;
import java.util.*;

public class day19_2931_baek {
    static char[][] map;
    static int R, C;
    static P M, Z, start;
    static P needToFill = new P(-1, -1);
    static char forWhat;
    static boolean[][] visited;
    // 상 하 좌 우 
    static int[] mx = {0, 0, -1, 1};
    static int[] my = {-1, 1, 0, 0};
    static Queue<P> q = new LinkedList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        map = new char[R + 1][C + 1];
        visited = new boolean[R + 1][C + 1];
        for (int i = 1; i <= R; i++) {
            String s = br.readLine();
            for (int j = 1; j <= C; j++) {
                map[i][j] = s.charAt(j - 1);
                if(map[i][j] == 'M') {
                    M = new P(i, j);
                    start = new P(i, j);
                    visited[M.i][M.j] = true;
                    q.add(M);
                }else if(map[i][j] =='Z') {
                    Z = new P(i, j);
                }
            }
        }
        P cur = q.remove();
        for (int i = 0; i < 4; i++) {
            int ty = cur.i + my[i];
            int tx = cur.j + mx[i];
            if(ty > 0 && ty <= R && tx > 0 && tx <= C) {
                if(map[ty][tx] != '.' && map[ty][tx] != 'Z') {
                    q.add(new P(ty, tx));
                    visited[ty][tx] = true;
                    break;
                }
            }
        }
        if(q.isEmpty()) {
            visited[Z.i][Z.j] = true;
            start.i = Z.i;
            start.j = Z.j;
            for (int i = 0; i < 4; i++) {
                int ty = Z.i + my[i];
                int tx = Z.j + mx[i];
                if(ty > 0 && ty <= R && tx > 0 && tx <= C) {
                    if(map[ty][tx] != '.' && map[ty][tx] != 'M') {
                        visited[ty][tx] = true;
                        q.add(new P(ty, tx));
                        break;
                    }
                }
            }
        }
        while(!q.isEmpty()) {
            cur = q.remove();
            int ty = 0;
            int tx = 0;
            boolean find = false, end = false;
            switch(map[cur.i][cur.j]){
                case '-':
                    for (int i = 0; i < 4; i++) {
                        if(i == 0 || i == 1) continue;
                        ty = cur.i + my[i];
                        tx = cur.j + mx[i];
                        if(ty > 0 && ty <= R && tx > 0 && tx <= C) {
                            if(!visited[ty][tx]) {
                                if(map[ty][tx] == '.'){
                                    find = true;
                                    needToFill = new P(ty, tx);
                                    q.add(needToFill);
                                }
                                else {
                                    q.add(new P(ty, tx));
                                    visited[ty][tx] = true;
                                }
                                break;
                            }
                        }
                    }
                    break;
                case '|':
                    for (int i = 0; i < 4; i++) {
                        if(i == 2 || i == 3) continue;
                        ty = cur.i + my[i];
                        tx = cur.j + mx[i];
                        if(ty > 0 && ty <= R && tx > 0 && tx <= C) {
                            if(!visited[ty][tx]) {
                                if(map[ty][tx] == '.'){
                                    find = true;
                                    needToFill = new P(ty, tx);
                                    q.add(needToFill);
                                }
                                else {
                                    q.add(new P(ty, tx));
                                    visited[ty][tx] = true;
                                }
                                break;
                            }
                        }
                    }
                    break;
                case '+':
                    for (int i = 0; i < 4; i++) {
                        ty = cur.i + my[i];
                        tx = cur.j + mx[i];
                        if(ty > 0 && ty <= R && tx > 0 && tx <= C) {
                            if(!visited[ty][tx]) {
                                if(map[ty][tx] == '.'){
                                    find = true;
                                    needToFill = new P(ty, tx);
                                    q.add(needToFill);
                                }
                                else {
                                    q.add(new P(ty, tx));
                                    visited[ty][tx] = true;
                                }
                            }
                        }
                    }
                    break;
                case '1':
                    for (int i = 0; i < 4; i++) {
                        if(i == 0 || i == 2) continue;
                        ty = cur.i + my[i];
                        tx = cur.j + mx[i];
                        if(ty > 0 && ty <= R && tx > 0 && tx <= C) {
                            if(!visited[ty][tx]) {
                                if(map[ty][tx] == '.'){
                                    find = true;
                                    needToFill = new P(ty, tx);
                                    q.add(needToFill);
                                }
                                else {
                                    q.add(new P(ty, tx));
                                    visited[ty][tx] = true;
                                }
                                break;
                            }
                        }
                    }
                    break;
                case '2':
                    for (int i = 0; i < 4; i++) {
                        if(i == 1 || i == 2) continue;
                        ty = cur.i + my[i];
                        tx = cur.j + mx[i];
                        if(ty > 0 && ty <= R && tx > 0 && tx <= C) {
                            if(!visited[ty][tx]) {
                                if(map[ty][tx] == '.'){
                                    find = true;
                                    needToFill = new P(ty, tx);
                                    q.add(needToFill);
                                }
                                else {
                                    q.add(new P(ty, tx));
                                    visited[ty][tx] = true;
                                }
                                break;
                            }
                        }
                    }
                    break;
                case '3':
                    for (int i = 0; i < 4; i++) {
                        if(i == 1 || i == 3) continue;
                        ty = cur.i + my[i];
                        tx = cur.j + mx[i];
                        if(ty > 0 && ty <= R && tx > 0 && tx <= C) {
                            if(!visited[ty][tx]) {
                                if(map[ty][tx] == '.'){
                                    find = true;
                                    needToFill = new P(ty, tx);
                                    q.add(needToFill);
                                }
                                else {
                                    q.add(new P(ty, tx));
                                    visited[ty][tx] = true;
                                }
                                break;
                            }
                        }
                    }
                    break;
                case '4':
                    for (int i = 0; i < 4; i++) {
                        if(i == 0 || i == 3) continue;
                        ty = cur.i + my[i];
                        tx = cur.j + mx[i];
                        if(ty > 0 && ty <= R && tx > 0 && tx <= C) {
                            if(!visited[ty][tx]) {
                                if(map[ty][tx] == '.'){
                                    find = true;
                                    needToFill = new P(ty, tx);
                                    q.add(needToFill);
                                }
                                else {
                                    q.add(new P(ty, tx));
                                    visited[ty][tx] = true;
                                }
                                break;
                            }
                        }
                    }
                    break;
                case '.': // .
                    end = true;
                    boolean[] dir = {false, false, false, false};
                    int dirCount = 0;
                    for (int i = 0; i < 4; i++) {
                        ty = cur.i + my[i];
                        tx = cur.j + mx[i];
                        if(ty > 0 && ty <= R && tx > 0 && tx <= C) {
                            if(map[ty][tx] != '.') {
                                if(i == 0) {
                                    if(map[ty][tx] == '|' || map[ty][tx] == '+' || map[ty][tx] == '1' || map[ty][tx] =='4') {
                                        dir[i] = true;
                                        dirCount++;
                                    }
                                }
                                if(i == 1) {
                                    if(map[ty][tx] == '|' || map[ty][tx] == '+' || map[ty][tx] == '2' || map[ty][tx] =='3') {
                                        dir[i] = true;
                                        dirCount++;
                                    }
                                }
                                if (i == 2) {
                                    if (map[ty][tx] == '-' || map[ty][tx] == '+' || map[ty][tx] == '1' || map[ty][tx] == '2') {
                                        dir[i] = true;
                                        dirCount++;
                                    }
                                }
                                if (i == 3) {
                                    if (map[ty][tx] == '-' || map[ty][tx] == '+' || map[ty][tx] == '3' || map[ty][tx] == '4') {
                                        dir[i] = true;
                                        dirCount++;
                                    }
                                }
                            }
                        }
                    }

                    int targetI = Z.i;
                    int targetJ = Z.j;
                    if (start.i == Z.i && start.j == Z.j) {
                        targetI = M.i;
                        targetJ = M.j;
                    }
                    for (int i = 0; i < 4; i++) {
                        ty = cur.i + my[i];
                        tx = cur.j + mx[i];
                        if(ty > 0 && ty <= R && tx > 0 && tx <= C) {
                            if (ty == targetI && tx == targetJ) {
                                if(i == 0) {
                                    int tty = ty + 2;
                                    if(tty > 0 && ty <= R) {
                                        if (map[tty][tx] != map[start.i][start.j]) {
                                            dir[i] = true;
                                        }
                                    }
                                    else dir[i] = true;
                                }
                                if(i == 1) {
                                    int tty = ty - 2;
                                    if (tty > 0 && ty <= R) {
                                        if (map[tty][tx] != map[start.i][start.j]) {
                                            dir[i] = true;
                                        }
                                    }
                                    else dir[i] = true;
                                }
                                if (i == 2) {
                                    int ttx = tx + 2;
                                    if(ttx > 0 && tx <= C) {
                                        if (map[ty][ttx] != map[start.i][start.j]) {
                                            dir[i] = true;
                                        }
                                    }
                                    else dir[i] = true;
                                }
                                if (i == 3) {
                                    int ttx = tx - 2;
                                    if(ttx > 0 && tx <= C) {
                                        if (map[ty][ttx] != map[start.i][start.j]) {
                                            dir[i] = true;
                                        }
                                    }
                                    else dir[i] = true;
                                }
                            }
                        }
                    }

                    if(dir[0]) {
                        if(dir[1]) {
                            if(dir[2] && dir[3]) {
                                forWhat = '+';
                            } else forWhat = '|';
                        }
                        else if(dir[3]) {
                            forWhat = '2';
                        } else {
                            forWhat = '3';
                        }
                    }
                    else if (dir[1]) {
                        if(dir[3]) { // 하 우
                            forWhat = '1';
                        } else { // 하 좌
                            forWhat = '4';
                        }
                    } else if(dir[2]) {
                        if(dir[3]){
                            forWhat = '-';
                        }
                    }
                    break;
                default:
                    end = true;
                    break;
            }
            if(end) break;
        }
        bw.write(needToFill.i + " " + needToFill.j + " " + forWhat + "\n");
        bw.flush();
        bw.close();
    }
}
class P {
    int i, j;

    public P(int i, int j) {
        this.i = i;
        this.j = j;
    }
}
