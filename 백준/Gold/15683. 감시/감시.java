import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int answer = 100;
    static int[][] arr;
    static List<int[]> cctv = new ArrayList<>();

    public static void dfs(int cnt, int[][] arr){
        if (cnt == cctv.size()){
            checkAnswer(arr);
            return;
        }

        int num = cctv.get(cnt)[0];
        int x = cctv.get(cnt)[1];
        int y = cctv.get(cnt)[2];
        int [][] tmp;

        if (num == 1){
            tmp = copyArr(arr);
            checkUp(tmp, x, y);
            dfs(cnt + 1, tmp);

            tmp = copyArr(arr);
            checkRight(tmp, x, y);
            dfs(cnt + 1, tmp);

            tmp = copyArr(arr);
            checkDown(tmp, x, y);
            dfs(cnt + 1, tmp);

            tmp = copyArr(arr);
            checkLeft(tmp, x, y);
            dfs(cnt + 1, tmp);
        }else if (num == 2){
            tmp = copyArr(arr);
            checkUp(tmp, x, y);
            checkDown(tmp, x, y);
            dfs(cnt + 1, tmp);

            tmp = copyArr(arr);
            checkRight(tmp, x, y);
            checkLeft(tmp, x, y);
            dfs(cnt + 1, tmp);
        }else if (num == 3){
            tmp = copyArr(arr);
            checkLeft(tmp, x, y);
            checkDown(tmp, x, y);
            dfs(cnt + 1, tmp);

            tmp = copyArr(arr);
            checkLeft(tmp, x, y);
            checkUp(tmp, x, y);
            dfs(cnt + 1, tmp);

            tmp = copyArr(arr);
            checkRight(tmp, x, y);
            checkUp(tmp, x, y);
            dfs(cnt + 1, tmp);

            tmp = copyArr(arr);
            checkRight(tmp, x, y);
            checkDown(tmp, x, y);
            dfs(cnt + 1, tmp);
        }else if (num == 4){
            tmp = copyArr(arr);
            checkLeft(tmp, x, y);
            checkRight(tmp, x, y);
            checkDown(tmp, x, y);
            dfs(cnt + 1, tmp);

            tmp = copyArr(arr);
            checkLeft(tmp, x, y);
            checkUp(tmp, x, y);
            checkDown(tmp, x, y);
            dfs(cnt + 1, tmp);

            tmp = copyArr(arr);
            checkLeft(tmp, x, y);
            checkRight(tmp, x, y);
            checkUp(tmp, x, y);
            dfs(cnt + 1, tmp);

            tmp = copyArr(arr);
            checkUp(tmp, x, y);
            checkRight(tmp, x, y);
            checkDown(tmp, x, y);
            dfs(cnt + 1, tmp);
        }else if (num == 5){
            tmp = copyArr(arr);
            checkUp(tmp, x, y);
            checkRight(tmp, x, y);
            checkDown(tmp, x, y);
            checkLeft(tmp, x, y);
            dfs(cnt + 1, tmp);
        }

    }
    public static void checkLeft(int[][] tmp, int x, int y) {
        for(int i = y - 1; i >= 0; i--) {
            if(tmp[x][i] == 6)
                return;
            if(tmp[x][i] != 0)
                continue;
            tmp[x][i] = -1;
        }
    }

    public static void checkRight(int[][] tmp, int x, int y) {
        for(int i = y + 1; i < m; i++) {
            if(tmp[x][i] == 6)
                return;
            if(tmp[x][i] != 0)
                continue;
            tmp[x][i] = -1;
        }
    }

    public static void checkUp(int[][] tmp, int x, int y) {
        for(int i = x - 1; i >= 0; i--) {
            if(tmp[i][y] == 6)
                return;
            if(tmp[i][y] != 0)
                continue;
            tmp[i][y] = -1;
        }
    }

    public static void checkDown(int[][] tmp, int x, int y) {
        for(int i = x + 1; i < n; i++) {
            if(tmp[i][y] == 6)
                return;
            if(tmp[i][y] != 0)
                continue;
            tmp[i][y] = -1;
        }
    }


    public static void checkAnswer(int[][] tmp){
        int cnt = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (tmp[i][j] == 0){
                    cnt ++;
                }
            }
        }
        answer = Math.min(answer, cnt);
    }

    public static int[][] copyArr(int[][] arr) {
        int[][] tmp = new int[n][m];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                tmp[i][j] = arr[i][j];
            }
        }

        return tmp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] != 0 && arr[i][j] <= 5)
                    cctv.add(new int[]{arr[i][j], i, j});
            }
        }
        dfs(0, arr);
        System.out.println(answer);
    }
}
