import java.io.*;
import java.util.*;

public class day19_2688_baek {
    static long[][] dp;
    static int T;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int n = Integer.parseInt(br.readLine());
            long sum = 0;
            dp = new long[n + 1][10];
            Arrays.fill(dp[1], 1);
            for (int i = 2; i <= n; i++) {
                for (int j = 0; j < 10; j++) {
                    for (int k = 0; k <= j; k++) {
                        dp[i][j] += dp[i - 1][k];
                    }
                }
            }
            for (int i = 0; i < 10; i++) {
                sum += dp[n][i];
            }
            sb.append(sum).append("\n");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
