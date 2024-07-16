import java.util.*;
import java.io.*;

public class Main {
	static int n, m;
	static int answer;
	static int[][] arr;

	static boolean[][] visited;
	static int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

	public static void dfs(int sum, int x, int y, int depth){
		if(depth == 4) {
			answer = Math.max(answer, sum);
			return;
		}

		for(int i = 0 ; i < 4 ; i++) {
			int nx = x + d[i][0], ny = y + d[i][1];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;
			if (!visited[nx][ny]){
				visited[nx][ny] = true;
				dfs( sum + arr[nx][ny], nx, ny, depth + 1);
				visited[nx][ny] = false;
			}

		}
	}

	public static void combinations(int start, int depth, int x, int y, int sum) {
		if(depth == 3) {
			answer = Math.max(answer, sum);
			return;
		}
		for (int i = start; i < 4; i++) {
			int nx = x + d[i][0], ny = y + d[i][1];
			if(nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;
			combinations(i + 1, depth + 1, x, y, sum + arr[nx][ny]);
		}
	}


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		arr = new int[n][m];
		visited = new boolean[n][m];
		for (int i = 0; i < n; i++){
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++){
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for(int i = 0 ; i < n ; i++) {
			for(int j = 0 ; j < m ; j++) {
				visited[i][j] = true;
				dfs(arr[i][j], i, j, 1);
				visited[i][j] = false;
				combinations(0, 0, i, j,arr[i][j]);
			}
		}
		System.out.println(answer);
	}
}
