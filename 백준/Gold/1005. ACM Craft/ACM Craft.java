import java.util.*;
import java.io.*;

public class Main {
	static int t;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		while (t > 0){
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());
			int[] d = new int[n + 1];
			int[] result = new int[n + 1];
			int[] indegree = new int[n + 1];
			List<Integer>[] arr = new ArrayList[n + 1];

			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= n; i++){
				arr[i] = new ArrayList<>();
				d[i] = Integer.parseInt(st.nextToken());
			}

			for (int i = 0; i < k; i++){
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				indegree[b] += 1;
				arr[a].add(b);
			}

			Queue<Integer> q = new LinkedList<>();
			for (int i = 1; i <= n; i++){
				if (indegree[i] == 0) {
					q.add(i);
					result[i] = d[i];
				}
			}

			while (!q.isEmpty()){
				int cur = q.poll();
				for (int node : arr[cur]){
					indegree[node] -= 1;
					result[node] = Math.max(result[node], result[cur] + d[node]);
					if (indegree[node] == 0){
						q.add(node);
					}
				}
			}

			int end = Integer.parseInt(br.readLine());
			System.out.println(result[end]);

			t--;
		}
	}
}