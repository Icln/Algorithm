import java.io.*;
import java.util.*;

public class Main {
	static int n, answer;
	static int[][] map;
	static ArrayList<int[]> posB, posW;
	static int[] dx = {1, 1};
	static int[] dy = {1, -1};

	public static void dfs(int x, int y, int cnt, int idx, int[][] visited, ArrayList<int[]> pos) {
		answer = Math.max(answer, cnt);
		visited[x][y] += 1;

		for (int i = 0; i < 2; i++)
			arrive(x + dx[i], y + dy[i], i, visited);

		for (int i = idx + 1; i < pos.size(); i++) {
			if (visited[pos.get(i)[0]][pos.get(i)[1]] != 0) continue;
			dfs(pos.get(i)[0], pos.get(i)[1], cnt + 1, i, visited, pos);
		}

		visited[x][y] -= 1;
		for (int i = 0; i < 2; i++)
			leave(x + dx[i], y + dy[i], i, visited);
	}

	public static void arrive(int x, int y, int d, int[][] visited){
		if (x < 0 || x >= n || y < 0 || y >= n) return;
		visited[x][y] += 1;
		arrive(x + dx[d], y + dy[d], d, visited);
	}

	public static void leave(int x, int y, int d, int[][] visited){
		if (x < 0 || x >= n || y < 0 || y >= n) return;
		visited[x][y] -= 1;
		leave(x + dx[d], y + dy[d], d, visited);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		map = new int[n][n];
		StringTokenizer st;

		posB = new ArrayList<>();
		posW = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 1){
					if ((i + j) % 2 == 0) posB.add(new int[]{i, j});
					else posW.add(new int[]{i, j});
				}
			}
		}

		for (int i = 0; i < posB.size(); i++)
				dfs(posB.get(i)[0], posB.get(i)[1], 1, i, new int[n][n], posB);
		int tmp = answer;
		answer = 0;
		for (int i = 0; i < posW.size(); i++)
			dfs(posW.get(i)[0], posW.get(i)[1], 1, i, new int[n][n], posW);
		System.out.println(tmp + answer);
	}
}
