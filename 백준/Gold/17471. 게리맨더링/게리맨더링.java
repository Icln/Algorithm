import java.util.*;
import java.io.*;

public class Main{
	static int n, answer = Integer.MAX_VALUE;
	static int[] people;
	static boolean[] visited;
	static List<Node> list = new ArrayList<>();
	static class Node{
		int num;
		List<Integer> arr;
		Node(int num, List<Integer> arr){
			this.num = num;
			this.arr = arr;
		}
	}
	public static void combinations(int[] tmp1, int start, int depth, int r){
		if (depth == r){
			int[] tmp2 = remain(tmp1);
			if (bfs(tmp1) && bfs(tmp2))
				answer = Math.min(answer, cal(tmp1, tmp2));
			return;
		}
		for (int i = start; i < n; i++){
			tmp1[depth] = people[i];
			combinations(tmp1, i + 1, depth + 1, r);
		}
	}

	public static boolean bfs(int[] tmp){
		Queue<Integer> q = new ArrayDeque<>();
		visited = new boolean[n + 1];
		visited[tmp[0]] = true;
		q.offer(tmp[0]);

		while (!q.isEmpty()) {
			int cur = q.poll();
			for (int next : list.get(cur).arr){
				if(!visited[next] && Arrays.stream(tmp).anyMatch(x -> x == next)) {
					visited[next] = true;
					q.offer(next);
				}
			}
		}

		for (int e : tmp){
			if (!visited[e])
				return false;
		}
		return true;
	}


	public static int cal(int[] tmp1, int[] tmp2){
		int a = 0, b = 0;
		for (int i : tmp1){
			a += list.get(i).num;
		}

		for (int i : tmp2){
			b += list.get(i).num;
		}
		return Math.abs(a - b);
	}

	public static int[] remain(int[] tmp){
		int[] tmp2 = new int[n - tmp.length];
		int idx = 0, cnt = 0;
		for (int i = 0; i < n; i++){
			if (people[i] != tmp[cnt]){
				tmp2[idx++] = people[i];
			}
			else{
				if (cnt != tmp.length - 1)
					cnt++;
			}
		}

		return tmp2;
	}


	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine());
		list.add(new Node(0, new ArrayList<>()));
		people = new int[n];

		for (int i = 0; i < n; i++){
			people[i] = i + 1;
			list.add(new Node(Integer.parseInt(st.nextToken()), new ArrayList<>()));
		}


		for (int i = 1; i <= n; i++){
			st = new StringTokenizer(br.readLine());
			int tmp = Integer.parseInt(st.nextToken());
			for (int j = 0; j < tmp; j++){
				list.get(i).arr.add(Integer.parseInt(st.nextToken()));
			}
		}

		for (int i = 0; i < n / 2; i++){
			combinations(new int[i + 1], 0, 0, i + 1);
		}

		answer = (answer == Integer.MAX_VALUE) ? -1 : answer;
		System.out.println(answer);
	}
}