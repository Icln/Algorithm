import java.util.*;
import java.io.*;

public class Main {
    static int r, c, answer;
    static char[][] arr;
    static boolean[][] visited;
    static ArrayDeque<Node> q = new ArrayDeque<>();
    static int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static class Node{
        int x, y, z;
        char c;
        Node(int x, int y, int z, char c){
            this.x = x;
            this.y = y;
            this.z = z;
            this.c = c;
        }
    }
    public static int bfs(){
        while (!q.isEmpty()){
            Node tmp = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = tmp.x + d[i][0], ny = tmp.y + d[i][1];
                if (nx < 0 || nx >= r || ny < 0 || ny >= c){
                    if (tmp.c == 'F')
                        continue;
                    else
                        return tmp.z + 1;
                }
                if (tmp.c == 'F' && arr[nx][ny] == '.' && !visited[nx][ny]){
                    arr[nx][ny] = 'F';
                    visited[nx][ny] = true;
                    q.add(new Node(nx, ny, tmp.z + 1, 'F'));
                } else if (tmp.c =='J' && arr[nx][ny] == '.'&& !visited[nx][ny]) {
                    arr[nx][ny] = 'J';
                    visited[nx][ny] = true;
                    q.add(new Node(nx, ny, tmp.z + 1, 'J'));
                }
            }
        }
        return 0;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        arr = new char[r][c];
        visited = new boolean[r][c];

        for (int i = 0; i < r; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < c; j++) {
                arr[i][j] = tmp.charAt(j);
                if (arr[i][j] == 'F'){
                    q.offerFirst(new Node(i, j, 0,'F'));
                    visited[i][j] = true;
                }
                else if (arr[i][j] == 'J'){
                    q.offerLast(new Node(i, j , 0,'J'));
                    visited[i][j] = true;
                }
            }
        }

        answer = bfs();
        System.out.println((answer != 0) ? answer: "IMPOSSIBLE");
    }
}