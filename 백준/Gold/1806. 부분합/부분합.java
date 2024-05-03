import java.util.*;
import java.io.*;

public class Main {
	static int n, s;
	static int[] arr;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		s = Integer.parseInt(st.nextToken());
		arr = new int[n];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++){
			int tmp = Integer.parseInt(st.nextToken());
			arr[i] = tmp;
		}

		int l = 0, r = 0;
		int sum = arr[0];
		int result = Integer.MAX_VALUE;
		while (l <= r && r < n){
			if (sum >= s){
				result = Math.min(result, r - l + 1);
				sum -= arr[l];
				l += 1;
			}
			else{
				r += 1;
				if (r < n)
					sum += arr[r];
			}
		}
		if (result == Integer.MAX_VALUE){
			System.out.println(0);
		}
		else{
			System.out.println(result);
		}
	}
}