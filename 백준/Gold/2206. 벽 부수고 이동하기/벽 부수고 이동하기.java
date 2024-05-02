import java.util.*;
import java.io.*;

public class Main {
	static int n, m;
	static int[][] arr;
	static int[] dx = {-1, 1, 0, 0};

	static int[] dy = {0, 0, -1, 1};
	static boolean[][][] visited;

	static Queue<Node> q = new LinkedList<>();

	static class Node{
		int x, y, z, cnt;
		public Node(int x, int y, int z, int cnt){
			this.x = x;
			this.y = y;
			this.z = z;
			this.cnt = cnt;
		}
	}

	private static int bfs(){
		q.offer(new Node(0,0,1, 1));
		visited[0][0][1] = true;
		while(!q.isEmpty()){
			Node node = q.poll();
			int x = node.x;
			int y = node.y;
			int z = node.z;
			if (x == n - 1 && y == m - 1)
				return node.cnt;

			for (int i = 0; i < 4; i ++){
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < n && 0 <= ny && ny < m){
					if (arr[nx][ny] == 1 && z == 1 && !visited[nx][ny][0]){
						visited[nx][ny][0] = true;
						q.offer(new Node(nx, ny, 0, node.cnt + 1));
					}
					else if (arr[nx][ny] == 0 && !visited[nx][ny][z]){
						visited[nx][ny][z] = true;
						q.offer(new Node(nx, ny, z,node.cnt + 1));
					}
				}
			}
		}
		return -1;
	}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		visited = new boolean[n][m][2];

		for (int i = 0; i < n; i++){
			String[] s = br.readLine().split("");
			for (int j = 0; j < s.length; j++){
				arr[i][j] = Integer.parseInt(s[j]);
			}
		}

		System.out.println(bfs());
	}
}