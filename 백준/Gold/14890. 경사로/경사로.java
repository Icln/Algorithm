import java.io.*;
import java.util.*;

public class Main {
    static int n, l, answer;
    static int[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        arr = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        //열 검사
        for (int i = 0; i < n; i++) {
            boolean[] visited = new boolean[n];
            int cur = arr[0][i];
            for (int j = 1; j < n; j++) {
                if (Math.abs(cur - arr[j][i]) >= 2)
                    break;

                if (cur > arr[j][i] && cur - arr[j][i] == 1) { // 감소할 때
                    int tmp = arr[j][i];
                    boolean flag = false;
                    for (int k = j; k < j + l; k++) {
                        if (k >= n) { // 범위 벗어나면
                            flag = true;
                            break;
                        }
                        if (visited[k] || tmp != arr[k][i]) { // 같은 높이 아니거나 지어진적 있으면
                            flag = true;
                            break;
                        }
                        visited[k] = true;
                    }
                    if (flag)
                        break;
                    cur = arr[j][i];
                    j += l;
                    j--;
                }

                else if (arr[j][i] > cur && arr[j][i] - cur == 1) { // 증가할 때
                    int tmp = cur;
                    boolean flag = false;
                    for (int k = j - l;  k < j; k++) {
                        if (k < 0) { // 범위 벗어나면
                            flag = true;
                            break;
                        }
                        if (visited[k] || tmp != arr[k][i]) { // 같은 높이 아니거나 지어진적 있으면
                            flag = true;
                            break;
                        }
                        visited[k] = true;
                    }
                    if (flag)
                        break;
                    cur = arr[j][i];
                }

                if (j == n - 1)
                    answer ++;
            }
        }
        //행검사
        for (int i = 0; i < n; i++) {
            boolean[] visited = new boolean[n];
            int cur = arr[i][0];
            for (int j = 1; j < n; j++) {
                if (Math.abs(cur - arr[i][j]) >= 2)
                    break;

                if (cur > arr[i][j] && cur - arr[i][j] == 1) { // 감소할 때
                    int tmp = arr[i][j];
                    boolean flag = false;
                    for (int k = j; k < j + l; k++) {
                        if (k >= n) { // 범위 벗어나면
                            flag = true;
                            break;
                        }
                        if (visited[k] || tmp != arr[i][k]) { // 같은 높이 아니거나 지어진적 있으면
                            flag = true;
                            break;
                        }
                        visited[k] = true;
                    }
                    if (flag)
                        break;

                    cur = arr[i][j];
                    j += l;
                    j--;
                }

                else if (arr[i][j] > cur && arr[i][j] - cur == 1) { // 증가할 때
                    int tmp = cur;
                    boolean flag = false;
                    for (int k = j - l;  k < j; k++) {
                        if (k < 0) { // 범위 벗어나면
                            flag = true;
                            break;
                        }
                        if (visited[k] || tmp != arr[i][k]) { // 같은 높이 아니거나 지어진적 있으면
                            flag = true;
                            break;
                        }
                        visited[k] = true;
                    }
                    if (flag)
                        break;
                    cur = arr[i][j];
                }

                if (j == n - 1)
                    answer ++;

            }
        }
        System.out.println(answer);
    }
}
