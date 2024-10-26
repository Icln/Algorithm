import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class Main {
	static int answer = 0;
	static boolean[] visited;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int[] people = new int[7];
	static char[][] arr = new char[5][5];
	public static void combination(int depth, int start, int cnt){
		if (depth - cnt > 3) return;
		if (depth == 7){
			bfs(people[0] / 5, people[0] % 5);
			return;
		}

		for (int i = start; i < 25; i++) {
			people[depth] = i;
			combination(depth + 1, i + 1, (arr[i / 5][i % 5] == 'S') ? cnt + 1 : cnt);
		}
	}
	public static void bfs(int x, int y) {
		Queue<int[]> q = new ArrayDeque<>();
		q.offer(new int[]{x, y});
		visited = new boolean[7];
		visited[0] = true;
		int cnt = 1;

		while (!q.isEmpty()) {
			int[] cur = q.poll();
			for (int i = 0; i < 4; i++) {
				int nx = cur[0] + dx[i], ny = cur[1] + dy[i];
				if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5) continue;

				for (int j = 1; j < 7; j++) {
					if (!visited[j] && people[j] == nx * 5 + ny){
						visited[j] = true;
						cnt ++;
						q.offer(new int[]{nx, ny});
					}
				}
			}
		}
		answer = (cnt == 7) ? answer + 1 : answer;
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int i = 0; i < 5; i++) {
			String s = br.readLine();
			for (int j = 0; j < 5; j++) {
				arr[i][j] = s.charAt(j);
			}
		}
		combination(0, 0, 0);
		System.out.println(answer);
	}
}