import java.util.*;
import java.io.*;

public class Main{
	static int n, m ,k;
	static int[][] arr;
	static boolean[][][] visited;
	static int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static class Node{
		int x, y, cnt, wall;
		boolean isNight;

		public Node(int x, int y, int cnt, int wall, boolean isNight) {
			this.x = x;
			this.y = y;
			this.cnt = cnt;
			this.wall = wall;
			this.isNight = isNight;
		}
	}
	public static int bfs(){
		ArrayDeque<Node> q = new ArrayDeque<>();
		q.offer(new Node(0, 0, 1, 0,false));
		visited[0][0][0] = true;
		while (!q.isEmpty()){
			Node tmp = q.poll();
			if (tmp.x == n - 1 && tmp.y == m - 1)
				return tmp.cnt;

			for (int i = 0; i < 4; i++) {
				int nx = tmp.x + d[i][0], ny = tmp.y + d[i][1];
				if (nx < 0 || nx >= n || ny < 0 || ny >= m)
					continue;

				if (arr[nx][ny] == 0 && !visited[tmp.wall][nx][ny]){
					visited[tmp.wall][nx][ny] = true;
					q.offer(new Node(nx, ny, tmp.cnt + 1, tmp.wall, !tmp.isNight));
				}
				else{
					if (!tmp.isNight){
						if (tmp.wall < k && !visited[tmp.wall + 1][nx][ny]){
							visited[tmp.wall + 1][nx][ny] = true;
							q.offer(new Node(nx, ny, tmp.cnt + 1, tmp.wall + 1, !tmp.isNight));
						}
					}
					else{
						if (tmp.wall < k){
							q.offer(new Node(tmp.x, tmp.y, tmp.cnt + 1, tmp.wall, !tmp.isNight));
						}
					}
				}


			}
		}
		return -1;
	}
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		visited = new boolean[k + 1][n][m];

		for (int i = 0; i < n; i++) {
			String s = br.readLine();
			for (int j = 0; j < s.length(); j++) {
				arr[i][j] = s.charAt(j) - '0';
			}
		}

		System.out.println(bfs());
	}
}