import java.util.*;
import java.io.*;
public class Main {
	static int n, start, end;
	static List<Node> arr = new ArrayList<>();
	static StringTokenizer st;
	private static class Node implements Comparable<Node>{
		int x, y;
		public Node(int x, int y){
			this.x = x;
			this.y = y;
		}

		@Override
		public int compareTo(Node o){
			if (this.x == o.x)
				return Integer.compare(this.y, o.y);
			return Integer.compare(this.x, o.x);
		}

	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++){
			st = new StringTokenizer(br.readLine());
			start = Integer.parseInt(st.nextToken());
			end = Integer.parseInt(st.nextToken());
			arr.add(new Node(start, end));
		}
		Collections.sort(arr);
		PriorityQueue<Integer> q = new PriorityQueue<>();
		q.offer(arr.get(0).y);

		int answer = 1;
		for (int i = 1; i < arr.size(); i++){
			while (!q.isEmpty() && q.peek() <= arr.get(i).x){
				q.poll();
			}
			q.offer(arr.get(i).y);
			answer = Math.max(answer, q.size());
		}
		System.out.println(answer);
	}
}
