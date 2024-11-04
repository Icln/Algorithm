import java.io.*;
import java.util.*;

public class Main {
	static int n, m, g, r, answer;
	static int[] red, green;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int[][] arr, visitedR, visitedG;
	static List<Integer> list = new ArrayList<>();
	public static void combinations(int cnt, int idx, char color, HashSet<Integer> set){
		if(color == 'R' && cnt == r){
			combinations(0, 0, 'G', set);
			return;
		}
		else if(color == 'G' && cnt == g){
			bfs();
			return;
		}

		if (color == 'R'){
			for (int i = idx; i < list.size(); i++) {
				red[cnt] = list.get(i);
				set.add(red[cnt]);
				combinations(cnt + 1, i + 1, 'R', set);
				set.remove(red[cnt]);
			}
		}
		else if (color == 'G'){
			for (int i = idx; i < list.size(); i++) {
				if (set.contains(list.get(i))) continue;
				green[cnt] = list.get(i);
				set.add(green[cnt]);
				combinations(cnt + 1, i + 1, 'G', set);
				set.remove(green[cnt]);
			}
		}

	}
	public static void bfs(){
		Queue<int[]> q = new ArrayDeque<>();
		visitedR = new int[n][m];
		visitedG = new int[n][m];
		for (int i = 0; i < r; i++) {
			q.offer(new int[]{1, 0, red[i]});
			visitedR[red[i]/m][red[i]%m] = 1;
		}

		for (int i = 0; i < g; i++){
			q.offer(new int[]{1, 1, green[i]});
			visitedG[green[i]/m][green[i]%m] = 1;
		}

		int cnt = 0;
		while(!q.isEmpty()){
			int[] cur = q.poll();
			int time = cur[0];
			int color = cur[1];
			int x = cur[2] / m;
			int y = cur[2] % m;
			if (visitedR[x][y] == visitedG[x][y])  continue;

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i], ny = y + dy[i];
				if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
				if (arr[nx][ny] == 0) continue;
				if (color == 0){ //  빨강
					if (visitedR[nx][ny] != 0 || visitedG[nx][ny] == 1) continue;
					if (visitedR[nx][ny] == 0 && visitedG[nx][ny] == 0){
						visitedR[nx][ny] = time + 1;
						q.offer(new int[]{time + 1, color, nx * m + ny});
					}
					else if(visitedR[nx][ny] == 0 && visitedG[nx][ny] == time + 1){
						cnt++;
						visitedR[nx][ny] = 1;
						visitedG[nx][ny] = 1;
					}
				}
				else{ // 초록
					if (visitedG[nx][ny] != 0 || visitedR[nx][ny] == 1) continue;
					if (visitedG[nx][ny] == 0 && visitedR[nx][ny] == 0){
						visitedG[nx][ny] = time + 1;
						q.offer(new int[]{time + 1, color, nx * m + ny});
					}
					else if(visitedG[nx][ny] == 0 && visitedR[nx][ny] == time + 1){
						cnt++;
						visitedG[nx][ny] = 1;
						visitedR[nx][ny] = 1;
					}
				}
			}
		}
		answer = Math.max(answer, cnt);
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		g = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		green = new int[g];
		red = new int[r];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 2)
					list.add(i * m + j);
			}
		}

		answer = -1;
		combinations(0, 0, 'R', new HashSet<>());
		System.out.println(answer);
	}
}