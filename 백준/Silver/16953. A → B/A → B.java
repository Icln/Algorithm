import java.util.*;
import java.io.*;

public class Main {
    static int answer = Integer.MAX_VALUE;
    static long a, b;
    public static void dfs(long num, int cnt){
        if (num == b){
            answer = Math.min(answer, cnt);
            return;
        }
        if (num * 2 <= b)
            dfs(num * 2, cnt + 1);
        if (num * 10 + 1 <= b)
            dfs(num * 10 + 1, cnt + 1);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        dfs(a * 2, 1);
        dfs(a * 10 + 1, 1);

        if (answer == Integer.MAX_VALUE){
            System.out.println(-1);
        }
        else{
            System.out.println(answer + 1);
        }
    }
}
