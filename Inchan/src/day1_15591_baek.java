import java.io.*;
import java.util.*;

public class day1_15591_baek {
    static int[][] D;
    static int N, Q;
    static List[] adjlist;
    static Queue<Edge> q;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());
        adjlist = new List[N + 1];
        D = new int[N + 1][N + 1];
        for (int i = 1; i <= N; i++) {
            adjlist[i] = new ArrayList<Edge>();
            for (int j = 1; j <= N; j++) {
//                if(i == j) D[i][j] = 0;
                D[i][j] = Integer.MAX_VALUE;
            }
        }
        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st2.nextToken());
            int b = Integer.parseInt(st2.nextToken());
            int r = Integer.parseInt(st2.nextToken());
            adjlist[a].add(new Edge(a, b, r));
            adjlist[b].add(new Edge(b, a, r));
            D[a][b] = r;
            D[b][a] = r;
        }


        for (int i = 0; i < Q; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st2.nextToken());
            int v = Integer.parseInt(st2.nextToken());
            int count = 0;
            q = new LinkedList<>();
            for (int j = 0; j < adjlist[v].size(); j++) {
                q.add((Edge)adjlist[v].get(j));
            }
            visited = new boolean[N + 1];
            visited[v] = true;
            while (!q.isEmpty()) {
                Edge next = q.remove();
                visited[next.end] = true;
                for (int j = 0; j < adjlist[next.end].size(); j++) {
                    Edge e = (Edge) adjlist[next.end].get(j);
                    if(!visited[e.end]) {
                        D[v][e.end] = Math.min(D[v][next.end], e.cost);
                        q.add(e);
                    }
                }
            }
            for (int j = 1; j <= N; j++) {
                if(v == j || D[v][j] == Integer.MAX_VALUE) continue;
                if(D[v][j] >= k) count++;
            }
            sb.append(count).append("\n");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}

class Edge {
    int start;
    int end;
    int cost;
    Edge(int start, int end, int cost) {
        this.start = start;
        this.end = end;
        this.cost = cost;
    }
}
