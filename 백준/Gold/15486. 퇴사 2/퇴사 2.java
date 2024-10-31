import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int[] t, p, dp;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        t = new int[n + 1];
        p = new int[n + 1];
        dp = new int[n + 1];
        StringTokenizer st;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            t[i + 1] = Integer.parseInt(st.nextToken());
            p[i + 1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= n; i++) {
            dp[i] = Math.max(dp[i], dp[i - 1]);
            int cur = i + t[i] - 1;
            if (cur <= n)
                dp[cur] = Math.max(dp[cur], dp[i - 1] + p[i]);
        }

        System.out.println(dp[n]);
    }
}
