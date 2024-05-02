import java.util.*;
import java.io.*;

public class Main {
	static int cnt;
	static int n;
	static int[][] arr;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static PriorityQueue<int[]> q = new PriorityQueue<>(new Comparator<int []>() {
		@Override
		public int compare(int[] o1, int[] o2) {
			if (o1[0] == o2[0]) return o1[1] - o2[1];
			return o1[0] - o2[0];
		}
	});
	private static int dijkstra(){
		q.offer(new int[]{arr[0][0], 0, 0});
		int[][] dist = new int[n][n];
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				dist[i][j] = Integer.MAX_VALUE;
			}
		}

		dist[0][0] = arr[0][0];
		while (!q.isEmpty()){
			int[] tmp = q.poll();
			int cost = tmp[0];
			int x = tmp[1];
			int y = tmp[2];

			if (dist[x][y] < cost){
				continue;
			}
			for (int i = 0; i < 4; i++){
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < n && 0 <= ny && ny < n){
					if (arr[nx][ny] + cost < dist[nx][ny]){
						dist[nx][ny] = arr[nx][ny] + cost;
						q.offer(new int[]{dist[nx][ny], nx, ny});
					}

				}
			}
		}
		return dist[n - 1][n - 1];
	}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		cnt = 1;
		while (true){
			n = Integer.parseInt(br.readLine());
			if (n == 0){
				return;
			}
			arr = new int[n][n];
			StringTokenizer st;
			for (int i = 0; i < n; i++){
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j< n; j++){
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			System.out.printf("Problem %d: %d\n", cnt++, dijkstra());
		}
	}
}