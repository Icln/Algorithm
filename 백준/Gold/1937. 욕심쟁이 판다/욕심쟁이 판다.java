import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int n, answer;
	static int[][] arr, dp;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static PriorityQueue<Node> pq = new PriorityQueue<>();
	static class Node implements Comparable<Node> {
		int x, y, num;
		public Node(int x, int y, int num) {
			this.x = x;
			this.y = y;
			this.num = num;
		}

		@Override
		public int compareTo(Node o) {
			return -(this.num - o.num);
		}
	}
	public static int solve(){
		while (!pq.isEmpty()) {
			Node cur = pq.poll();
			int x = cur.x;
			int y = cur.y;

			int max = -1;
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
				if (arr[x][y] < arr[nx][ny]) {
					max = Math.max(max, dp[nx][ny] + 1);
				}
			}
			if (max == -1) continue;
			dp[x][y] = max;
			answer = Math.max(answer, dp[x][y]);
		}
		return answer + 1;
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		arr = new int[n][n];
		dp = new int[n][n];

		StringTokenizer st;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				pq.offer(new Node(i, j, arr[i][j]));
			}
		}

		System.out.println(solve());
	}
}