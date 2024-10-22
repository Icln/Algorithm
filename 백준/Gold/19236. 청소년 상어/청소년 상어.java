import java.io.*;
import java.util.*;

public class Main {
	static int answer = -1;
	static int[][] d = {{}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};
	public static boolean canMove(int x, int y, int sx, int sy) {
		return (x != sx || y != sy) && (x >= 0 && x < 4 && y >= 0 && y < 4);
	}

	public static int rotate(int x, int y, int sx, int sy, int tmp) {
		int cnt = 0;
		while (cnt++ != 7) {
			if (++tmp > 8) tmp = 1;
			if (canMove(x + d[tmp][0], y + d[tmp][1], sx, sy)) {
				return tmp;
			}
		}
		return tmp;
	}

	public static void swap(int[][] arr, int[][] dir, HashMap<Integer, int[]> pos, int x, int y, int nx, int ny) {
		int tmp = arr[x][y];
		arr[x][y] = arr[nx][ny];
		arr[nx][ny] = tmp;

		tmp = dir[x][y];
		dir[x][y] = dir[nx][ny];
		dir[nx][ny] = tmp;

		pos.put(arr[nx][ny], new int[]{nx, ny});
		pos.put(arr[x][y], new int[]{x, y});
	}
    
	public static void moveFish(int[][] arr, int[][] dir, HashMap<Integer, int[]> pos, int sx, int sy) {
		for (int i = 1; i <= 16; i++) {
			int[] cur = pos.getOrDefault(i, null);
			if (cur != null) {
				int nx = cur[0] + d[dir[cur[0]][cur[1]]][0];
				int ny = cur[1] + d[dir[cur[0]][cur[1]]][1];
				if (canMove(nx, ny, sx, sy))
					swap(arr, dir, pos, cur[0], cur[1], nx, ny);
				else {
					int tmp = rotate(cur[0], cur[1], sx, sy, dir[cur[0]][cur[1]]);
					if (tmp != dir[cur[0]][cur[1]]) {
						dir[cur[0]][cur[1]] = tmp;
						swap(arr, dir, pos, cur[0], cur[1], cur[0] + d[tmp][0], cur[1] + d[tmp][1]);
					}
				}
			}
		}
	}
    
	public static void dfs(int[][] arr, int[][] dir, HashMap<Integer, int[]> pos, int sum, int sx, int sy, int curDir) {
		answer = Math.max(answer, sum);

		int[][] copyArr = new int[4][4];
		int[][] copyDir = new int[4][4];
		for (int i = 0; i < 4; i++) {
			copyArr[i] = arr[i].clone();
			copyDir[i] = dir[i].clone();
		}
		HashMap<Integer, int[]> copyPos = (HashMap<Integer, int[]>) pos.clone();

		moveFish(copyArr, copyDir, copyPos, sx, sy);
		for (int i = 1; i < 4 ; i++) {
			int nx = sx + d[curDir][0] * i;
			int ny = sy + d[curDir][1] * i;
			if(nx < 0 || nx >= 4 || ny < 0 || ny >= 4) break;
			if(copyArr[nx][ny] != 0) {
				int num = copyArr[nx][ny];
				int tmpDir = copyDir[nx][ny];
				copyArr[nx][ny] = 0;
				copyDir[nx][ny] = tmpDir;
				copyPos.remove(num);
				dfs(copyArr, copyDir, copyPos, sum + num, nx, ny, tmpDir);
				copyArr[nx][ny] = num;
				copyPos.put(num, new int[]{nx, ny});
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int[][] arr = new int[4][4];
		int[][] dir = new int[4][4];
		HashMap<Integer, int[]> pos = new HashMap<>();

		for (int i = 0; i < 4; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 4; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				dir[i][j] = Integer.parseInt(st.nextToken());
				pos.put(arr[i][j], new int[]{i, j});
			}
		}

		answer = arr[0][0];
		int curDir = dir[0][0];
		int sx = 0;
		int sy = 0;
		pos.remove(arr[0][0]);
		arr[0][0] = 0;

		dfs(arr, dir, pos, answer, sx, sy, curDir);
		System.out.println(answer);
	}

}