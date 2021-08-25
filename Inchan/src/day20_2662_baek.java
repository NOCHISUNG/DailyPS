import java.io.*;
import java.util.*;

public class day20_2662_baek {
    static int[][] dp; // dp[i][n] : 기업이 i개 있을 때 n원으로 얻을 수 있는 최대 이익
    static int[][] info; // info[i][j] : j원으로 i 기업에 투자했을 때 이익
    static int N, M; // N : 투자 금액, M : 기업 개수
    static int[][] memo; // memo[i][n] : n원 있을 떄 dp[i][n]이 최대일 때 i기업에 얼마 투자?
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        dp = new int[M + 1][N + 1];
        info = new int[M + 1][N + 1];
        memo = new int[M + 1][N + 1];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int j = 1;
            while(st.hasMoreTokens()) {
                int b = Integer.parseInt(st.nextToken());
                info[j++][a] = b;
            }
        }


        for (int i = 1; i <= M; i++) { // 모든 기업에 대해
            for (int c = 1; c <= N; c++) { // 모든 투자 금액
                // i 기업에 k 원만큼 쓸 때 이익
                for (int j = 0; j <= c; j++) {
                    int a = dp[i - 1][c - j] + info[i][j];
                    if (a > dp[i][c]) {
                        dp[i][c] = a;
                        memo[i][c] = j;
                    }
                }
            }
        }
        System.out.println(dp[M][N]);
        Stack<Integer> ans = new Stack<>();
        int cost = N;
        for (int i = M; i > 0; i--) {
            ans.push(memo[i][cost]);
            cost -= memo[i][cost];
        }
        while(!ans.isEmpty()) {
            sb.append(ans.pop()).append(" ");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
