import java.io.*;
import java.util.*;

public class day4_1563_baek {
    static int[][][] dp;
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        dp = new int[N+1][4][4];
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j < 4; j++) {
                Arrays.fill(dp[i][j], -1);
            }
        }
        bw.write(getDP(0, 0, 0) + "\n");
        bw.flush();
        bw.close();
    }
    static int getDP(int day, int late, int abs) {
        if(late >= 2 || abs >= 3) { // 지각이 두번, 결석을 연속 세번 이상 한 경우
            return 0;
        }
        if(day == N) return 1;

        if(dp[day][late][abs] != -1) {
            return dp[day][late][abs];
        }

        return dp[day][late][abs] = (getDP(day + 1, late, 0) + getDP(day + 1, late + 1, 0) + getDP(day + 1, late, abs + 1)) % 1000000;
    }
}
