import java.util.*;
import java.io.*;
public class Main {
	static int n, l;
	static List<Pos> arr = new ArrayList<>();
	static StringTokenizer st;

	static class Pos implements Comparable<Pos>{
		int x, y;
		public Pos(int x, int y){
			this.x = x;
			this.y = y;
		}
		@Override
		public int compareTo(Pos p){
			return this.x - p.x;
		}
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		l = Integer.parseInt(st.nextToken());
		for (int i = 0; i < n; i++){
			st = new StringTokenizer(br.readLine());
			arr.add(new Pos(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
		}
		Collections.sort(arr);
		int answer = 0, start = 0;
		for (int i = 0; i < arr.size(); i++) {
			Pos p = arr.get(i);
			for (int j = p.x; j < p.y; j++) {
				if (start < j) {
					start = j + l - 1;
					answer++;
				}
			}
		}
		System.out.println(answer);
	}
}
