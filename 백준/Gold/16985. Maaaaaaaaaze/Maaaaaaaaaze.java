import java.util.*;
import java.io.*;

public class Main {
    //초기 입력 값을 저장하는 배열
    static int[][][] arr = new int[5][5][5];
    //선택된 판에 따라 최단거리를 탐색하는 배열
    static int[][][] copy = new int[5][5][5];
    //각 판의 회전횟수를 저장하는 배열 
    static int[] rotateCnt = new int[5];

    //bfs 상하동서남북으로 탐색하기 위한 배열
    static int[] dz = {0, 0, 0, 0, 1, -1};
    static int[] dy = {-1, 1, 0, 0, 0, 0};
    static int[] dx = {0, 0, 1, -1, 0, 0};

    //선택된 판(순열)을 구하는 리스트
    static ArrayList<Integer> order = new ArrayList<>();

    //최단거리를 저장하는 변수
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        //25개 줄의 입력을 5개의 5*5배열로 나누어 저장
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < 5; k++) {
                    //최단거리를 저장하기 위해서 사용자가 지나가는 길은 0, 없는길은 max 값으로 변환
                    arr[i][j][k] = Integer.parseInt(st.nextToken());
                    if (arr[i][j][k] == 0) arr[i][j][k] = Integer.MAX_VALUE;
                    else arr[i][j][k] = 0;
                }
            }
        }
        //판의 순서를 선택하는 메서드(순열)
        permutation(0);

        //최솟값이 갱신되지 않았으면 -1, 갱신되었으면 최솟값을 출력
        System.out.println((min == Integer.MAX_VALUE) ? -1 : min);
    }

    /**
     * 판의 순서를 선택하는 메서드(순열)
     * int d: 순열 깊이
     * <p>
     * 기저조건: 깊이가 5면 최솟값을 갱신한다.
     * 1. bfs를 통해서 000 -> 444 까지의 최단경로를 계산한다.
     * 2. 444까지의 경로가 계산된 경우 최솟값과 비교하여 갱신하고 함수를 종료한다.
     * <p>
     * 호출조건
     * 1. 5개의 판에 대해서 방문하지 않은 판을 선택하고
     * 2. 회전 횟수에 따라서 다음 순열을 호출한다.
     * 3. 방문 처리를 취소한다.
     */
    private static void permutation(int d) {
        //기저 조건
        if (d >= 5) {
            bfs();
            if (copy[4][4][4] == 0) return;
            min = Math.min(min, copy[4][4][4]);
            return;
        }
        //호출 조건
        for (int i = 0; i < 5; i++) {
            if (rotateCnt[i] == 0) {
                order.add(i);
                for (int j = 1; j <= 4; j++) {
                    rotateCnt[i] = j;
                    permutation(d + 1);
                }
                order.remove(order.size() - 1);
                rotateCnt[i] = 0;
            }
        }
    }

    /**
     * 000-> 444까지 최단경로를 탐색하는 메서드 (BFS사용)
     * <p>
     * 1. 선택된 순열과 회전횟수만큼 판을 쌓는다.
     * 1.1 회전횟수만큼 rotate 메서드를 호출한다.
     * 2. Queue에 시작지점(0,0,0)을 넣고 bfs를 실행한다.
     * 2.1 (4,4,4)에 도착하거나 queue가 모든 경로를 방문했다면 함수를 종료한다.(시간절약)
     * 2.2 상하동서남북에 대해서 배열범위안에 있고 해당 칸을 이동한적이 없고 이동할 수 있으면
     * 2.3 경로를 갱신하면서 queue에 다시 넣는다.
     */
    private static void bfs() {
        //돌리기
        for (int i = 0; i < 5; i++) {
            copy[i] = rotate(arr[order.get(i)], rotateCnt[i]);
        }

        //copy
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{0, 0, 0});

        if (copy[0][0][0] == Integer.MAX_VALUE) return;

        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            int z = node[0];
            int y = node[1];
            int x = node[2];

            if (z == 4 && y == 4 && x == 4) return;

            for (int i = 0; i < 6; i++) {
                int hz = z + dz[i];
                int hy = y + dy[i];
                int hx = x + dx[i];

                if (check(hz, hy, hx) && copy[hz][hy][hx] == 0) {
                    copy[hz][hy][hx] = copy[z][y][x] + 1;
                    queue.add(new int[]{hz, hy, hx});
                }
            }
        }
    }

    /**
     * 원본 판에서 회전된 판을 반환하는 메서드
     *
     * @param pan 원본 판
     * @param n   회전 횟수
     * @return 회전된 판
     * <p>
     * 1. 회전된 결과를 저장하는 배열 tmp 회전하기 위한 배열 tmp2
     * 2. 깊은 복사를 함
     * 3. 회전 횟수만큼 반시계방향으로 회전
     */
    private static int[][] rotate(int[][] pan, int n) {
        //1. 회전된 결과를 저장하는 배열 tmp 회전하기 위한 배열 tmp2
        int[][] tmp = new int[5][5];
        int[][] tmp2 = new int[5][5];
        //2. 깊은 복사를 함
        for (int i = 0; i < 5; i++) {
            tmp2[i] = pan[i].clone();
        }
        //3. 회전 횟수만큼 반시계방향으로 회전
        for (int a = 0; a < n; a++) {
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    tmp[i][j] = tmp2[j][4 - i];
                }
            }

            for (int i = 0; i < 5; i++) {
                tmp2[i] = tmp[i].clone();
            }
        }
        return tmp;
    }

    /**
     * 좌표가 배열 범위안에 있는지 확인하는 메서드
     *
     * @param z
     * @param y
     * @param x
     * @return
     */
    static boolean check(int z, int y, int x) {
        if (z >= 0 && z < 5 && y >= 0 && y < 5 && x >= 0 && x < 5) {
            return true;
        }
        return false;
    }
}