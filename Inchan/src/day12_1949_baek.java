import java.io.*;
import java.util.*;

public class day12_1949_baek {
    static int N;
    static boolean[] visited;
    static int[][] dp;
    static int[] people;
    static List[] adj;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        dp = new int[N + 1][2];
        visited = new boolean[N + 1];
        people = new int[N + 1];
        adj = new List[N + 1];
        for (int i = 1; i <= N; i++) {
            adj[i] = new ArrayList<Integer>();
        }
        StringTokenizer init = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            people[i] = Integer.parseInt(init.nextToken());
        }
        for (int i = 0; i < N-1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adj[a].add(b);
            adj[b].add(a);
        }
        visited[1] = true;
        dfs(1);

        int ret = Math.max(dp[1][0], dp[1][1]);
        bw.write(ret + "\n");
        bw.flush();
        bw.close();
    }
    static void dfs(int node) {
        int len = adj[node].size();
        for (int i = 0; i < len; i++) {
            int next = (int) adj[node].get(i);
            if(visited[next]) continue;
            visited[next] = true;
            dfs(next);
            // dp
            dp[node][0] += dp[next][1];
            dp[node][1] += Math.max(dp[next][0], dp[next][1]);
        }
        dp[node][0] += people[node];
    }
}
