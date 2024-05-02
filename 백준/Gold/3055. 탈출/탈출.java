import java.util.*;
import java.io.*;

public class Main {
	static int INF = Integer.MAX_VALUE;
	static int r, c;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static Queue<Node> q = new LinkedList<>();

	static Queue<Node> w = new LinkedList<>();
	static boolean[][] visited;
	static char[][] arr;
	static long[][] water;
	static class Node{
		int x, y;
		long cnt;
		public Node(int x, int y, long cnt){
			this.x = x;
			this.y = y;
			this.cnt = cnt;
		}
	}
	private static long bfs(){
		while (!w.isEmpty()){
			Node node = w.poll();
			int x = node.x;
			int y = node.y;

			for (int i = 0; i < 4; i++){
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < r && 0 <= ny && ny < c){
					if (arr[nx][ny] == '.' && water[nx][ny] > water[x][y] + 1){
						water[nx][ny] = water[x][y] + 1;
						w.add(new Node(nx, ny, water[nx][ny]));
					}
				}

			}
		}

		while (!q.isEmpty()){
			Node node = q.poll();
			int x = node.x;
			int y = node.y;
			long cnt = node.cnt;
			if (arr[x][y] == 'D')
				return cnt;

			for (int i = 0; i < 4; i++){
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < r && 0 <= ny && ny < c){
					if (!visited[nx][ny] && (arr[nx][ny] == '.' || arr[nx][ny] == 'D') && (cnt < water[nx][ny])){
						visited[nx][ny] = true;
						q.add(new Node(nx, ny, cnt + 1));
					}
				}

			}
		}
		return -1;
	}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		arr = new char[r][c];
		water = new long[r][c];
		visited = new boolean[r][c];

		for (int i = 0; i < r; i++){
			String[] s = br.readLine().split("");
			for (int j = 0; j < c; j++){
				arr[i][j] = s[j].charAt(0);
				water[i][j] = INF;
				if (arr[i][j] == 'S') {
					q.add(new Node(i, j, 1));
					visited[i][j] = true;
				} else if (arr[i][j] == '*') {
					w.add(new Node(i, j, 0));
					water[i][j] = 0;
				}
			}
		}
		long tmp = bfs();
		if (tmp == -1)
			System.out.println("KAKTUS");
		else
			System.out.println(tmp - 1);
	}
}