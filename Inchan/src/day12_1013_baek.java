import java.io.*;
import java.util.*;

public class day12_1013_baek {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        String pattern = "(100+1+|01)+";
        for (int i = 0; i < T; i++) {
            String s = br.readLine();
            if(s.matches(pattern)) {
                sb.append("YES").append("\n");
            }
            else {
                sb.append("NO").append("\n");
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
