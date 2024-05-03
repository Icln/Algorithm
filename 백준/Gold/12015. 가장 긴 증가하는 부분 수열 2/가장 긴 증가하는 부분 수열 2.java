import java.util.*;
import java.io.*;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];

		List<Integer> list = new ArrayList<>();
		list.add(0);

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++){
			int value = Integer.parseInt(st.nextToken());
			arr[i] = value;
			if (value > list.get(list.size() - 1))
				list.add(value);
			else{
				int l = 0;
				int r = list.size() - 1;
				while (l < r) {
					int mid = (l + r) / 2;
					if (list.get(mid) < value){
						l = mid + 1;
					}
					else {
						r = mid;
					}
				}
				list.set(r, value);
			}
		}
		System.out.println(list.size() - 1);
	}
}