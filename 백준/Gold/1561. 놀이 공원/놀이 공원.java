import java.io.*;
import java.util.*;

public class Main {
	static int n, m, child, tmp, remain, idx;
	static long l, r, time;
	static int[] times;
	static boolean check(long mid){
		long cnt = m;
		for (int time : times)
			cnt += mid / time;
		return cnt >= n;
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		times = new int[m];
		for (int i = 0; i < m; i++)
			times[i] = (Integer.parseInt(st.nextToken()));

		if (n <= m){
			System.out.println(n);
			return;
		}

		l = 1;
		r = 60000000000L;
		time = 60000000000L;
		while(l <= r){
			long mid = (l + r) / 2;
			if(check(mid)){
				r = mid - 1;
				time = Math.min(time, mid);
			}
			else
				l = mid + 1;
		}

		time -= 1;
		child = m;
		for (int i = 0; i < m; i++)
			child += time / times[i];
		remain = n - child;
		
		while (true){
			if ((time + 1) / times[idx] != time / times[idx])
				tmp++;
			idx++;
			if (tmp == remain)
				break;
		}
		System.out.println(idx);
	}
}