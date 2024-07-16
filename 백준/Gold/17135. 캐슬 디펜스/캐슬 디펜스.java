import java.util.*;
import java.io.*;

public class Main {
    static final int ARCHER_NUM = 3;
    static boolean flag;
    static int answer;
    static int n, m, d;
    static int[][] origin;
    static List<int[]> enemyPos = new ArrayList<>();

    public static boolean enemyFind(int[][] arr){
        flag = false;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (arr[i][j] == 1){
                    enemyPos.add(new int[]{i, j});
                    flag = true;
                }
            }
        }
        return flag;
    }

    public static void enemyDown(int[][] arr){
        for (int i = 0; i < n; i++)
            Arrays.fill(arr[i], 0);

        for (int i = 0; i < enemyPos.size(); i++){
            if (enemyPos.get(i)[0] != n - 1){
                arr[enemyPos.get(i)[0] + 1][enemyPos.get(i)[1]] = 1;
            }
        }
    }

    public static void placeArcher(boolean[] visited, int start, int depth){
        if(depth == ARCHER_NUM){
            List<Integer> archers = new ArrayList<>();
            for(int i = 0; i < m; i++){
                if(visited[i])
                    archers.add(i);
            }

            int[][] arr = new int[n][m];
            for (int i = 0; i < n; i++){
                for (int j = 0; j < m; j++){
                    arr[i][j] = origin[i][j];
                }
            }

            answer = Math.max(answer, attack(archers, arr));
            return;
        }
        for(int i = start; i < m; i++){
            if(!visited[i]){
                visited[i] = true;
                placeArcher(visited, i + 1, depth + 1);
                visited[i] = false;
            }
        }
    }

    public static int attack(List<Integer> archers, int[][] arr){
        int tmp = 0;
        while (enemyFind(arr)){
            List<int[]> enemy = new ArrayList<>();
            int idx = 0;
            for (int archer : archers){
                boolean enter = true;
                int dist = Integer.MAX_VALUE;
                for (int[] pos: enemyPos){
                    int a = Math.abs(n - pos[0]) + Math.abs(archer - pos[1]);
                    if (dist >= a && a <= d){
                        if (dist == a){
                            if (pos[1] <= enemy.get(idx)[1]){
                                enemy.get(idx)[0] = pos[0];
                                enemy.get(idx)[1] = pos[1];
                            }
                        }
                        else{
                            dist = a;
                            if (enter){
                                idx = enemy.size();
                                enemy.add(new int[]{pos[0], pos[1]});
                                enter = false;
                            }
                            else{
                                enemy.get(idx)[0] = pos[0];
                                enemy.get(idx)[1] = pos[1];
                            }
                        }
                    }
                }
            }

            int originLength = enemyPos.size();
            for (int i = 0; i < enemy.size(); i++){
                removeEnemyPosition(new int[]{enemy.get(i)[0], enemy.get(i)[1]});
            }
            tmp += (originLength - enemyPos.size());

            enemyDown(arr);
            enemyPos.clear();
        }
        return tmp;
    }

    private static void removeEnemyPosition(int[] pos) {
        enemyPos.removeIf(p -> p[0] == pos[0] && p[1] == pos[1]);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        origin = new int[n][m];
        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++){
                origin[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        placeArcher(new boolean[m], 0, 0);
        System.out.println(answer);
    }
}