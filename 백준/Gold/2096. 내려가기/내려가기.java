import java.util.*;
import java.io.*;

public class Main {
	static int n;
	static int[][] arr;
	static int[][] dp1;

	static int[][] dp2;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		arr = new int[n][3];
		dp1 = new int[n][3];
		dp2 = new int[n][3];
		for (int i = 0; i < n; i++){
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++){
				int tmp = Integer.parseInt(st.nextToken());
				arr[i][j] = tmp;
			}
		}

		for (int i = 0; i < 3; i++){
			dp1[0][i] = arr[0][i];
			dp2[0][i] = arr[0][i];
		}

		for (int i = 1; i < n; i++){
			for (int j = 0; j < 3; j++){
				if (j == 0){
					dp1[i][j] = arr[i][j] + Math.max(dp1[i - 1][j], dp1[i - 1][j + 1]);
					dp2[i][j] = arr[i][j] + Math.min(dp2[i - 1][j], dp2[i - 1][j + 1]);
				} else if (j == 1) {
					dp1[i][j] = arr[i][j] + Math.max(dp1[i - 1][j - 1], Math.max(dp1[i - 1][j], dp1[i - 1][j + 1]));
					dp2[i][j] = arr[i][j] + Math.min(dp2[i - 1][j - 1], Math.min(dp2[i - 1][j], dp2[i - 1][j + 1]));
				}
				else{
					dp1[i][j] = arr[i][j] + Math.max(dp1[i - 1][j - 1], dp1[i - 1][j]);
					dp2[i][j] = arr[i][j] + Math.min(dp2[i - 1][j - 1], dp2[i - 1][j]);
				}
			}
		}

		int max = -1;
		int min = Integer.MAX_VALUE;
		for (int i = 0; i < 3; i++){
			max = Math.max(max, dp1[n-1][i]);
			min = Math.min(min, dp2[n-1][i]);
		}

		System.out.printf("%d %d\n", max, min);
	}
}