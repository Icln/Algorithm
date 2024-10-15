import java.io.*;
import java.util.*;

public class Main {
	static int indexBreak, t;
	static long minResult;
	static String maxResult;
	static int[] cnt, store, nonZero;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		t = Integer.parseInt(br.readLine());
		cnt = new int[t];

		for (int tc = 0; tc < t; tc++) {
			minResult = Long.MAX_VALUE;
			indexBreak = 100;

			cnt[tc] = Integer.parseInt(br.readLine());
			store = new int[cnt[tc] / 2];

			//System.out.println(Arrays.toString(cnt));
			//System.out.println(Arrays.toString(store));
			calMin(cnt[tc], 0, 0, 2);
			calMax(cnt[tc]);

			sb.append(minResult).append(" ").append(maxResult).append("\n");
		}

		System.out.println(sb);
	}

	private static void calMax(int num) {
		StringBuilder sb = new StringBuilder();
		if (num % 2 == 0) {
			for (int i = 0; i < num / 2; i++)
				sb.append(1);
		} else {
			sb.append(7);
			num -= 3;
			for (int i = 0; i < num / 2; i++) {
				sb.append(1);
			}
		}
		maxResult = String.valueOf(sb);
	}

	public static void calMin(int num, int index, int sum, int last) {
		if (index > indexBreak)
			return;

		if (sum > num)
			return;

		if (sum == num) {
			indexBreak = index;
			int i = 0;
			for (; i < store.length; i++) {
				if (store[i] == 0)
					break;
			}

			nonZero = new int[i];
			//System.out.println(i);
			for (int j = 0; j < i; j++) {
				nonZero[j] = store[j];
				//System.out.println(Arrays.toString(nonZero));
				if (nonZero[j] == 2) nonZero[j] = 1;
				else if (nonZero[j] == 3) nonZero[j] = 7;
				else if (nonZero[j] == 4) nonZero[j] = 4;
				else if (nonZero[j] == 5) nonZero[j] = 2;
				else if (nonZero[j] == 6) nonZero[j] = 0;
				else if (nonZero[j] == 7) nonZero[j] = 8;
				// System.out.println(Arrays.toString(nonZero));
				// System.out.println();
			}
			Arrays.sort(nonZero);
			if (nonZero[0] == 0) {
				for (int j = 1; j < nonZero.length; j++) {
					if (nonZero[j] != 0 && nonZero[j] < 6) {
						nonZero[0] = nonZero[j];
						nonZero[j] = 0;
						break;
					} else if (nonZero[j] != 0 && nonZero[j] >= 6) {
						nonZero[0] = 6;
						break;
					}
				}
			}

			//System.out.println(Arrays.toString(nonZero));
			long minTemp = 0;
			for (int j = 0; j < nonZero.length; j++) {
				minTemp += nonZero[j] * Math.pow(10, nonZero.length - 1 - j);
			}

			//System.out.println(minTemp);

			if (minTemp < minResult && minTemp != 0) minResult = minTemp; // 최소값 업데이트
			if (minTemp == 0){
				minResult = Math.min(minResult, 6 * (long)Math.pow(10, nonZero.length - 1));
			}
			return;
		}

		if (index >= store.length) {
			return; // 배열 길이를 넘으면 종료
		}

		// 큰 값부터 작은 값으로 탐색하기 위해 for 루프를 역순으로 설정
		for (int j = 7; j >= last; j--) { // 마지막 값보다 큰 값이 아닌, 작은 값부터 추가
			store[index] = j;
			calMin(num, index + 1, sum + j, j); // 다음 숫자 선택 및 합계 증가, 마지막 값 전달
			store[index] = 0; // 백트래킹: 현재 값을 0으로 초기화
		}
	}
}