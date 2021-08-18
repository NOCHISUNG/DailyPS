import java.io.*;
import java.util.*;

public class day8_4781_baek {
    static int N;
    static int M;
    static int[] c;
    static int[] p;
    static int[] dp; // dp[p] 돈 한도가 p일 때 최대 이익
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        while(true) {
            StringTokenizer initial = new StringTokenizer(br.readLine());
            N = Integer.parseInt(initial.nextToken());
            double a = Double.parseDouble(initial.nextToken());
            M = (int) (a * 100);
            if(N == 0 && M == 0.00) break;
            c = new int[N];
            p = new int[N];
            dp = new int[M+1];
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                c[i] = Integer.parseInt(st.nextToken());
                p[i] = (int)(Double.parseDouble(st.nextToken()) * 100 + 0.5);
            }
            for (int i = 1; i <= M; i++) {
                int max = -1;
                for (int j = 0; j < N; j++) {
                    if(p[j] > i) { // 선택할 수 없음
                        max = Math.max(dp[i - 1], max);
                    } else { // 선택할 수 있음 -> 어떤 거 선택할거야?
                        max = Math.max(max, dp[i - p[j]] + c[j]);
                    }
                }
                dp[i] = max;
            }
            sb.append(dp[M]).append("\n");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
