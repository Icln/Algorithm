import java.util.*;
class Solution {
    static List<Integer> idx = new ArrayList<>();
    static List<String> strings = new ArrayList<>();
    static List<String[]> answers = new ArrayList<>();
    static HashMap<String, Integer> map = new HashMap<>();
    static boolean[] visited;
    static int[] order; 
    static int len;

    static void dfs(int cnt, int prev, String[][] tickets){
        if(cnt == len){
            String[] tmp = new String[len + 1]; 
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < len; i++){
                tmp[i] = tickets[order[i]][0];
                sb.append(tmp[i]);
                if(i == len - 1)
                    tmp[i + 1] = tickets[order[i]][1];
            }
            
            map.put(sb.toString(), answers.size());
            strings.add(sb.toString());
            answers.add(tmp);
            return;
        }
        for(int i = 0; i < len; i++){
            if(!visited[i] && tickets[prev][1].equals(tickets[i][0])){
                visited[i] = true;
                order[cnt] = i;
                dfs(cnt + 1, i, tickets);
                visited[i] = false;
            }
        }
    }
    
    public String[] solution(String[][] tickets) {
        len = tickets.length;
        for(int i = 0; i < len; i++){
            if(tickets[i][0].equals("ICN")){
                idx.add(i);
            }
        }
        
        order = new int[len];
        visited = new boolean[len];
        for(int start: idx){
            visited[start] = true;
            order[0] = start;
            dfs(1, start, tickets);
            visited[start] = false;
        }
        Collections.sort(strings);
        return answers.get(map.get(strings.get(0)));
    }
}