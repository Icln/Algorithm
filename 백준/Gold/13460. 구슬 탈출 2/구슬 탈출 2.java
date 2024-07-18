import java.nio.Buffer;
import java.util.*;
import java.io.*;
public class Main {
    static int n, m;
    static char[][] arr;
    static Node node;
    static boolean[][][][] visited;
    static int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    static class Node{
        int rx, ry, bx, by, cnt;
        public Node(int rx, int ry, int bx, int by, int cnt){
            this.rx = rx;
            this.ry = ry;
            this.bx = bx;
            this.by = by;
            this.cnt = cnt;
        }
    }

    public static int bfs(){
        Queue<Node> q = new LinkedList<>();
        q.offer(node);
        visited[node.rx][node.ry][node.bx][node.by] = true;
        
        while(!q.isEmpty()) {
            Node tmp = q.poll();
            int rx = tmp.rx, ry = tmp.ry, bx = tmp.bx, by = tmp.by, cnt = tmp.cnt;
            if (cnt == 10)
                continue;

            for (int i = 0; i < 4; i++) {
                int nrx = rx, nry = ry, nbx = bx, nby = by;
                boolean isRedHole = false, isBlueHole = false;
                while (arr[nrx + d[i][0]][nry + d[i][1]] != '#') {
                    if (arr[nrx+ d[i][0]][nry+ d[i][1]] == 'O') {
                        isRedHole = true;
                        break;
                    }
                    nrx += d[i][0];
                    nry += d[i][1];
                }
                while (arr[nbx+ d[i][0]][nby+ d[i][1]] != '#') {
                    if (arr[nbx+ d[i][0]][nby+ d[i][1]] == 'O') {
                        isBlueHole = true;
                        break;
                    }
                    nbx += d[i][0];
                    nby += d[i][1];
                }
                if (isBlueHole)
                    continue;
                if (isRedHole)
                    return cnt + 1;

                if (nrx == nbx && nry == nby) {
                    if (i == 0) {
                        if (rx > bx)
                            nrx++;
                        else
                            nbx++;
                    } else if (i == 1) {
                        if (rx < bx)
                            nrx--;
                        else
                            nbx--;
                    } else if (i == 2) {
                        if (ry > by)
                            nry++;
                        else
                            nby++;

                    } else {
                        if (ry < by)
                            nry--;
                        else
                            nby--;
                    }
                }
                
                if(!visited[nrx][nry][nbx][nby]) {
                    visited[nrx][nry][nbx][nby] = true;
                    q.offer(new Node(nrx, nry, nbx, nby, cnt + 1));
                }

            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new char[n][m];
        visited = new boolean[n][m][n][m];
        node = new Node(0, 0, 0, 0, 0);

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < m; j++) {
                if (s.charAt(j) == 'R') {
                    node.rx = i;
                    node.ry = j;
                } else if (s.charAt(j) == 'B') {
                    node.bx = i;
                    node.by = j;
                }
                arr[i][j] = s.charAt(j);
            }
        }

        System.out.println(bfs());
    }
}
