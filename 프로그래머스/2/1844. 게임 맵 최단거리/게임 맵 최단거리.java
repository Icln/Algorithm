import java.util.*;
class Solution {
    static ArrayDeque<int[]> q = new ArrayDeque<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1}; 
    static int n, m;
    
    static int bfs(int[][] maps){    
        maps[0][0] = 0;
        q.offer(new int[]{0, 0, 1});
        while(!q.isEmpty()){
            int[] cur = q.poll();   
            if(cur[0] == n - 1 && cur[1] == m - 1){
                return cur[2];
            }
            
            for(int i = 0; i < 4; i++){
                int nx = cur[0] + dx[i], ny = cur[1] + dy[i];
                if(nx < 0 || nx >= n || ny < 0 || ny >= m || maps[nx][ny] == 0) continue;
                maps[nx][ny] = 0;
                q.offer(new int[]{nx, ny, cur[2] + 1});
            }
        }
        return -1;
    }
    
    public int solution(int[][] maps) {
        n = maps.length;
        m = maps[0].length;
        return bfs(maps);
    }
}