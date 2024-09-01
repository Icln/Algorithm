import java.util.*;
import java.io.*;
public class Main {
	static int n, m, cnt, answer;
	static int[] parent;
	static int[][] arr;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static List<Node> graph;

	static class Node implements Comparable<Node>{
		int a, b, w;

		public Node(int a, int b, int w) {
			this.a = a;
			this.b = b;
			this.w = w;
		}

		@Override
		public int compareTo(Node o){
			return this.w - o.w;
		}
	}
	public static void islandSet(int x, int y, int num){
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i], ny = y + dy[i];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
			if (arr[nx][ny] == -1){
				arr[nx][ny] = num;
				islandSet(nx, ny, num);
			}
		}
	}

	public static void makeBridge(int x, int y){
		for (int k = 0; k < 4; k++) {
			int nx = x, ny = y, len = 0;
			while(true){
				nx += dx[k];
				ny += dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= m || arr[nx][ny] == arr[x][y]) {
					break;
				}
				if (arr[nx][ny] != 0){
					if (len >= 2) {
						graph.add(new Node(arr[x][y], arr[nx][ny], len));
					}
					break;
				}
				len ++;
			}
		}
	}

	public static int find(int x){
		if (parent[x] == x) return x;
		return parent[x] = find(parent[x]);
	}

	public static boolean union(int x, int y){
		x = find(x);
		y = find(y);
		if (x == y) return false;
		if (x < y) parent[y] = x;
		else parent[x] = y;
		return true;
	}

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		graph = new ArrayList<>();

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 1) arr[i][j] = -1;
			}
		}

		int num = 1;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] == -1){
					arr[i][j] = num;
					islandSet(i, j, num++);
				}
			}
		}

		parent = new int[num];
		for (int i = 0; i < num; i++)
			parent[i] = i;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] != 0)
					makeBridge(i, j);
			}
		}

		Collections.sort(graph);
		cnt = 0;
		answer = 0;
		for (Node node : graph) {
			if (union(node.a, node.b)){
				answer += node.w;
				if (++cnt == num - 1)
					break;
			}
		}

		System.out.println((cnt == num - 2) ? answer : -1);
	}
}