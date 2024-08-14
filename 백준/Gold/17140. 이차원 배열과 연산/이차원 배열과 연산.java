import java.io.*;
import java.util.*;

public class Main {
    static int r, c, k, answer;
    static int rl, cl;
    static int[][] arr = new int[101][101];
    static class Pair implements Comparable<Pair>{
        int num;
        int cnt;

        public Pair(int num, int cnt) {
            this.num = num;
            this.cnt = cnt;
        }

        @Override
        public int compareTo(Pair o) {
            if(this.cnt == o.cnt) {
                return this.num - o.num;
            }
            return this.cnt - o.cnt;
        }
    }
    public static void functionR(){
        int[][] tmp = new int[101][101];
        int col = 0;
        for (int i = 0; i < rl; i++) {
            Map<Integer, Integer> cnt = new HashMap<>();
            for (int j = 0; j < cl; j++) {
                if (arr[i][j] == 0)
                    continue;
                cnt.put(arr[i][j], cnt.getOrDefault(arr[i][j], 0) + 1);
            }

            List<Pair> list = new ArrayList<>();
            for (Map.Entry<Integer, Integer> entry : cnt.entrySet()) {
                list.add(new Pair(entry.getKey(), entry.getValue()));
            }
            col = Math.max(col, list.size() * 2);
            Collections.sort(list);
            for (int j = 0; j < list.size(); j++) {
                if (j >= 50)
                    break;
                Pair pair = list.get(j);
                tmp[i][2 * j] = pair.num;
                tmp[i][2 * j + 1] = pair.cnt;
            }
        }
        cl = Math.min(99, col);
        arr = tmp;
    }

    public static void functionC(){
        int[][] tmp = new int[101][101];
        int row = 0;
        for (int i = 0; i < cl; i++) {
            Map<Integer, Integer> cnt = new HashMap<>();
            for (int j = 0; j < rl; j++) {
                if (arr[j][i] == 0)
                    continue;
                cnt.put(arr[j][i], cnt.getOrDefault(arr[j][i], 0) + 1);
            }

            List<Pair> list = new ArrayList<>();
            for (Map.Entry<Integer, Integer> entry : cnt.entrySet()) {
                list.add(new Pair(entry.getKey(), entry.getValue()));
            }
            row = Math.max(row, list.size() * 2);
            Collections.sort(list);
            for (int j = 0; j < list.size(); j++) {
                if (j >= 50)
                    break;
                Pair pair = list.get(j);
                tmp[2 * j][i] = pair.num;
                tmp[2 * j + 1][i] = pair.cnt;
            }
        }
        rl = Math.min(99, row);
        arr = tmp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken()) - 1;
        c = Integer.parseInt(st.nextToken()) - 1;
        k = Integer.parseInt(st.nextToken());
        rl = 3;
        cl = 3;

        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int time = 0;
        while (time <= 100){
            if (arr[r][c] == k){
                answer = time;
                break;
            }
            if (rl >= cl)
                functionR();
            else
                functionC();
            time ++;
        }
        System.out.println((time >= 101) ? -1 : answer);
    }
}