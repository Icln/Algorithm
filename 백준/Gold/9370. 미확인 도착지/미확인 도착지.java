import java.io.*;
import java.util.*;

public class Main {
	static int T, n, m, t, s, g, h, a, b, d, x;
	static int INF = 50000001;
	static int[] dist;
	static List<Integer> answer;
	static List<List<int[]>> graph;
	static PriorityQueue<int[]> q;
	public static int dijkstra(int start, int end) {
		q = new PriorityQueue<>((a, b) -> a[1] - b[1]);
		dist = new int[n + 1];
		Arrays.fill(dist, INF);

		q.offer(new int[]{start, 0});
		dist[start] = 0;
		while (!q.isEmpty()) {
			int[] tmp = q.poll();
			int cur = tmp[0];
			int cost = tmp[1];
			if (dist[cur] < cost) continue;

			for (int[] next : graph.get(cur)) {
				if(cost + next[1] < dist[next[0]] ){
					dist[next[0]] = cost + next[1];
					q.offer(new int[]{next[0], dist[next[0]]});
				}
			}
		}
		return dist[end];
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for (int tc = 0; tc < T; tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			t = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			g = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());

			graph = new ArrayList<>();
			for (int i = 0; i <= n; i++)
				graph.add(new ArrayList<>());

			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				a = Integer.parseInt(st.nextToken());
				b = Integer.parseInt(st.nextToken());
				d = Integer.parseInt(st.nextToken());
				graph.get(a).add(new int[]{b, d});
				graph.get(b).add(new int[]{a, d});
			}

			answer = new ArrayList<>();
			for (int i = 0; i < t; i++) {
				x = Integer.parseInt(br.readLine());
				int tmp1 = dijkstra(s, g) + dijkstra(g, h) + dijkstra(h, x);
				int tmp2 = dijkstra(s, h) + dijkstra(h, g) + dijkstra(g, x);
				int tmp3 = dijkstra(s, x);
				if (Math.min(tmp1, tmp2) == tmp3) answer.add(x);
			}

			Collections.sort(answer);
			for (Integer i : answer) {
				System.out.print(i + " ");
			}
			System.out.println();
		}
	}
}