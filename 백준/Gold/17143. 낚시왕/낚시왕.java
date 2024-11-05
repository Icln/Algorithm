import java.io.*;
import java.util.*;

public class Main {
	static int r, c, m, pos, answer;
	static int[][] visited;
	static Map<Integer, Info> shark = new HashMap<>();
	static class Info{
		int x, y, s, d, z;
		Info(int x, int y, int s, int d, int z){
			this.x = x;
			this.y = y;
			this.s = s;
			this.d = d;
			this.z = z;
		}
	}

	public static void fish(int fisher) {
		int sharkSize = 0;
		int sharkPos = Integer.MAX_VALUE;

		for (Info info : shark.values()) {
			if (info.y == fisher && info.x < sharkPos) {
				sharkPos = info.x;
				sharkSize = info.z;
			}
		}

		if (sharkSize > 0) {
			answer += sharkSize;
			shark.remove(sharkSize);
		}
	}

	public static void moveShark(){
		visited = new int[r + 1][c + 1];
		List<Integer> tmp = new ArrayList<>();
		for (Integer i : shark.keySet())
			tmp.add(i);
		
		for (Integer i : tmp) {
			Info info = shark.get(i);
			int dist = info.s;
			int dir = info.d;

			if (dir <= 2) {
				dist %= (2 * (r - 1));
				for (int d = 0; d < dist; d++) {
					if (info.x == 1) dir = 2;
					else if (info.x == r) dir = 1;
					info.x += (dir == 1) ? -1 : 1;
				}
			} else {
				dist %= (2 * (c - 1));
				for (int d = 0; d < dist; d++) {
					if (info.y == 1) dir = 3;
					else if (info.y == c) dir = 4;
					info.y += (dir == 3) ? 1 : -1;
				}
			}

			info.d = dir;

			if (visited[info.x][info.y] == 0) {
				visited[info.x][info.y] = info.z;
				shark.put(info.z, info);
			} else if (visited[info.x][info.y] > info.z) {
				shark.remove(info.z);
			} else if (visited[info.x][info.y] < info.z) {
				shark.remove(visited[info.x][info.y]);
				shark.put(info.z, info);
				visited[info.x][info.y] = info.z;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		for (int i = 1; i <= m; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			int z = Integer.parseInt(st.nextToken());
			shark.put(z, new Info(x, y, s, d, z));
		}

		for (int i = 1; i <= c; i++) {
			fish(i);
			moveShark();
		}

		System.out.println(answer);
	}
}
