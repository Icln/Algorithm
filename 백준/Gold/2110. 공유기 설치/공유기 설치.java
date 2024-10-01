import java.util.*;
import java.io.*;

class Main{
	static int n, c, min, max, answer;
	static int[] x;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		x = new int[n];

		for (int i = 0; i < n; i++)
			x[i] = Integer.parseInt(br.readLine());
		Arrays.sort(x);

		min = 1;
		max = x[n - 1] - x[0];
		answer = 0;
		while(min <= max){
			int mid = (min + max) / 2;
			int cur = x[0];
			int cnt = 1;
			for (int i = 1; i < n; i++){
				if (x[i] >= cur + mid){
					cur = x[i];
					cnt += 1;
				}
			}

			if (cnt >= c){
				answer = mid;
				min = mid + 1;
			}
			else
				max = mid - 1;
		}
		System.out.println(answer);
	}
}