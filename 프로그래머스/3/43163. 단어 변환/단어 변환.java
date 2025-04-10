import java.util.*;
class Solution {
    static ArrayDeque<Word> q = new ArrayDeque<>();
    static class Word{
        String cur;
        int cnt;
        public Word(String cur, int cnt){
            this.cur = cur;
            this.cnt = cnt;
        }
    }
    public int bfs(String begin, String target, String[] words, boolean[] visited){
        
        q.offer(new Word(begin, 0));
        while(!q.isEmpty()){
            Word word = q.poll();
            if(word.cur.equals(target)){
                return word.cnt;
            }
            
            for(int i = 0; i < words.length; i++){
                int tmp = 0;
                if(visited[i]) continue;
                for(int j = 0; j < words[i].length(); j++){
                    if(word.cur.charAt(j) != words[i].charAt(j)){
                        tmp++;
                    }
                }
                if(tmp == 1){
                    visited[i] = true;
                    q.offer(new Word(words[i], word.cnt + 1));
                }   
            }
        }
        
        return 0;
    }
    public int solution(String begin, String target, String[] words) {
        boolean[] visited = new boolean[words.length];
        return bfs(begin, target, words, visited);
    }
}