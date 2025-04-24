import java.util.*;
class Solution {
    static boolean[] nodes;
    public void dfs(int start, int[][] computers, int n){
        for(int i = 0; i < n; i++){
            if(i != start && computers[i][start] == 1){
                if(!nodes[i]){                
                    nodes[i] = true;
                    dfs(i, computers, n);
                }
            }
        }
    }
    public int solution(int n, int[][] computers) {
        nodes = new boolean[n];            
        int answer = 0;
        for(int i = 0; i < n; i++){
            if(!nodes[i]){
                answer++;
                nodes[i] = true;
                dfs(i, computers, n);
            }
                
        }
        return answer;
    }
}