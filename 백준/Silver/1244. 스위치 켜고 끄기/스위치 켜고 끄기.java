import java.util.*;
import java.io.*;

public class Main {
	static int switchNum, studentNum;
	static int[] status;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		switchNum = Integer.parseInt(br.readLine());
		status = new int[switchNum + 1];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= switchNum; i++){
			status[i] = Integer.parseInt(st.nextToken());
		}

		studentNum = Integer.parseInt(br.readLine());
		for (int i = 0; i < studentNum; i++){
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int n = Integer.parseInt(st.nextToken());
			if (s == 1){
				for (int j = n; j <= switchNum; j += n){
					status[j] = status[j] == 0 ? 1: 0;
				}
			}
			else{
				status[n] = status[n] == 0 ? 1: 0;
				
				for(int j = 1; j <= switchNum / 2; j++) {
					if(n + j > switchNum || n - j <= 0)
						break;
					
					if(status[n - j] == status[n + j]) {
						status[n - j] = status[n - j] == 0 ? 1: 0;
						status[n + j] = status[n + j] == 0 ? 1: 0;
					}
					else break;
				}
			}
		}
		for(int i = 1; i <= switchNum; i++) {
			System.out.print(status[i] + " ");
			if(i % 20 == 0)
				System.out.println();
		}
	}


}