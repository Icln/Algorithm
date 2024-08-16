import java.io.*;
import java.util.*;

public class Solution{
    static ArrayDeque<Integer> arr = new ArrayDeque<>();
    public static void encode(){
        int num = 1;
        while(true){
            int tmp = arr.removeFirst() - num++;
            if (tmp <= 0){
                arr.addLast(0);
                break;
            }
            else
                arr.addLast(tmp);

            if (num == 6)
                num = 1;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 1; i <= 10; i++) {
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr.clear();
            for (int j = 0; j < 8; j++) {
                arr.add(Integer.parseInt(st.nextToken()));
            }
            
            encode();
            System.out.print("#" + i + " ");
            for (Integer num : arr) {
                System.out.printf(num + " ");
            }
            System.out.println();
        }
    }
}