import java.io.*;
import java.util.*;

public class Main {
	static int n, maxScore;
	static int[][] result;
	static int[] lineUp = new int[9];
	static int[] visited = new int[9];

	public static void permutation(int depth) {
		if (depth == 9) {
			maxScore = Math.max(maxScore, solution(lineUp));
			return;
		}

		if (depth == 3) {
			permutation(depth + 1);
			return;
		}

		for (int i = 1; i < 9; i++) {
			if (visited[i] == 0) {
				lineUp[depth] = i;
				visited[i] = 1;
				permutation(depth + 1);
				visited[i] = 0;
			}
		}
	}

	public static int solution(int[] lineUp) {
		int inning = 0;
		int playerIdx = 0;
		int outCnt = 0;
		int score = 0;
		int[] base = new int[3];

		while (inning < n) {
			int heat = result[inning][lineUp[playerIdx]];
			playerIdx = (playerIdx + 1) % 9;
			if (heat == 0) {
				outCnt += 1;
				if (outCnt == 3) {
					inning += 1;
					outCnt = 0;
					base = new int[3];
				}
			} else {
				for (int i = 2; i >= 0; i--) {
					if (base[i] > 0) {
						if (i + heat > 2)
							score += 1;
						else
							base[i + heat] = base[i];
						base[i] = 0;
					}
				}
				if (heat == 4)
					score += 1;
				else
					base[heat - 1] = 1;
			}
		}
		return score;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		result = new int[n][9];

		StringTokenizer st;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 9; j++)
				result[i][j] = Integer.parseInt(st.nextToken());
		}

		maxScore = 0;
		permutation(0);
		System.out.println(maxScore);
	}
}
