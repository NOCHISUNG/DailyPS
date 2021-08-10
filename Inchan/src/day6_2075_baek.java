import java.io.*;
import java.util.*;

public class day6_2075_baek {
    static PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                pq.add(Integer.valueOf(st.nextToken()));
            }
        }
        for (int i = 0; i < N-1; i++) {
            pq.remove();
        }
        bw.write(pq.remove() + "\n");
        bw.flush();
        bw.close();
    }
}
