import java.util.*;
import java.io.*;

public class Main {
	static int n, answer = Integer.MIN_VALUE;
	static List<Integer> operand = new ArrayList<>();
	static List<Character> operator = new ArrayList<>();
	public static void dfs(int opNum, int sum) {
		if(opNum >= operator.size()) {
			answer = Math.max(answer, sum);
			return;
		}

		// 1. 괄호 사용 x
		dfs(opNum + 1, cal(opNum, sum, operand.get(opNum + 1)));

		// 2. 괄호 사용
		if(opNum + 1 < operator.size())
			dfs(opNum + 2, cal (opNum, sum, cal (opNum + 1, operand.get(opNum + 1), operand.get(opNum + 2))));

	}
	public static int cal(int idx, int a, int b) {
		switch(operator.get(idx)) {
			case '+':
				return a + b;
			case '-':
				return a - b;
			case '*':
				return a * b;
		}
		return -1;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		String s = br.readLine();
		for (int i = 0; i < n; i++) {
			if (i % 2 == 0)
				operand.add(s.charAt(i) - '0');
			else
				operator.add(s.charAt(i));
		}

		dfs(0, operand.get(0));
		System.out.println(answer);
	}
}
