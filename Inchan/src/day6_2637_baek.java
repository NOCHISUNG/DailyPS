import java.io.*;
import java.util.*;

public class day6_2637_baek {
    static int N, M;
    static Node[] nodes;
    static Queue<Integer> q = new LinkedList<>();
    static List<Integer> basics = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        nodes = new Node[N + 1];
        for (int i = 1; i <= N; i++) {
            nodes[i] = new Node(N);
        }
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int X = Integer.parseInt(st.nextToken());
            int Y = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            nodes[X].sub.put(Y, K);
            nodes[X].add(Y);
            nodes[Y].to[X] = true;
        }
        for (int i = 1; i <= N; i++) {
            if(nodes[i].fromCount==0) {
                basics.add(i);
            }
        }
        for (int i : basics) { // 기본 부품들 제거
            for (int j = 1; j <= N; j++) {
                if(nodes[i].to[j]) {
                    nodes[j].from[i] = false;
                    nodes[j].fromCount--;
                    if(nodes[j].fromCount == 0) q.add(j);
                }
            }
        }
        while(!q.isEmpty()) {
            int now = q.remove(); // 5 나옴
            if(now == N) break;
            for (int i = 1; i <= N; i++) {
                if(nodes[now].to[i]) {
                    for (int basic : nodes[now].sub.keySet()) {
                        if(nodes[i].sub.containsKey(basic)) {
                            int add = nodes[i].sub.get(basic) + (nodes[i].sub.get(now) * nodes[now].sub.get(basic));
                            nodes[i].sub.put(basic, add);
                        }
                        else {
                            int add = nodes[i].sub.get(now) * nodes[now].sub.get(basic);
                            nodes[i].sub.put(basic, add);
                        }
                    }
                    nodes[i].sub.remove(now);
                    nodes[i].from[now] = false;
                    nodes[i].fromCount--;
                    if(nodes[i].fromCount == 0) q.add(i);
                }
            }
        }
        for (int a : nodes[N].sub.keySet()) {
            sb.append(a).append(" ").append(nodes[N].sub.get(a)).append("\n");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

}
class Node {
    Map<Integer, Integer> sub;
    boolean[] from, to;
    int fromCount;
    Node(int N) {
        fromCount = 0;
        sub = new TreeMap<>();
        from = new boolean[N + 1];
        to = new boolean[N + 1];
    }
    public void add(int from) {
        this.from[from] = true;
        fromCount++;
    }
}
