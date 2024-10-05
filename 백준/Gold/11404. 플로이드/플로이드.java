import java.util.*;
import java.io.*;

class Main{
	static int n, m;
	static long[][] dist;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		dist = new long[n + 1][n + 1];
		for (int i = 1; i <= n; i++) {
			Arrays.fill(dist[i], Integer.MAX_VALUE);
			dist[i][i] = 0;
		}

		for (int i = 0; i < m; i++){
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			dist[a][b] = Math.min(dist[a][b], c);
		}

		for (int k = 1; k < n + 1; k++) {
			for (int i = 1; i < n + 1; i++) {
				for (int j = 1; j < n + 1; j++) {
					dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
				}
			}
		}

		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= n; j++){
				if (dist[i][j] == Integer.MAX_VALUE)
					dist[i][j] = 0;
				if (j == n)
					System.out.printf("%d\n", dist[i][j]);
				else
					System.out.printf("%d ", dist[i][j]);
			}
		}
	}
}