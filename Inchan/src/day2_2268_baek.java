import java.io.*;
import java.util.*;

public class day2_2268_baek {
    static int N, M, S;
    static long[] tree;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        S = 1;
        while(S < N) {
            S *= 2;
        }
        tree = new long[S * 2];
        arr = new int[N + 1];

        for (int i = 0; i < M; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st2.nextToken());
            int a = Integer.parseInt(st2.nextToken());
            int b = Integer.parseInt(st2.nextToken());
            if(type == 0) { // sum
                if(a > b) {
                    int temp = a;
                    a = b;
                    b = temp;
                }
                sb.append(query(1, S, 1, a, b)).append("\n");
            }
            else { // modify
                long diff = b - tree[S + a - 1];
                update(1, S, 1, a, diff);
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static long query(int left, int right, int node, int queryLeft, int queryRight) {
        if (left > queryRight || right < queryLeft) return 0;
        if(left >= queryLeft && right <= queryRight) {
            return tree[node];
        }
        int mid = (left + right) / 2;
        return query(left, mid, 2 * node, queryLeft, queryRight) + query(mid + 1, right, 2 * node + 1, queryLeft, queryRight);
    }

    static void update(int left, int right, int node,  int target, long diff) {
        if(target >= left && target <= right) {
            tree[node] += diff;
            if(2*node < tree.length) {
                int mid = (left + right) / 2;
                update(left, mid, 2*node, target, diff);
                update(mid + 1, right, 2 * node + 1, target, diff);
            }
        }
    }
}
