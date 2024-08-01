import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int t;
	static StringTokenizer st;
	static class Score implements Comparable<Score>{
		int first, second;
		public Score(int first, int second){
			this.first = first;
			this.second = second;
		}

		@Override
		public int compareTo(Score o){
			return second - o.second;
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		while(t-- > 0){
			int n = Integer.parseInt(br.readLine());
			List<Score> arr = new ArrayList<>();
			for (int i = 0; i < n; i++){
				st = new StringTokenizer(br.readLine());
				arr.add(new Score(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
			}
			Collections.sort(arr);
			int answer = 1;
			int s1 = arr.get(0).first, s2 = arr.get(0).second;
			for (int i = 1; i < arr.size(); i++){
				int tmp1 = arr.get(i).first, tmp2 = arr.get(i).second;
				if (tmp1 < s1 || tmp2 < s2){
					answer++;
					s1 = Math.min(s1, tmp1);
					s2 = Math.min(s2, tmp2);
				}
			}
			System.out.println(answer);
		}
	}

}