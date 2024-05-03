import java.util.*;
import java.io.*;

public class Main{

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		int[] arr = new int[n];
		for (int i = 0; i < n; i++){
			int tmp = Integer.parseInt(br.readLine());
			arr[i] = tmp;
		}
		Arrays.sort(arr);

		int start = 1;
		int end = arr[arr.length - 1] - arr[0];
		int result = 0;

		while (start <= end){
			int mid = (start + end) / 2;
			int cur = arr[0];
			int cnt = 1;
			for (int i = 1; i < n; i++){
				if (arr[i] >= cur + mid){
					cur = arr[i];
					cnt += 1;
				}
			}

			if (cnt >= c){
				result = mid;
				start = mid + 1;
			}
			else
				end = mid - 1;
		}
		System.out.println(result);
	}
}