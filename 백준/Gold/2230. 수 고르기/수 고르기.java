import java.util.*;
import java.io.*;

public class Main {
	static int n, m;
	static int[] arr;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n];
		for (int i = 0; i < n; i++){
			int tmp = Integer.parseInt(br.readLine());
			arr[i] = tmp;
		}
		Arrays.sort(arr);
		int l = 0;
		int r = 0;
		int result = Integer.MAX_VALUE;
		while (r < n){
			int tmp = arr[r] - arr[l];
			if (tmp < m){
				r++;
				continue;
			} else if (tmp == m) {
				result = tmp;
				break;
			}
			else{
				result = Math.min(result, tmp);
				l++;
			}
		}
		System.out.println(result);
	}

}