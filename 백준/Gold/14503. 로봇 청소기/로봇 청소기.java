import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, M, r, c, d, result;
	static int[][] map = new int[N][M];
	static int[][] delta = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int[N][M];

		st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++)
				map[i][j] = Integer.parseInt(st.nextToken());
		}

		function(r, c, d);
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				if (map[i][j] == 2) result++;

		System.out.println(result);
	}

	public static void function(int row, int col, int dir) {
		if (map[row][col] == 0)
			map[row][col] = 2; // 청소 완료 (0 -> 2)
		
		int count = 0;
		for (int d = 0; d < 4; d++) { // 청소 안한 개수 세주는 함수
			int nr = row + delta[d][0];
			int nc = col + delta[d][1];

			if (!isInGrid(nr, nc)) continue;
			if (map[nr][nc] == 0) count++;
		}

		// 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
		if (count == 0) {
			int nr = row;
			int nc = col;
			//상 우 하 좌 0 1 2 3
			if (dir == 0) {
				nr += delta[2][0];
				nc += delta[2][1];
			} else if (dir == 1) {
				nr += delta[3][0];
				nc += delta[3][1];
			} else if (dir == 2) {
				nr += delta[0][0];
				nc += delta[0][1];
			} else if (dir == 3) {
				nr += delta[1][0];
				nc += delta[1][1];
			}

			if (isInGrid(nr, nc) && map[nr][nc] != 1) 
				function(nr, nc, dir);
		}

		// 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
		else {
			int nd = dir;
			for (int i = 0; i < 4; i++) {
				nd -= 1;
				if (nd == -1) nd = 3;
				int nr = row + delta[nd][0];
				int nc = col + delta[nd][1];

				if (isInGrid(nr, nc) && map[nr][nc] == 0) {
					function(nr, nc, nd);
					break;
				}
			}
		}
	}

	public static boolean isInGrid(int nr, int nc) {
		if (nr < 0 || nr >= N || nc < 0 || nc >= M) return false;
		return true;
	}
}
