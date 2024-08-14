import java.io.*;

public class Main {
	public static void functionU(char op){
		char[] originB = {b[0][0], b[0][1], b[0][2]};
		char[] originR = {r[0][0], r[0][1], r[0][2]};
		char[] originF = {f[0][0], f[0][1], f[0][2]};
		char[] originL = {l[0][0], l[0][1], l[0][2]};
		if (op == '+'){
			u = rotate1(u);
			for (int i = 0; i < 3; i++) {
				b[0][i] = originL[i];
				l[0][i] = originF[i];
				f[0][i] = originR[i];
				r[0][i] = originB[i];
			}
		}
		else{
			u = rotate2(u);
			for (int i = 0; i < 3; i++) {
				b[0][i] = originR[i];
				l[0][i] = originB[i];
				f[0][i] = originL[i];
				r[0][i] = originF[i];
			}
		}
		//U + : B의 윗행 = L의 윗행, L의 윗행 = F의 윗행, F의 윗행 = R의 윗행, R의 윗행 = B의 윗행
		//U - : L의 윗행 = B의 윗행, F의 윗행 = L의 윗행, R의 윗행 = F의 윗행, B의 윗행 = R의 윗행
	}
	public static void functionD(char op){
		char[] originB = {b[2][0], b[2][1], b[2][2]};
		char[] originR = {r[2][0], r[2][1], r[2][2]};
		char[] originF = {f[2][0], f[2][1], f[2][2]};
		char[] originL = {l[2][0], l[2][1], l[2][2]};
		if (op == '+'){
			d = rotate1(d);
			for (int i = 0; i < 3; i++) {
				b[2][i] = originR[i];
				l[2][i] = originB[i];
				f[2][i] = originL[i];
				r[2][i] = originF[i];
			}
		}
		else{
			d = rotate2(d);
			for (int i = 0; i < 3; i++) {
				b[2][i] = originL[i];
				l[2][i] = originF[i];
				f[2][i] = originR[i];
				r[2][i] = originB[i];
			}
		}
		//D + : B의 아래행 = R의 아래행, L의 아래행 = B의 아래행, F의 아래행 = L의 아래행, R의 아래행 = F의 아래행
		//D - : R의 아래행 = B의 아래행, B의 아래행 = L의 아래행, L의 아래행 = F의 아래행, F의 아래행 = R의 아래행
	}
	public static void functionF(char op){
		char[] originU = {u[2][0], u[2][1], u[2][2]};
		char[] originR = {r[0][0], r[1][0], r[2][0]};
		char[] originD = {d[2][0], d[2][1], d[2][2]};
		char[] originL = {l[2][2], l[1][2], l[0][2]};
		if (op == '+'){
			f = rotate1(f);
			for (int i = 0; i < 3; i++) {
				d[2][i] = originR[i];
				u[2][i] = originL[i];
				l[2-i][2] = originD[i];
				r[i][0] = originU[i];
			}
		}
		else{
			f = rotate2(f);
			for (int i = 0; i < 3; i++) {
				d[2][i] = originL[i];
				u[2][i] = originR[i];
				l[2-i][2] = originU[i];
				r[i][0] = originD[i];
			}
		}
		//F + : R의 좌측열 = U의 아래행, D의 아래행 = R의 좌측열, L의 우측열 = D의 아래행, U의 아래행 = L의 우측열
		//F - : U의 아래행 = R의 좌측열, R의 좌측열 = D의 아래행, D의 아래행 = L의 우측열, L의 우측열 = U의 아래행
	}
	public static void functionB(char op){
		char[] originU = {u[0][0], u[0][1], u[0][2]};
		char[] originR = {r[0][2], r[1][2], r[2][2]};
		char[] originD = {d[0][0], d[0][1], d[0][2]};
		char[] originL = {l[2][0], l[1][0], l[0][0]};
		if (op == '+'){
			b = rotate1(b);
			for (int i = 0; i < 3; i++) {
				d[0][i] = originL[i];
				u[0][i] = originR[i];
				l[2-i][0] = originU[i];
				r[i][2] = originD[i];
			}
		}
		else{
			b = rotate2(b);
			for (int i = 0; i < 3; i++) {
				d[0][i] = originR[i];
				u[0][i] = originL[i];
				l[2-i][0] = originD[i];
				r[i][2] = originU[i];
			}
		}
		//B + : U의 윗행 = R의 우측열, L의 좌측열 =  U의 윗행, D의 윗행 = L의 좌측열, R의 우측열 = D의 윗행
		//B - : R의 우측열 = U의 윗행, U의 윗행 = L의 좌측열, L의 좌측열 = D의 윗행, D의 윗행 = R의 우측열
	}
	public static void functionL(char op){
		char[] originU = {u[0][0], u[1][0], u[2][0]};
		char[] originF = {f[0][0], f[1][0], f[2][0]};
		char[] originD = {d[2][2], d[1][2], d[0][2]};
		char[] originB = {b[2][2], b[1][2], b[0][2]};
		if (op == '+'){
			l = rotate1(l);
			for (int i = 0; i < 3; i++) {
				u[i][0] = originB[i];
				f[i][0] = originU[i];
				d[2-i][2] = originF[i];
				b[2-i][2] = originD[i];
			}
		}
		else{
			l = rotate2(l);
			for (int i = 0; i < 3; i++) {
				u[i][0] = originF[i];
				f[i][0] = originD[i];
				d[2-i][2] = originB[i];
				b[2-i][2] = originU[i];
			}
		}
		//L + : U의 좌측열 = B의 우측열, D의 우측열 = F의 좌측열, B의 우측열 = D의 우측열, F의 좌측열 = U의 좌측열
		//L - : B의 우측열 = U의 좌측열, F의 좌측열 = D의 우측열, D의 우측열 = B의 우측열, U의 좌측열 = F의 좌측열
	}
	public static void functionR(char op){
		char[] originU = {u[0][2], u[1][2], u[2][2]};
		char[] originF = {f[0][2], f[1][2], f[2][2]};
		char[] originD = {d[0][0], d[1][0], d[2][0]};
		char[] originB = {b[0][0], b[1][0], b[2][0]};
		if (op == '+'){
			r = rotate1(r);
			for (int i = 0; i < 3; i++) {
				u[i][2] = originF[i];
				f[2-i][2] = originD[i];
				d[i][0] = originB[i];
				b[2-i][0] = originU[i];
			}
		}
		else{
			r = rotate2(r);
			for (int i = 0; i < 3; i++) {
				u[2-i][2] = originB[i];
				f[i][2] = originU[i];
				d[2-i][0] = originF[i];
				b[i][0] = originD[i];
			}
		}
		//R + : U의 우측열 = F의 우측열, F의 우측열 = D의 좌측열, D의 좌측열 = B의 좌측열, B의 좌측열 = U의 우측열
		//R - : F의 우측열 = U의 우측열, D의 좌측열 = F의 우측열, B의 좌측열 = D의 좌측열, U의 우측열 = B의 좌측열
	}
	public static char[][] rotate1(char[][] arr) {
		char[][] tmp = new char[3][3];
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++) {
				tmp[i][j] = arr[2 - j][i];
			}
		}
		return tmp;
	}

	public static char[][] rotate2(char[][] arr) {
		char[][] tmp = new char[3][3];
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++) {
				tmp[i][j] = arr[j][2 - i];
			}
		}
		return tmp;
	}

	public static void printArr(char[][] u){
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				System.out.print(u[i][j]);
			}
			System.out.println();
		}
	}

	static char[][] u;
	static char[][] d;
	static char[][] f;
	static char[][] b;
	static char[][] l;
	static char[][] r;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		for (int i = 0; i < t; i++) {
			u = new char[][]{{'w', 'w', 'w'}, {'w', 'w', 'w'}, {'w', 'w', 'w'}};
			d = new char[][]{{'y', 'y', 'y'}, {'y', 'y', 'y'}, {'y', 'y', 'y'}};
			f = new char[][]{{'r', 'r', 'r'}, {'r', 'r', 'r'}, {'r', 'r', 'r'}};
			b = new char[][]{{'o', 'o', 'o'}, {'o', 'o', 'o'}, {'o', 'o', 'o'}};
			l = new char[][]{{'g', 'g', 'g'}, {'g', 'g', 'g'}, {'g', 'g', 'g'}};
			r = new char[][]{{'b', 'b', 'b'}, {'b', 'b', 'b'}, {'b', 'b', 'b'}};
			int n = Integer.parseInt(br.readLine());
			String s = br.readLine();
			char[] command = new char[2];
			for (int j = 0, idx = 0; j < s.length(); j++) {
				if (s.charAt(j) == ' ')
					continue;
				command[idx++] = s.charAt(j);
				if (idx == 2){
					if (command[0] == 'U')
						functionU(command[1]);
					else if (command[0] == 'D')
						functionD(command[1]);
					else if (command[0] == 'F')
						functionF(command[1]);
					else if (command[0] == 'B')
						functionB(command[1]);
					else if (command[0] == 'L')
						functionL(command[1]);
					else if (command[0] == 'R')
						functionR(command[1]);
					idx = 0;
				}
			}
			printArr(u);
		}
	}
}