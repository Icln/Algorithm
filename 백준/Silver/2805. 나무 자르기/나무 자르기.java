import java.util.*;
import java.io.*;

class Main{
	static int n, m, l, r, h;
	static int[] trees;
	public static boolean check(int h){
		long sum = 0;
		for (int tree : trees) {
			int tmp = tree - h;
			if (tmp > 0)
				sum += tmp;
		}
		return (sum >= m) ? true: false;
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		trees = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			trees[i] = Integer.parseInt(st.nextToken());
			r = Math.max(r, trees[i]);
		}

		l = 1;
		h = 0;
		while(l <= r){
			int mid = (l + r) / 2;
			if (check(mid)){
				h = Math.max(h, mid);
				l = mid + 1;
			}
			else{
				r = mid - 1;
			}
		}
		System.out.println(h);
	}
}