import java.io.*;
import java.util.*;

public class day6_13701_baek {
    static boolean[] check = new boolean[33554432];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        while(st.hasMoreTokens()){
            int a = Integer.parseInt(st.nextToken());
            if(!check[a]) {
                check[a] = true;
                sb.append(a).append(" ");
            }
        }
        bw.write(sb.toString() + "\n");
        bw.flush();
        bw.close();
    }
}
