import java.util.*;
import java.io.*;

public class Main {
	static long[][] dist;
	static int INF = Integer.MAX_VALUE;
	static int n, m;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		dist = new long[n][n];

		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				if (i != j)
					dist[i][j] = INF;
			}
		}

		for (int i = 0; i < m; i++){
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			dist[a - 1][b - 1] = Math.min(dist[a - 1][b - 1], c);
		}

		for (int k = 0; k < n; k++){
			for (int i = 0; i < n; i++){
				for (int j = 0; j < n; j++){
					dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
				}
			}
		}

		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				if (dist[i][j] == INF)
					dist[i][j] = 0;
				if (j == n - 1)
					System.out.printf("%d\n", dist[i][j]);
				else
					System.out.printf("%d ", dist[i][j]);
			}
		}

	}
}