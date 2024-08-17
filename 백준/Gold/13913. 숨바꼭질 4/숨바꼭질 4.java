import java.util.*;
import java.io.*;

public class Main{
	static int n, k;
	static int[] parent = new int[100001];
	static int[] visited = new int[100001];

	public static void bfs(){
		ArrayDeque<Integer> q = new ArrayDeque<>();
		visited[n] = 1;
		q.offer(n);
		while (!q.isEmpty()){
			int cur = q.poll();
			if (cur == k)
				return;

			for (int i = 0; i < 3; i++) {
				int next;
				if (i == 0)
					next = cur + 1;
				else if (i == 1)
					next = cur - 1;
				else
					next = cur * 2;

				if (next < 0 || next > 100000)
					continue;

				if (visited[next] == 0) {
					q.add(next);
					visited[next] = visited[cur] + 1;
					parent[next] = cur;
				}
			}


		}
	}

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		bfs();

		Stack<Integer> stack = new Stack<>();
		stack.push(k);
		int num = k;

		while (num != n) {
			stack.push(parent[num]);
			num = parent[num];
		}

		System.out.println(visited[k] - 1);
		while (!stack.isEmpty()) {
			System.out.print(stack.pop() + " ");
		}
	}
}