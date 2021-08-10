import java.io.*;
import java.util.*;
public class day6_2957_baek {
    static int N;
    static long C = 0;
    static TreeSet<Integer> map = new TreeSet<>();
    static int[] depth;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        depth = new int[N + 2];
        depth[0] = -1;
        depth[N + 1] = -1;
        map.add((N + 1));
        map.add(0);
        for (int i = 0; i < N; i++) {
            int a = Integer.parseInt(br.readLine());
            depth[a] = Math.max(depth[map.higher(a)], depth[map.lower(a)]) + 1;
            map.add(a);
            C += depth[a];
            sb.append(C).append("\n");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}