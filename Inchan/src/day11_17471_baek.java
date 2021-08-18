import java.io.*;
import java.util.*;

public class day11_17471_baek {
    static int N, min = Integer.MAX_VALUE;
    static int[] people;
    static Area[] areas;
    static boolean[] bfsVisited, visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        N = Integer.parseInt(br.readLine());
        people = new int[N + 1];
        areas = new Area[N + 1];
        visited = new boolean[N + 1];
        StringTokenizer initial = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            people[i] = Integer.parseInt(initial.nextToken());
            areas[i] = new Area(i, people[i]);
        }
        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            for (int j = 0; j < n; j++) {
                int a = Integer.parseInt(st.nextToken());
                areas[i].adj.add(a);
//                areas[a].adj.add(i);
            }
        }

        for (int i = 1; i < N; i++) {
            for (int j = 1; j <= N - i + 1; j++) {
                backtracking(j, 0, i);
            }
        }
        if(min == Integer.MAX_VALUE) min = -1;

        bw.write(min + "\n");
        bw.flush();
        bw.close();

    }

    static void backtracking(int now, int count, int max) {
        if(count == max) {
            List<Integer> reds = new ArrayList<>();
            List<Integer> blues = new ArrayList<>();
            for (int i = 1; i <= N; i++) {
                if(areas[i].isRed) {
                    reds.add(i);
                    areas[i].isBlue = false;
                }
                else {
                    blues.add(i);
                    areas[i].isRed = false;
                    areas[i].isBlue = true;
                }
            }
            arg ret = new arg();
            if (promising(reds, blues, ret)) {
                min = Math.min(min, ret.diff);
            }
            return;
        }

        for (int i = now; i <= N; i++) {
            if(visited[i]) continue;
            visited[i] = true;
            areas[i].isRed = true;
            backtracking(i, count + 1, max);
            visited[i] = false;
            areas[i].isRed = false;
        }
    }
    static boolean promising(List<Integer> reds, List<Integer> blues, arg ret) {
        bfsVisited = new boolean[N + 1];
        Queue<Integer> q = new LinkedList<>();
        q.add(reds.get(0));
        bfsVisited[reds.get(0)] = true;
        int count = 0;
        int redPeople = 0;
        while(!q.isEmpty()) {
            int now = q.remove();
            redPeople += areas[now].people;
            count++;

            for (int a : areas[now].adj) {
                if (!bfsVisited[a] && areas[a].isRed) {
                    q.add(a);
                    bfsVisited[a] = true;

                }
            }
        }
        if(count != reds.size()) return false;
        count = 0;
        int bluePeople = 0;
        q.add(blues.get(0));
        bfsVisited[blues.get(0)] = true;
        while (!q.isEmpty()) {
            int now = q.remove();
            bluePeople += areas[now].people;
            count++;

            for (int a : areas[now].adj) {
                if(!bfsVisited[a] && areas[a].isBlue) {
                    bfsVisited[a] = true;
                    q.add(a);
                }
            }
        }
        if(count != blues.size()) return false;
        ret.diff = Math.abs(bluePeople - redPeople);
        return true;
    }
}
class arg {
    int diff = 0;
}
class Area {
    int number;
    int people;
    boolean isRed, isBlue;
    List<Integer> adj;

    public Area(int number, int people) {
        this.number = number;
        this.people = people;
        this.isRed = false;
        this.isBlue = false;
        this.adj = new ArrayList<>();
    }
}
