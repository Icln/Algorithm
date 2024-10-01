import java.util.*;
import java.io.*;

class Main{
	static int k, n;
	static long l, r, answer;
	static long[] len;
	public static boolean check(long mid){
		long cnt = 0;
		for (long tmp : len) {
			cnt += tmp / mid;
		}
		return (cnt >= n) ? true : false;
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		k = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		len = new long[k];

		for (int i = 0; i < k; i++) {
			len[i] = Long.parseLong(br.readLine());
			r = Math.max(r, len[i]);
		}

		l = 1;
		answer = 0;
		while(l <= r){
			long mid = (l + r) / 2;
			if (check(mid)){
				answer = Math.max(answer, mid);
				l = mid + 1;
			}
			else{
				r = mid - 1;
			}
		}
		System.out.println(answer);
	}
}