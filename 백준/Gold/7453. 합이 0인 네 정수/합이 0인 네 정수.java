import java.util.*;
import java.io.*;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[][] arr = new int[n][4];
		StringTokenizer st;
		for (int i = 0; i < n; i++){
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 4; j++){
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int[] ab = new int[n * n];
		int[] cd = new int[n * n];
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				ab[i * n + j] = arr[i][0] + arr[j][1];
				cd[i * n + j] = arr[i][2] + arr[j][3];
			}
		}

		Arrays.sort(ab);
		Arrays.sort(cd);
		int l = 0;
		int r = n * n - 1;
		long cnt = 0;
		while (l < n * n && r > -1){
			long ba = ab[l], dc = cd[r];
			long sum = ab[l] + cd[r];
			if (sum < 0)
				l += 1;
			else if (sum > 0)
				r -= 1;
			else{
				long tmpA = 0, tmpC = 0;
				while (l < n * n && ab[l] == ba){
					l += 1;
					tmpA += 1;
				}
				while (r > -1 && cd[r] == dc){
					r -= 1;
					tmpC += 1;
				}
				cnt += tmpA * tmpC;
			}
		}

		System.out.println(cnt);


	}
}