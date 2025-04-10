import java.util.*;
class Solution {
    static List<String> list = new ArrayList<>();
    static List<Integer> idx = new ArrayList<>();
    static boolean[] visited;

    static void dfs(int cnt, int prev, String[][] tickets, String s){
        if(cnt == tickets.length){ 
            list.add(s + " " + tickets[prev][1]);
            return;
        }
        for(int i = 0; i < tickets.length; i++){
            if(!visited[i] && tickets[prev][1].equals(tickets[i][0])){
                visited[i] = true;
                dfs(cnt + 1, i, tickets, s + " " + tickets[prev][1]);
                visited[i] = false;
            }
        }
    }
    
    public String[] solution(String[][] tickets) {
        for(int i = 0; i < tickets.length; i++){
            if(tickets[i][0].equals("ICN"))
                idx.add(i);
        }
        
        visited = new boolean[tickets.length];
        for(int start: idx){
            visited[start] = true;
            dfs(1, start, tickets, "ICN");
            visited[start] = false;
        }
        
        Collections.sort(list);
        return list.get(0).split(" ");
    }
}