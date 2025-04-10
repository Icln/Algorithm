class Solution {
    static boolean[] visited;
    static int answer = Integer.MAX_VALUE;
    static void dfs(String target, String cur, String[] words, int cnt){
        if(cur.equals(target)){
            answer = Math.min(answer, cnt);
            return;
        }
        for(int i = 0; i < words.length; i++){
            if(visited[i]) continue;
            int tmp = 0;
            for(int j = 0; j < cur.length(); j++){
                if(cur.charAt(j) != words[i].charAt(j))
                    tmp++;
            }
            if(tmp != 1) continue;
            visited[i] = true;
            dfs(target, words[i], words, cnt + 1);    
            visited[i] = false;
        }
    }
    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
        dfs(target, begin, words, 0);
        return (answer == Integer.MAX_VALUE) ? 0 : answer;
    }
}