import java.io.*;
import java.util.*;

public class day19_1365_baek {
    static int[] arr;
    static TreeSet<Integer> set = new TreeSet<>(), dpSet = new TreeSet<>();
    static int N, max = -1, maxIndex = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        arr = new int[N+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        set.add(arr[1]);
        for (int i = 2; i <= N; i++) {
            int last = set.last();
            if(arr[i] > last) {
                set.add(arr[i]);
            }
            else {
                set.remove(set.higher(arr[i]));
                set.add(arr[i]);
            }
        }
        System.out.println(N - set.size());
        // 7 4 2 3 1 6 8 9 5 10
    }
}
