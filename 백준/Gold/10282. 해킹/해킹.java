import java.util.*;
import java.io.*;

public class Main {
	static int INF = Integer.MAX_VALUE;
	static Queue<Node> q = new PriorityQueue<>();
	static List<Node>[] graph;
	static int[] dist;
	static int t;
	static int cnt;

	static class Node implements Comparable<Node>{
		int cur, cost;
		public Node (int cur, int cost){
			this.cur = cur;
			this.cost = cost;
		}

		@Override
		public int compareTo(Node node){
			return Integer.compare(this.cost, node.cost);
		}
	}

	private static void dijkstra(int start){
		q.add(new Node(start, 0));
		dist[start] = 0;

		while (!q.isEmpty()){
			Node node = q.poll();
			int cur = node.cur;
			int cost = node.cost;

			if (dist[cur] < cost)
				continue;

			for (Node tmp: graph[cur]){
				int next = tmp.cur;
				if (cost + tmp.cost < dist[next]){
					if (dist[next] == INF)
						cnt ++;
					dist[next] = cost + tmp.cost;
					q.offer(new Node(next, dist[next]));
				}
			}
		}
	}

	public static void main(String[] args)throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		for (int i = 0; i < t; i++){
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());

			graph = new ArrayList[n + 1];
			dist = new int[n + 1];

			for (int j = 1; j < n + 1; j ++){
				dist[j] = INF;
				graph[j] = new ArrayList<>();
			}

			for (int j = 0; j < d; j++){
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				int s = Integer.parseInt(st.nextToken());

				Node node = new Node(a, s);
				graph[b].add(node);
			}

			cnt = 1;
			dijkstra(c);

			int result = 0;
			for (int j = 1; j < n + 1; j ++){
				if (dist[j] != INF)
					result = Math.max(result, dist[j]);
			}

			System.out.printf("%d %d\n", cnt, result);
		}
	}
}