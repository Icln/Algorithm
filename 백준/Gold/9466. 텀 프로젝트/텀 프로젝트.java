import java.util.*;
import java.io.*;

public class Main{
	static int cnt;
	static int[] arr;
	static boolean[] record, visited;
	private static void dfs(int x){
		if (visited[x]){
			record[x] = true;
			cnt++;
		}
		else
			visited[x] = true;

		if (!record[arr[x]])
			dfs(arr[x]);

		visited[x] = false;
		record[x] = true;
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		while (t > 0){
			int n = Integer.parseInt(br.readLine());
			arr = new int[n + 1];
			record = new boolean[n + 1];
			visited = new boolean[n + 1];
			cnt = 0;

			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= n; i++){
				arr[i] = Integer.parseInt(st.nextToken());
			}

			for (int i = 1; i <= n; i++){
				if (!record[i]){
					dfs(i);
				}
			}

			System.out.println(n - cnt);
			t--;
		}

	}
}