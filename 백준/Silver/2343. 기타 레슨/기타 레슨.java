import java.util.*;
import java.io.*;

class Main{
	static int n, m, start, end, answer, tmp_answer;
	static int[] size;
	public static boolean check(int mid){
		int cnt = 0;
		int sum = 0;
		for (int i = 0; i < n; i++) {
			if (sum + size[i] > mid){
				sum = 0;
				cnt ++;
			}
			sum += size[i];
		}
		if (sum > 0) cnt++;
		return cnt <= m;
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		size = new int[n];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			size[i] = Integer.parseInt(st.nextToken());
			start = Math.max(start, size[i]);
			end += size[i];
		}
		answer = 0;

		while(start <= end){
			int mid = (start + end) / 2;
			if (check(mid)){
				end = mid - 1;
				answer = mid;
			}
			else
				start = mid + 1;
		}

		System.out.println(answer);
	}
}