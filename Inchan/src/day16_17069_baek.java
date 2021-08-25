import java.io.*;
import java.util.*;

public class day16_17069_baek {
    static long[][][] dp; // dp[dir][i][j] : dir 방향으로 놓인 파이프가 i,j 에 도착하는 방법의 수
    static int N;
    static int[][] map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        map = new int[N + 2][N + 2];
        dp = new long[3][N + 2][N + 2];
        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // dp[0][i][j] : 가로 방향으로 i,j에 도달하는 경우의 수 -> dp[0][i][j+1] += (dp[0][i][j] + dp[2][i][j])
        // dp[1][i][j] : 세로 방향으로 I,j에 도달하는 경우의 수 -> dp[1][i+1][j] += (dp[1][i][j] + dp[2][i][j])
        // dp[2][i][j] : 대각선 방향으로 i,j에 도달하는 경우의 수 -> dp[2][i+1][j+1] += (dp[0][i][j] + dp[1][i][j] + dp[2][i][j])
        dp[0][1][2] =  1; // 초기 상태

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if(map[i][j+1] == 0) dp[0][i][j+1] += (dp[0][i][j] + dp[2][i][j]);
                if(map[i+1][j] == 0) dp[1][i+1][j] += (dp[1][i][j] + dp[2][i][j]);
                if(map[i+1][j+1] == 0 && map[i+1][j] == 0 && map[i][j+1] == 0) dp[2][i+1][j+1] += (dp[0][i][j] + dp[1][i][j] + dp[2][i][j]);
            }
        }
        bw.write(dp[0][N][N] + dp[1][N][N] + dp[2][N][N] + "\n");
        bw.flush();
        bw.close();
    }
}
