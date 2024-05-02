import java.util.*;
import java.io.*;

public class Main {
	static int r, c;
	static int er, ec;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static Queue<Node> q = new LinkedList<>();

	static Queue<Node> w = new LinkedList<>();
	static int[][] dist;
	static char[][] arr;
	static class Node{
		int x, y;
		public Node(int x, int y){
			this.x = x;
			this.y = y;
		}
	}
	private static int bfs(){
		while (!q.isEmpty()){
			Node node = q.poll();
			int x = node.x;
			int y = node.y;
			if (x == er && y == ec)
				return dist[x][y];

			for (int i = 0; i < 4; i++){
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < r && 0 <= ny && ny < c){
					if ((arr[nx][ny] == '.' || arr[nx][ny] == 'D') && arr[x][y] == 'S'){
						arr[nx][ny] = 'S';
						dist[nx][ny] = dist[x][y] + 1;
						q.add(new Node(nx, ny));
					}
					else if ((arr[nx][ny] == '.' || arr[nx][ny] == 'S') && arr[x][y] == '*') {
						arr[nx][ny] = '*';
						q.add(new Node(nx, ny));
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
		dist = new int[r][c];

		for (int i = 0; i < r; i++){
			String[] s = br.readLine().split("");
			for (int j = 0; j < c; j++){
				arr[i][j] = s[j].charAt(0);
				if (arr[i][j] == 'S') {
					q.add(new Node(i, j));
				} else if (arr[i][j] == 'D') {
					er = i;
					ec = j;
				}
			}
		}

		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				if (arr[i][j] == '*') {
					q.add(new Node(i, j));
				}
			}
		}

		int result = bfs();
		if (result == -1)
			System.out.println("KAKTUS");
		else
			System.out.println(result);
	}
}