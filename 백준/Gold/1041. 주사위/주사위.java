import java.util.*;
import java.io.*;

public class Main {
    private static final int[] side = new int[6];
    private static long[] tmp = new long[3];
    private static int[] min = new int[3];
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<6; i++) side[i] = Integer.parseInt(st.nextToken());

        setMinIdx();

        tmp[0] = 4L;
        tmp[1] = 8L * (N-2) + 4;
        tmp[2] = 5L * (N-2) * (N-2) + 4L * (N-2);

        if(N == 1) {
            Arrays.sort(side);
            System.out.println(side[0] + side[1] + side[2] + side[3] + side[4]);
        } else {
            System.out.println(
                    tmp[0] * (min[0] + min[1] + min[2]) +
                            tmp[1] * (min[0] + min[1]) +
                            tmp[2] * min[0]);
        }
    }

    private static void setMinIdx() {
        min[0] = Math.min(side[0], side[5]);
        min[1] = Math.min(side[1], side[4]);
        min[2] = Math.min(side[2], side[3]);

        Arrays.sort(min);
    }
}