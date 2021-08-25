import java.io.*;
import java.util.*;
public class day15_2262_baek {
    static List<Integer> arr;
    static PriorityQueue<Rank> pq = new PriorityQueue<Rank>(Comparator.comparingInt(Rank::getRank).reversed());
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new ArrayList<>();
        if(N == 1) {
            bw.write("0\n");
            bw.flush();
            bw.close();
            return;
        }
        for (int i = 0; i < N; i++) {
            arr.add(Integer.parseInt(st.nextToken()));
            pq.add(new Rank(arr.get(i), i));
        }
        int ans = 0;
        while (arr.size() > 1) {
            Rank cur = pq.remove();
            int index = arr.indexOf(cur.rank);
            int gap;
            if(index == 0) {
                gap = arr.get(index) - arr.get(index + 1);
            } else if (index == arr.size() - 1) {
                gap = arr.get(index) - arr.get(index - 1);
            } else {
                int leftDiff = arr.get(index) - arr.get(index - 1);
                int rightDiff = arr.get(index)- arr.get(index + 1);
                gap = Math.min(leftDiff, rightDiff);
            }
            ans += gap;
            arr.remove(index);
        }
        bw.write(ans + "\n");
        bw.flush();
        bw.close();
    }
}
class Rank {
    int rank;
    int index;

    public Rank(int rank, int index) {
        this.rank = rank;
        this.index = index;
    }

    public int getRank() {
        return rank;
    }
}
