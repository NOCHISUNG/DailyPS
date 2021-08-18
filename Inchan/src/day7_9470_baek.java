import java.io.*;
import java.util.*;

public class day7_9470_baek {
    static int T, K, M, P;
    static HCNode[] nodes;
    static Queue<Integer> q;
    static int[] strahler;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            StringTokenizer initialST = new StringTokenizer(br.readLine());
            K = Integer.parseInt(initialST.nextToken());
            M = Integer.parseInt(initialST.nextToken());
            P = Integer.parseInt(initialST.nextToken());
            nodes = new HCNode[M + 1];
            strahler = new int[M + 1];
            q = new LinkedList<>();
            for (int i = 1; i <= M; i++) {
                nodes[i] = new HCNode(i);
            }
            for (int i = 0; i < P; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int A = Integer.parseInt(st.nextToken());
                int B = Integer.parseInt(st.nextToken());
                nodes[A].outDegree++;
                nodes[A].out.add(B);
                nodes[B].inDegree++;
                nodes[B].in.add(A);
            }
            for (int i = 1; i <= M; i++) {
                if(nodes[i].inDegree == 0) {
                    q.add(i);
                    strahler[i] = 1;
                }
            }

            while (!q.isEmpty()) {
                int now = q.remove();

                for (int i : nodes[now].in) {
                    int add;
                    if(nodes[now].map.containsKey(strahler[i])) {
                        add = nodes[now].map.get(strahler[i]) + 1;
                    }
                    else {
                        add = 1;
                    }
                    nodes[now].map.put(strahler[i], add);
                }

                if(nodes[now].in.size() != 0) {
                    Object[] array = nodes[now].map.keySet().toArray();
                    int max = nodes[now].map.get((int) array[0]);
                    if(max == 1){
                        strahler[now] = (int) array[0];
                    }
                    else if(max >= 2) {
                        strahler[now] = (int) array[0] + 1;
                    }
                }

                for (int i : nodes[now].out) {
                    nodes[i].inDegree--;
                    nodes[now].outDegree--;
                    if(nodes[i].inDegree == 0) q.add(i);
                }
            }

            sb.append(t + 1).append(" ").append(strahler[M]).append("\n");

        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }
}

class HCNode {
    int outDegree, inDegree;
    List<Integer> out, in;
    int id;
    Map<Integer, Integer> map;

    HCNode(int id) {
        this.id = id;
        this.in = new ArrayList<>();
        this.out = new ArrayList<>();
        this.outDegree = 0;
        this.inDegree = 0;
        this.map = new TreeMap<>(Comparator.reverseOrder());
    }
}