import java.util.*;
import java.io.*;

public class Main{
	static int n, m, h, answer;
	static int[][] arr;
	public static void dfs(int x, int cnt){
		if (cnt > 3 || cnt >= answer)
			return;

		if (check()){
			answer = Math.min(answer, cnt);
			return;
		}

		for (int i = x; i <= h; i++) {
			for (int j = 1; j < n; j++) {
				if (arr[i][j] == 0 && arr[i][j + 1] == 0) {
					arr[i][j] = 1;
					arr[i][j + 1] = -1;
					dfs(i,cnt + 1);
					arr[i][j] = 0;
					arr[i][j + 1] = 0;
				}
			}
		}
	}

	public static boolean check() {
		for (int i = 1; i <= n; i++) {
			int x = 1;
			int y = i;

			while (x <= h) {
				if (arr[x][y] == 1)
					y++;
				else if (arr[x][y] == -1)
					y--;
				x++;
			}
			if (y != i)
				return false;
		}
		return true;
	}

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());

		arr = new int[h + 1][n + 1];
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			arr[x][y] = 1;
			arr[x][y + 1] = -1;
		}

		answer = Integer.MAX_VALUE;
		dfs(1, 0);
		System.out.println((answer == Integer.MAX_VALUE) ? -1 : answer);
	}
}