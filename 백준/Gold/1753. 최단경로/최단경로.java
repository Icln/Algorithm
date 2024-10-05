import java.util.*;
import java.io.*;

class Main{
	static int v, e, k;
	static int[] dist;
	static List<List<Node>> graph;
	static class Node implements Comparable<Node>{
		int to, w;
		public Node(int to, int w){
			this.to = to;
			this.w = w;
		}

		@Override
		public int compareTo(Node o){
			return this.w - o.w;
		}
	}

	public static void bfs(){
		PriorityQueue<Node> q = new PriorityQueue<>();
		q.offer(new Node(k, 0));
		dist[k] = 0;

		while(!q.isEmpty()){
			Node node = q.poll();
			int cur = node.to;
			int cost = node.w;
			if (dist[cur] < cost) continue;

			for (Node next : graph.get(cur)){
				if (next.w + cost < dist[next.to]){
					dist[next.to] = next.w + cost;
					q.offer(new Node(next.to, dist[next.to]));
				}
			}
		}

		for (int i = 1; i <= v; i++)
			System.out.println((dist[i] == Integer.MAX_VALUE) ? "INF" : dist[i]);

	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		v = Integer.parseInt(st.nextToken());
		e = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(br.readLine());

		graph = new ArrayList<>();
		dist = new int[v + 1];
		for (int i = 0; i <= v; i++){
			graph.add(new ArrayList<>());
			dist[i] = Integer.MAX_VALUE;
		}

		for (int i = 0; i < e; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			graph.get(from).add(new Node(to, w));
		}

		bfs();
	}
}