import java.io.*;
import java.util.*;
public class day4_2696_baek {
    static int T, midValue, M;

    // 1 2 3 4 5 6 7 8 9
    // minQ 3
    // maxQ 2
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            PriorityQueue<Integer> maxQ = new PriorityQueue<>(Comparator.reverseOrder()), minQ = new PriorityQueue<>();
            int count = 0;
            StringBuilder sb = new StringBuilder();
            M = Integer.parseInt(br.readLine());
            for (int j = 0; j < M / 10 + 1; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int bound = Math.min(M - j * 10, 10);
                for (int k = 1; k <= bound; k++) {
                    int a = Integer.parseInt(st.nextToken());
                    if(maxQ.size() == minQ.size() && maxQ.size() == 0) {
                        maxQ.add(a);
                    }
                    else if (maxQ.size() > minQ.size()) {
                        midValue = maxQ.peek();
                        if(a < midValue) {
                            maxQ.remove();
                            minQ.add(midValue);
                            maxQ.add(a);
                        }
                        else {
                            minQ.add(a);
                        }
                    }
                    else if(maxQ.size() == minQ.size()){
                        midValue = maxQ.peek();
                        if(a > midValue) {
                            minQ.add(a);
                            maxQ.add(minQ.remove());
                        }
                        else {
                            maxQ.add(a);
                        }
                    }

                    if(k % 2 == 1) {
                        sb.append(maxQ.peek()).append(" ");
                        count++;
                        if(count%10 == 0) {
                            sb.append("\n");
                        }
                    }
                }
            }
            bw.write(count + "\n");
            bw.write(sb.toString() + "\n");
        }
        bw.flush();
        bw.close();
    }
}
