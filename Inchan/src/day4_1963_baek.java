import java.io.*;
import java.util.*;

public class day4_1963_baek {
    static int T, start, end;
    static Queue<Integer> q;
    static boolean[] visited;
    static int[] days;
    static boolean[] isPrime = new boolean[10000];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        T = Integer.parseInt(br.readLine());
        Arrays.fill(isPrime, true);
        makePrime();
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            start = Integer.parseInt(st.nextToken());
            end = Integer.parseInt(st.nextToken());
            visited = new boolean[10000];
            days = new int[10000];
            q = new LinkedList<>();
            q.add(start);
            visited[start] = true;
            boolean find = false;
            while(!q.isEmpty()) {
                int now = q.remove();
                if(now == end) {
                    find = true;
                    break;
                }

                for (int j = 0; j < 4; j++) {
                    for (int k = 0; k <= 9; k++) {
                        if(j == 0 && k == 0) continue;

                        int next = change(now, j, k);

                        if(isPrime[next] && !visited[next]) {
                            visited[next] = true;
                            q.add(next);
                            days[next] = days[now] + 1;
                        }
                    }
                }
            }
            if(find) {
                sb.append(days[end]).append("\n");
            }
            else {
                sb.append("Impossible\n");
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
    static int change(int now, int digit, int TO) {
        StringBuilder sb = new StringBuilder();
        sb.append(now);
        sb.replace(digit, digit + 1, Integer.toString(TO));
        return Integer.parseInt(sb.toString());
    }

    static void makePrime() {
        for (int i = 2; i < 10000; i++) {
            if(isPrime[i]) {
                for (int j = i * 2; j < 10000; j += i) {
                    isPrime[j] = false;
                }
            }
        }
    }
}
