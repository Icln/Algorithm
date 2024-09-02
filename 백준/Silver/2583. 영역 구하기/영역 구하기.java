import java.util.*;
import java.io.*;

public class Main {
    static int m, n, k, cnt;
    static int[][] arr;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static List<Integer> answer = new ArrayList<>();
    public static void dfs(int x, int y, int num){
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;
            if (arr[nx][ny] == 0){
                arr[nx][ny] = num;
                cnt ++;
                dfs(nx, ny, num);
            }
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        arr = new int[n][m];

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int sx = Integer.parseInt(st.nextToken());
            int sy = Integer.parseInt(st.nextToken());
            int ex = Integer.parseInt(st.nextToken());
            int ey = Integer.parseInt(st.nextToken());
            for (int j = sx; j < ex; j++) {
                for (int l = sy; l < ey; l++) {
                    arr[j][l] = -1;
                }
            }
        }

        int num = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cnt = 1;
                if (arr[i][j] == 0){
                    arr[i][j] = ++num;
                    dfs(i, j, num);
                    answer.add(cnt);
                }
            }
        }
        Collections.sort(answer);

        System.out.println(num);
        for (Integer i : answer) {
            System.out.printf(i + " ");
        }

        // n, m 100이하
        // 얼은 지역은 사람이 걸어다닐 수 x
        // k개의 얼어붙은 영역을 직사각형으로 그렵니
        // 넓이 오름차순 정렬
        // 왼쪽아래 0,0,시작, 오른쪽 위 n, m
        // 왼쪽아래 xy, 오른쪽 위 xy
        // 02 44    0,3 0,2, 3,3
        // 21 36
        // 30 71
    }
}
