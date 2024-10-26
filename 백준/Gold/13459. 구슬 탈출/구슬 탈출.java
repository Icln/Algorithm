import java.io.*;
import java.util.*;

public class Main {
	static int n, m, rx, ry, bx, by, ex, ey;
	static char[][] board;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};

	public static int bfs(){
		Queue<int[]> q = new ArrayDeque<>();
		q.offer(new int[]{rx, ry, bx, by, 0});
		while(!q.isEmpty()){
			int[] cur = q.poll();
			if (cur[4] >= 10) return 0;

			for (int i = 0; i < 4; i++) {
				int x1 = cur[0], y1 = cur[1], x2 = cur[2], y2 = cur[3];
				boolean isRed = false, isBlue = false;
				while (true) {
					int nx = x1 + dx[i];
					int ny = y1 + dy[i];
					if (board[nx][ny] == '#') break;
					if (board[nx][ny] == 'O') {
						isRed = true;
						break;
					}

					x1 = nx;
					y1 = ny;
				}

				while (true) {
					int nx = x2 + dx[i];
					int ny = y2 + dy[i];
					if (board[nx][ny] == '#') break;
					if (board[nx][ny] == 'O') {
						isBlue = true;
						break;
					}

					x2 = nx;
					y2 = ny;
				}

				if (isBlue) continue;
				if (isRed) return 1;
				if (cur[0] == x1 && cur[1] == y1 && cur[2] == x2 && cur[3] == y2) continue;
				if (x1 == x2 && y1 == y2) {
					if (i == 0) {
						if (cur[0] < cur[2]) x2++;
						else x1++;
					} else if (i == 1) {
						if (cur[0] < cur[2]) x1--;
						else x2--;
					} else if (i == 2) {
						if (cur[1] < cur[3]) y2++;
						else y1++;
					} else if (i == 3) {
						if (cur[1] < cur[3]) y1--;
						else y2--;
					}
				}

				q.offer(new int[]{x1, y1, x2, y2, cur[4] + 1});
			}
		}
		return 0;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		board = new char[n][m];
		for (int i = 0; i < n; i++) {
			String s = br.readLine();
			for (int j = 0; j < m; j++){
				board[i][j] = s.charAt(j);
				if (board[i][j] == 'R'){
					rx = i;
					ry = j;
				}
				else if (board[i][j] == 'B'){
					bx = i;
					by = j;
				}
				else if (board[i][j] == 'O'){
					ex = i;
					ey = j;
				}
			}
		}

		System.out.println(bfs());
	}
}