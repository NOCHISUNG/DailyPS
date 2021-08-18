import java.io.*;
import java.util.*;

public class day9_12837_baek {
    static int N, Q, S;
    static long[] tree;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer initial = new StringTokenizer(br.readLine());
        N = Integer.parseInt(initial.nextToken());
        Q = Integer.parseInt(initial.nextToken());
        S = 1;
        while(S < N) {
            S *= 2;
        }
        tree = new long[S * 2];

        for (int i = 0; i < Q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());

            if(type == 1) {
                update(1, S, 1, p, q);
            }
            else {
                long ret = query(1, S, 1, p, q);
                sb.append(ret).append("\n");
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }
    static long query(int left, int right, int node, int qLeft, int qRight) {
        // 관계 없음
        if (left > qRight || right < qLeft) return 0;
        if(left >= qLeft && right <= qRight) return tree[node];

        int mid = (left + right) / 2;
        return query(left, mid, 2 * node, qLeft, qRight) + query(mid + 1, right, 2 * node + 1, qLeft, qRight);
    }

    static void update(int left, int right, int node, int target, int diff) {
        if(left <= target && target <= right) {
            tree[node] += diff;
            if(2*node < tree.length) {
                int mid = (left + right) / 2;
                update(left, mid, 2*node, target, diff);
                update(mid + 1, right, 2 * node + 1, target, diff);
            }
        }
    }
}
