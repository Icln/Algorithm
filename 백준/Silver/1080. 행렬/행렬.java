import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	static int n, m;
	static int[][] a, b;

	public static boolean check(){
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				if (a[i][j] != b[i][j])
					return false;
			}
		}
		return true;
	}

	public static void change(int x, int y){
		for (int i = x; i <= x + 2; i++){
			for (int j = y; j <= y + 2; j++){
				a[i][j] = a[i][j] == 1 ? 0 : 1;
			}
		}
	}


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		a = new int[n][m];
		b = new int[n][m];

		for (int i = 0; i < 2; i++){
			for (int j = 0; j < n; j++){
				String tmp = br.readLine();
				for (int k = 0; k < m; k++){
					if (i == 0)
						a[j][k] = tmp.charAt(k) - '0';
					else
						b[j][k] = tmp.charAt(k) - '0';
				}
			}
		}

		if (n < 3 || m < 3) {
			if (check()) 
				System.out.println("0");
			else
				System.out.println("-1");
			return;
		}

		int answer = 0;
		for (int i = 0; i < n - 2; i++) {
			for (int j = 0; j < m - 2; j++) {
				if (a[i][j] != b[i][j]) {
					change(i, j);
					answer++;
				}
			}
		}

		if (!check()) 
			answer = -1;
		System.out.println(answer);
	}
}