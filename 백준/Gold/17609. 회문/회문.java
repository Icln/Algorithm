import java.util.*;
import java.io.*;

public class Main{
	private static boolean check(String[] s, int l, int r){
		while (l < r){
			if (s[l].equals(s[r])){
				l += 1;
				r -= 1;
			}
			else
				return false;
		}
		return true;
	}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		for (int i = 0; i < t; i++){
			String[] s = br.readLine().split("");
			int l = 0;
			int r = s.length - 1;
			int result = 0;
			while (l < r){
				if (s[l].equals(s[r])){
					l += 1;
					r -= 1;
				}
				else {
					if (check(s, l + 1, r) || check(s, l, r - 1)){
						result = 1;
						break;
					}
					else{
						result = 2;
						break;
					}
				}
			}
			System.out.println(result);
		}

	}
}