import java.util.*;
import java.io.*;

public class Main {
	static int[][] arr = new int[10][10];
	static int[] cnt = new int[5];
	static int result = 26;

	private static boolean check(int r, int c, int size) {
		for (int i = r; i <= r + size; i++) {
			for (int j = c; j <= c + size; j++) {
				if (arr[i][j] != 1) {
					return false;
				}
			}
		}
		return true;
	}

	private static void detach(int r, int c, int size) {
		for (int i = r; i <= r + size; i++) {
			for (int j = c; j <= c + size; j++) {
				arr[i][j] = 0;
			}
		}
	}

	private static void attach(int r, int c, int size) {
		for (int i = r; i <= r + size; i++) {
			for (int j = c; j <= c + size; j++) {
				arr[i][j] = 1;
			}
		}
	}

	private static void dfs(int r, int c, int num) {
		if (r >= 10) {
			result = Math.min(result, num);
			return;
		}

		if (c >= 10) {
			dfs(r + 1, 0, num);
			return;
		}

		if (arr[r][c] == 1) {
			for (int size = 0; size < 5; size++) {
				if (r + size < 10 && c + size < 10 && check(r, c, size) && cnt[size] > 0) {
					cnt[size]--;
					detach(r, c, size);
					dfs(r, c + 1, num + 1);
					cnt[size]++;
					attach(r, c, size);
				}
			}
		} else {
			dfs(r, c + 1, num);
		}
	}

	public static void main(String[] args) throws Exception{
		for (int i = 0; i < 5; i++){
			cnt[i] = 5;
		}
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int i = 0; i < 10; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 10; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		dfs(0, 0, 0);
		System.out.println(result != 26 ? result : -1);
	}
}