import java.io.*;
import java.util.*;

public class day14_7578_baek {
    static int[] num, factory;
    static long[] tree;
    static int N, S;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());

        num = new int[1000001];
        S = 1;
        while (S < N) {
            S *= 2;
        }
        tree = new long[S * 2];
        factory = new int[N + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            int n = Integer.parseInt(st.nextToken());
            num[n] = i; // 인덱스 저장
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            int n = Integer.parseInt(st.nextToken());
            factory[i] = num[n]; // 2번째 배열에는 첫번째 배열에서의 인덱스를 저장
        }
        long ans = 0;
        for (int i = 1; i <= N; i++) {
            int now = factory[i];
            ans += query(1, S, 1, now + 1, S);

            update(1, S, 1, now, 1);
        }
        bw.write(ans + "\n");
        bw.flush();
        bw.close();
    }

    static long query(int left, int right, int node, int qLeft, int qRight) {
        if (left > qRight || right < qLeft) {
            return 0;
        }
        if (left >= qLeft && right <= qRight) {
            return tree[node];
        }
        int mid = (left + right) / 2;
        return query(left, mid, 2 * node, qLeft, qRight) + query(mid + 1, right, 2 * node + 1, qLeft, qRight);
    }

    static void update(int left, int right, int node, int target, int diff) {
        if(target >= left && target <= right) {
            tree[node] += diff;
            if (2 * node < tree.length) {
                int mid = (left + right) / 2;
                update(left, mid, 2 * node, target, diff);
                update(mid + 1, right, 2 * node + 1, target, diff);
            }

        }
    }
}
