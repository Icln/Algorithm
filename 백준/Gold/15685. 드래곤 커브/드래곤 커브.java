import java.io.*;
import java.util.*;

public class Main{
    static int n;
    static boolean[][] arr = new boolean[101][101];
    static int[][] dir = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};
    public static void curve(int x, int y, int d, int g){
        List<Integer> list = new ArrayList<>();
        list.add(d);
        for (int i = 1; i <= g; i++) {
            for (int j = list.size() - 1; j >= 0; j--) {
                int tmp = (list.get(j) == 3) ? 0 : list.get(j) + 1;
                list.add(tmp);
            }
        }

        arr[y][x] = true;
        int ny = y, nx = x;
        for (Integer i : list) {
            nx += dir[i][0];
            ny += dir[i][1];
            arr[ny][nx] = true;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            curve(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        int answer = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (arr[i][j] && arr[i + 1][j] && arr[i][j + 1] && arr[i + 1][j + 1])
                    answer++;
            }
        }
        System.out.println(answer);
    }
}