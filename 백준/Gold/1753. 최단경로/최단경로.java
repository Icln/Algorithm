import java.util.*;
import java.io.*;

public class Main {
	static class Node implements Comparable<Node>{
		int cur, cost;
		public Node(int cur, int cost){
			this.cur = cur;
			this.cost = cost;
		}

		@Override
		public int compareTo(Node node){
			return Integer.compare(this.cost, node.cost);
		}
	}
	static int INF = Integer.MAX_VALUE;
	static Queue<Node> q = new PriorityQueue<>();
	static List<Node>[] graph;
	static int[] dist;
	static int v, e, k;

	private static void dijkstra(){
		q.add(new Node(k, 0));
		dist[k] = 0;

		while(!q.isEmpty()){
			Node node = q.poll();
			int cur = node.cur;
			int cost = node.cost;

			if (dist[cur] < cost)
				continue;

			for (Node tmp : graph[cur]){
				int next = tmp.cur;
				if (cost + tmp.cost < dist[next]){
					dist[next] = cost + tmp.cost;
					q.offer(new Node(next, dist[next]));
				}
			}
		}

		for (int i = 1; i <= v; i++){
			if (dist[i] != INF)
				System.out.println(dist[i]);
			else
				System.out.println("INF");
		}
	}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		v = Integer.parseInt(st.nextToken());
		e = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(br.readLine());
		dist = new int[v + 1];
		graph = new ArrayList[v + 1];

		for (int i = 1; i <= v; i ++){
			dist[i] = INF;
			graph[i] = new ArrayList<>();
		}

		for (int i = 0; i < e; i++){
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			graph[a].add(new Node(b, c));
		}

		dijkstra();
	}
}