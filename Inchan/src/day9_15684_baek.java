import java.io.*;
import java.util.*;

public class day9_15684_baek {
    static boolean[][][] ladder;
    static int N, M, H, base;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer initial = new StringTokenizer(br.readLine());
        N = Integer.parseInt(initial.nextToken());
        M = Integer.parseInt(initial.nextToken());
        H = Integer.parseInt(initial.nextToken());
        if(M == 0) {
            bw.write("0\n");
            bw.flush();
            bw.close();
            return;
        }

        ladder = new boolean[M + 1][N + 1][N + 1];
        base = 0;
        // ladder[a][b][b+1] - a 가로줄에서 b와 b+1 세로줄을 잇는 가로선이 있는가?
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            ladder[a][b][b + 1] = true;
            base++;
        }
        if(N == 2) {
            if (base % 2 == 1) {
                bw.write("1\n");
            }
            else {
                bw.write("0\n");
            }
            bw.flush();
            bw.close();
        }
    }
    static boolean promising(int a, int b) { // b : start
        if (b == 1) {
            return ladder[a][b + 1][b + 2];
        } else if (b == N - 1) {
            return ladder[a][b - 1][b];
        } else {
            return ladder[a][b - 1][b] && ladder[a][b + 1][b + 2];
        }
    }

    static void backtracking(int now, int count) {

    }
}
