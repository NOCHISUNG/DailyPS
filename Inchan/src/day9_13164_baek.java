import java.io.*;
import java.util.*;

public class day9_13164_baek {
    static int[] height, diff;
    static int N, K;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer init = new StringTokenizer(br.readLine());
        N = Integer.parseInt(init.nextToken());
        K = Integer.parseInt(init.nextToken());
        StringTokenizer st = new StringTokenizer(br.readLine());
        height = new int[N];
        diff = new int[N - 1];
        for (int i = 0; i < N; i++) {
            height[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < N - 1; i++) {
            diff[i] = height[i + 1] - height[i];
        }

        Arrays.sort(diff);
        int answer = 0;
        for (int i = 0; i < N - K; i++) {
            answer += diff[i];
        }
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
    }
}
