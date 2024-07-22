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

        // 열 검사
        for (int i = 0; i < n; i++) {
            if (checkColumn(i)) 
                answer++;
            if (checkRow(i)) 
                answer++;
        }
        System.out.println(answer);
    }

    private static boolean checkColumn(int col) {
        boolean[] visited = new boolean[n];
        int cur = arr[0][col];

        for (int j = 1; j < n; j++) {
            if (Math.abs(cur - arr[j][col]) >= 2) 
                return false;

            if (cur > arr[j][col] && cur - arr[j][col] == 1) { // 감소할 때
                if (!decreasing(j, col, visited, true)) 
                    return false;
                cur = arr[j][col];
                j += l - 1;
            } else if (arr[j][col] > cur && arr[j][col] - cur == 1) { // 증가할 때
                if (!increasing(j, col, visited, true)) 
                    return false;
                cur = arr[j][col];
            }
        }
        return true;
    }

    private static boolean checkRow(int row) {
        boolean[] visited = new boolean[n];
        int cur = arr[row][0];

        for (int j = 1; j < n; j++) {
            if (Math.abs(cur - arr[row][j]) >= 2) return false;

            if (cur > arr[row][j] && cur - arr[row][j] == 1) { // 감소할 때
                if (!decreasing(j, row, visited, false)) return false;
                cur = arr[row][j];
                j += l - 1;
            } else if (arr[row][j] > cur && arr[row][j] - cur == 1) { // 증가할 때
                if (!increasing(j, row, visited, false)) return false;
                cur = arr[row][j];
            }
        }
        return true;
    }

    private static boolean decreasing(int start, int fixed, boolean[] visited, boolean isColumn) {
        int tmp = isColumn ? arr[start][fixed] : arr[fixed][start];
        for (int k = start; k < start + l; k++) {
            if (k >= n || visited[k] || (isColumn ? tmp != arr[k][fixed] : tmp != arr[fixed][k])) {
                return false;
            }
            visited[k] = true;
        }
        return true;
    }

    private static boolean increasing(int start, int fixed, boolean[] visited, boolean isColumn) {
        int tmp = isColumn ? arr[start - 1][fixed] : arr[fixed][start - 1];
        for (int k = start - l; k < start; k++) {
            if (k < 0 || visited[k] || (isColumn ? tmp != arr[k][fixed] : tmp != arr[fixed][k])) {
                return false;
            }
            visited[k] = true;
        }
        return true;
    }
}
