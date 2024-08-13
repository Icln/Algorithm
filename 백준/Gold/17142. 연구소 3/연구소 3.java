import java.io.*;
import java.util.*;

public class Main
{
    static int n, m, answer = Integer.MAX_VALUE;
    static int[][] arr;
    static int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static List<int[]> virus = new ArrayList<>();
    static int[][] tmpVirus;
    public static void bfs(int[][] tmpArr, boolean[][] visited, Queue<int[]> q){
        int max = Integer.MIN_VALUE;
        while(!q.isEmpty()){
            int[] tmp = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = tmp[0] + d[i][0], ny = tmp[1] + d[i][1];
                if (nx < 0 || nx >= n || ny < 0 || ny >= n || visited[nx][ny] || tmpArr[nx][ny] == -100)
                    continue;
                if (!visited[nx][ny] && (tmpArr[nx][ny] == -2 || tmpArr[nx][ny] == -1)){
                    int num = tmpArr[nx][ny];
                    tmpArr[nx][ny] = tmpArr[tmp[0]][tmp[1]] + 1;
                    if (num == -2)
                        max = Math.max(max, tmpArr[nx][ny] + 1);
                    q.offer(new int[]{nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }

        boolean flag = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (tmpArr[i][j] == -2){
                    flag = true;
                    break;
                }
            }
        }
        if (!flag)
            answer = Math.min(answer, max);
    }

    public static void combinations(int cnt, int idx){
        if (cnt == m){
            int[][] tmpArr = new int[n][n];
            boolean[][] visited = new boolean[n][n];
            Queue<int[]> q = new ArrayDeque<>();
            for (int i = 0; i < m; i++) {
                q.offer(new int[]{tmpVirus[i][0], tmpVirus[i][1]});
                tmpArr[tmpVirus[i][0]][tmpVirus[i][1]] = -1;
                visited[tmpVirus[i][0]][tmpVirus[i][1]] = true;
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    tmpArr[i][j] = arr[i][j];
                }
            }

            bfs(tmpArr, visited, q);
            return;
        }

        for (int i = idx; i < virus.size(); i++) {
            tmpVirus[cnt][0] = virus.get(i)[0];
            tmpVirus[cnt][1] = virus.get(i)[1];
            combinations(cnt + 1, i + 1);
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                char tmp = st.nextToken().charAt(0);
                if (tmp == '2') {
                    arr[i][j] = -1;
                    virus.add(new int[]{i, j});
                }
                else if (tmp == '1'){
                    arr[i][j] = -100;
                }
                else
                    arr[i][j] = -2;
            }
        }
        tmpVirus = new int[m][2];
        combinations(0, 0);
        if (answer == Integer.MIN_VALUE)
            System.out.println(0);
        else if (answer == Integer.MAX_VALUE)
            System.out.println(-1);
        else
            System.out.println(answer);
    }
}