import java.io.*;
import java.util.*;

public class Solution{
	static int n, l, t, answer;
	static int[] score, cal, arr, idx;

	public static boolean np(int num){
		int i = num - 1;
		while (i >= 0 && arr[i] == n - num + i) --i;
		if (i < 0) return false;

		arr[i]++;
		for (int j = i + 1; j < num; j++)
			arr[j] = arr[j - 1] + 1;

		return true;
	}

	public static int getAnswer(int num){
		int tmpCal = 0, tmpScore = 0;
		for (int i = 0; i < num; i++) {
			tmpCal += cal[idx[arr[i]]];
			tmpScore += score[idx[arr[i]]];
		}
		return (tmpCal > l) ? 0 : tmpScore;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= t; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			l = Integer.parseInt(st.nextToken());
			score = new int[n];
			cal = new int[n];
			idx = new int[n];
            answer = 0;
			
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				score[i] = Integer.parseInt(st.nextToken());
				cal[i] = Integer.parseInt(st.nextToken());
			}

			for (int i = 0; i < n; i++)
				idx[i] = i;

			for (int i = 1; i <= n; i++) {
				arr = new int[n];
				for (int j = 0; j < i; j++) 
					arr[j] = j;
				do{
					answer = Math.max(answer, getAnswer(i));
				}while(np(i));
			}
			System.out.println("#" + tc + " " + answer);
		}
	}
}

