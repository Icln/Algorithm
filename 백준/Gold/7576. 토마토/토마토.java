import java.util.*;
import java.io.*;

public class Main {
	static int[] dx = { -1, 1, 0, 0};
	static int[] dy = { 0, 0, -1, 1};
	static int n, m;
	static int[][] arr;
	static Queue<int[]> q = new LinkedList<>();
	public static int bfs(){
		while (!q.isEmpty()){
			int[] pos = q.poll();
			int x = pos[0];
			int y = pos[1];

			for(int i = 0; i < 4; i++){
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (0 <= nx && nx < m && 0 <= ny && ny < n){
					if (arr[nx][ny] == 0){
						arr[nx][ny] =  arr[x][y] + 1;
						q.add(new int[]{nx, ny});
					}
				}
			}
		}

		int max = -1;
		for (int i = 0; i < m; i++){
			for (int j = 0; j < n; j++){
				if (arr[i][j] == 0)
					return -1;
				max = Math.max(max, arr[i][j]);
			}
		}
		return (max == 1) ? 0 : max - 1;

	}


	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[m][n];

		for (int i = 0; i < m; i++){
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++){
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 1){
					q.add(new int[]{i, j});
				}
			}
		}

		System.out.println(bfs());
	}
}