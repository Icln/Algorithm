import java.io.*;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 *  No.16920: 확장 게임
 *  Hint: BFS + 구현
 */

public class Main {
    static int n, m, p;
    static int[] s;
    static ArrayList<Point>[] starts;   // BFS를 시작할 시작점들
    static int[] cnt;
    static boolean[][] visited;

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());
        starts = new ArrayList[p + 1];
        for (int i = 1; i <= p; i++) {
            starts[i] = new ArrayList<>();
        }

        s = new int[p + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= p; i++) {
            s[i] = Integer.parseInt(st.nextToken());
        }

        visited = new boolean[n][m];
        cnt = new int[p + 1];
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < m; j++) {
                char c = s.charAt(j);
                if (c == '#') { // 벽이면 방문한 걸로 침
                    visited[i][j] = true;
                } else if (c != '.') {  // 숫자면 방문 표시를 하고 시작점 리스트에  추가
                    starts[c - '0'].add(new Point(i, j, 0));
                    visited[i][j] = true;
                    cnt[c - '0']++;
                }
            }
        }

        while (true) {
            boolean endFlag = false;    // 새로 방문한 곳이 있는지를 표시
            for (int i = 1; i <= p; i++) {
                endFlag = bfs(i) || endFlag;
            }

            // 더이상 새로 방문한 곳이 없다면 루프 탈출
            if (!endFlag) {
                break;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= p; i++) {
            sb.append(cnt[i] + " ");
        }

        bw.write(sb.toString().trim());
        bw.close();
        br.close();
    }

    // 새로운 곳을 방문했으면 true 리턴
    static boolean bfs(int idx) {
        Queue<Point> q = new ArrayDeque<>();

        // 시작점들을 모두 큐에 삽입
        for (Point start : starts[idx]) {
            q.offer(start);
        }
        starts[idx].clear();    // 시작점 리스트 비움

        while (!q.isEmpty()) {
            Point cur = q.poll();

            // 시작점으로 부터 가장 먼 곳은 다음 BFS의 시작점으로 하기 위해 리스트에 추가
            if (cur.dist == s[idx]) {
                cur.setDist();
                starts[idx].add(cur);
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (isInRange(nx, ny) && canMove(nx, ny) && cur.dist < s[idx]) {
                    q.offer(new Point(nx, ny, cur.dist + 1));
                    visited[nx][ny] = true;
                    cnt[idx]++;
                }
            }
        }

        // 시작점 리스트가 비어 있음 == 새로 방문한 곳이 없음
        return !starts[idx].isEmpty();
    }

    static boolean canMove(int x, int y) {
        if (!visited[x][y]) {
            return true;
        }
        return false;
    }

    static boolean isInRange(int x, int y) {
        if (x >= 0 && x < n && y >= 0 && y < m) {
            return true;
        }
        return false;
    }

    static class Point {
        int x, y, dist;

        Point(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        public void setDist() {
            this.dist = 0;
        }
    }
}