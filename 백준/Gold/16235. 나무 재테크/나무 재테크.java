import java.util.*;
import java.io.*;

public class Main {
	static int n, m, k;
	static int[][] field;
	static int[][] a;
	static PriorityQueue<Tree> trees = new PriorityQueue<>();
	static List<Tree> die = new ArrayList<>();
	static int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};

	static class Tree implements Comparable<Tree> {
		int old, x, y;

		public Tree(int old, int x, int y) {
			this.old = old;
			this.x = x;
			this.y = y;
		}

		@Override
		public int compareTo(Tree o) {
			return this.old - o.old;
		}
	}

	public static void spring() {
		PriorityQueue<Tree> tmp = new PriorityQueue<>();
		die.clear();
		while (!trees.isEmpty()) {
			Tree t = trees.poll();
			if (field[t.x][t.y] >= t.old) {
				field[t.x][t.y] -= t.old;
				t.old += 1;
				tmp.add(t);
			} else {
				die.add(t);
			}
		}
		trees = tmp;
	}

	public static void summer() {
		for (Tree t : die) {
			field[t.x][t.y] += (t.old / 2);
		}
	}

	public static void fall() {
		List<Tree> newTrees = new ArrayList<>();
		for (Tree t : trees) {
			if (t.old % 5 == 0) {
				for (int i = 0; i < 8; i++) {
					int nx = t.x + d[i][0], ny = t.y + d[i][1];
					if (nx < 0 || nx >= n || ny < 0 || ny >= n)
						continue;
					newTrees.add(new Tree(1, nx, ny));
				}
			}
		}
		trees.addAll(newTrees);
	}

	public static void winter() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				field[i][j] += a[i][j];
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		a = new int[n][n];
		field = new int[n][n];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				a[i][j] = Integer.parseInt(st.nextToken());
				field[i][j] = 5;
			}
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int z = Integer.parseInt(st.nextToken());
			trees.add(new Tree(z, x - 1, y - 1));
		}

		for (int i = 0; i < k; i++) {
			spring();
			summer();
			fall();
			winter();
		}

		System.out.println(trees.size());
	}
}
