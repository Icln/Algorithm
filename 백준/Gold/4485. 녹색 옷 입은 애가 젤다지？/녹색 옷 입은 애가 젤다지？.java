import java.util.*;
import java.io.*;

public class Main {
	static int cnt;
	static int n;
	static int[][] arr;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static Queue<Node> q = new PriorityQueue<>();
	static class Node implements Comparable<Node>{
		int x, y, cost;
		public Node(int x, int y, int cost){
			this.x = x;
			this.y = y;
			this.cost = cost;
		}

		@Override
		public int compareTo(Node o){
			return Integer.compare(this.cost, o.cost);
		}
	}
	private static int dijkstra(){
		q.offer(new Node(0, 0, arr[0][0]));
		int[][] dist = new int[n][n];
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				dist[i][j] = Integer.MAX_VALUE;
			}
		}

		dist[0][0] = arr[0][0];
		while (!q.isEmpty()){
			Node tmp = q.poll();
			int cost = tmp.cost;
			int x = tmp.x;
			int y = tmp.y;

			if (dist[x][y] < cost){
				continue;
			}
			for (int i = 0; i < 4; i++){
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < n && 0 <= ny && ny < n){
					if (arr[nx][ny] + cost < dist[nx][ny]){
						dist[nx][ny] = arr[nx][ny] + cost;
						q.offer(new Node(nx, ny, dist[nx][ny]));
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