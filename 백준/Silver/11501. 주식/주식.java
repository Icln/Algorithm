import java.util.*;
import java.io.*;

class Main{
	static int t, n;
	static long answer;
	static int[] nums;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for (int i = 0; i < t; i++) {
			n = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			nums = new int[n];
			for (int j = 0; j < n; j++)
				nums[j] = Integer.parseInt(st.nextToken());

			answer = 0;
			int tmp = nums[n - 1];
			for(int j = n - 2; j >= 0; j--){
				if(nums[j] <= tmp)
					answer += tmp - nums[j];
				else
					tmp = nums[j];
			}
			System.out.println(answer);
		}
	}
}