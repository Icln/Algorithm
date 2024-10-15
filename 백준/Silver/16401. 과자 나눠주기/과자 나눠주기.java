import java.util.*;
import java.io.*;

public class Main {
    static int m, n, l, r;
    static int[] length;
    public static boolean check(int mid){
        int cnt = 0;
        for (int i : length) {
            cnt += i / mid;
        }
        return cnt >= m;
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        length = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            length[i] = Integer.parseInt(st.nextToken());
            r = Math.max(r, length[i]);
        }

        l = 1;
        int answer = 0;
        while(l <= r){
            int mid = (l + r) / 2;
            if (check(mid)){
                l = mid + 1;
                answer = Math.max(answer, mid);
            }
            else
                r = mid - 1;
        }
        System.out.println(answer);
    }
}
