import java.util.*;
import java.io.*;

public class Main {
    static int n, k, l, time, cur;
    static int[][] arr;
    static Snake snake = new Snake();
    static int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static Map<Integer, Character> map = new LinkedHashMap<>();

    static class Snake{
        int[] head = new int[2];
        LinkedList<int[]> body = new LinkedList<>();
    }

    public static int rotate(int d, char c){
        if (d == 0){
            if (c == 'D')
                return 3;
            else
                return 2;
        }
        else if (d == 1){
            if (c == 'D')
                return 2;
            else
                return 3;
        }
        else if (d == 2){
            if (c == 'D')
                return 0;
            else
                return 1;
        }
        else{
            if (c == 'D')
                return 1;
            else
                return 0;
        }
    }

    public static void eatApple(){
        snake.body.addFirst(new int[]{snake.head[0], snake.head[1]});
        arr[snake.head[0] + d[cur][0]][snake.head[1] + d[cur][1]] = 0;
    }

    public static void move(){
        if (!snake.body.isEmpty()) { // 몸통 이동
            snake.body.addFirst(new int[]{snake.head[0], snake.head[1]});
            snake.body.removeLast();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());
        arr = new int[n][n];
        for (int i = 0; i < k; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[Integer.parseInt(st.nextToken()) - 1][Integer.parseInt(st.nextToken()) - 1] = 1;
        }

        l = Integer.parseInt(br.readLine());
        for (int i = 0; i < l; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            map.put(Integer.parseInt(st.nextToken()), st.nextToken().charAt(0));
        }

        time = 0;
        cur = 3;
        snake.body.clear();

        while(true) {
            time ++;
            if (snake.head[0] + d[cur][0] < 0 || snake.head[0] + d[cur][0] >= n)
                break;

            if (snake.head[1] + d[cur][1] < 0 || snake.head[1] + d[cur][1] >= n)
                break;

            boolean bodyBang = false;
            for (int[] tmp : snake.body) {
                if (tmp[0] == snake.head[0] + d[cur][0] && tmp[1] == snake.head[1] + d[cur][1]) {
                    bodyBang = true;
                    break;
                }
            }
            if (bodyBang)
                break;

            if (arr[snake.head[0] + d[cur][0]][snake.head[1] + d[cur][1]] == 1)
                eatApple();
            else{
                move();
            }
            snake.head[0] += d[cur][0];
            snake.head[1] += d[cur][1];

            if (map.containsKey(time)) {
                cur = rotate(cur, map.get(time));
                map.remove(time);
            }
            
        }
        System.out.println(time);
    }
}
