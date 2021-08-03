import java.io.*;
import java.util.*;

public class day1_5676_baek {
    static int[] arr;
    static double[] tree;
    static int N,K, S;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        while(true) {
            try{
                StringTokenizer st = new StringTokenizer(br.readLine());
                N = Integer.parseInt(st.nextToken());
                K = Integer.parseInt(st.nextToken());
                S = 1;
                while(S < N) {
                    S *= 2;
                }
                arr = new int[N + 1];
                tree = new double[S * 2];
                StringTokenizer st2 = new StringTokenizer(br.readLine());
                for (int i = 1; i <= N; i++) {
                    arr[i] = Integer.parseInt(st2.nextToken());
                }
                initTree();
                for (int t = 0; t < K; t++) {
                    StringTokenizer st3 = new StringTokenizer(br.readLine());
                    char type = st3.nextToken().charAt(0);
                    int i = Integer.parseInt(st3.nextToken());
                    int j = Integer.parseInt(st3.nextToken());
                    if(type == 'C') {
                        if (tree[S + i - 1] == 0) {
                            updateIfZero(i, j);
                        }
                        else {
                            double diff = j / tree[S + i - 1];
                            update(1, S, 1, i, diff);
                        }
                    }
                    else {
                        double ret = query(1, S, 1, i, j);
                        if(ret < 0) {
                            sb.append("-");
                        } else if (ret > 0) {
                            sb.append("+");
                        } else {
                            sb.append("0");
                        }
                    }
                }
                sb.append("\n");
            } catch (Exception e) {
                break;
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
    static void initTree() {
        int n = 1;
        for (int i = S; i < S * 2; i++) {
            if(n > N) {
                tree[i] = 0;
            }
            else tree[i] = arr[n++];
        }
        for (int i = S - 1; i >= 1; i--) {
            tree[i] = tree[2 * i] * tree[2 * i + 1];
        }
    }
    static double query(int left, int right, int node, int queryLeft, int queryRight) {
        // 내 범위 밖
        if(left > queryRight || right < queryLeft) {
            return 1;
        }
        if(queryLeft <= left && queryRight >= right) {
            return tree[node];
        }
        int mid = (left + right) / 2;
        return query(left, mid, 2 * node, queryLeft, queryRight) * query(mid + 1, right, 2 * node + 1, queryLeft, queryRight);
    }

    static void update(int left, int right, int node, int target, double diff) {
        if(target >= left && target <= right) {
            tree[node] *= diff;
            if(2*node < tree.length) { // 자식이 있으면
                int mid = (left + right) / 2;
                update(left, mid, 2*node, target, diff);
                update(mid + 1, right, 2 * node + 1, target, diff);
            }
        }
    }
    static void updateIfZero(int target, int diff) {
        int i = S + target - 1;
        tree[i] += diff;
        i /= 2;
        while(i >= 1) {
            tree[i] = tree[2 * i] * tree[2 * i + 1];
            i /= 2;
        }
    }
}
