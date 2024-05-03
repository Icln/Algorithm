import java.util.*;
import java.io.*;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i ++){
			arr[i] = Integer.parseInt(st.nextToken());
		}

		Arrays.sort(arr);
		int l = 0;
		int r = n - 1;
		int min = Integer.MAX_VALUE;
		int[] result = {0, 0};
		while (l < r){
			int sum = arr[l] + arr[r];
			if (Math.abs(sum) < min){
				min = Math.abs(sum);
				result[0] = arr[l];
				result[1] = arr[r];
				if (sum == 0){
					break;
				}
			}
			if (sum < 0)
				l+= 1;
			else
				r -= 1;
		}
		System.out.println(result[0] + " " + result[1]);
	}

}