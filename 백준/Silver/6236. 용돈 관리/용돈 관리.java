import java.util.*;
import java.io.*;

class Main{
	static int n, m;
	static long l, r, answer;
	static int[] days;

	public static boolean check(long mid){
		int cnt = 0;
		long sum = 0;
		for (int day: days){
			if (day + sum > mid){
				sum = 0;
				cnt ++;
			}
			sum += day;
		}
		if (sum > 0) cnt ++;
		return cnt <= m;
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		days = new int[n];
		
		for (int i = 0; i < n; i++) {
			days[i] = Integer.parseInt(br.readLine());
			l = Math.max(l, days[i]);
			r += days[i];
		}

		answer = Integer.MAX_VALUE;
		while(l <= r){
			long mid = (l + r) / 2;
			if (check(mid)){
				r = mid - 1;
				answer = Math.min(answer, mid);
			}
			else{
				l = mid + 1;
			}
		}
		System.out.println(answer);
	}
}