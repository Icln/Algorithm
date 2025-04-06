import java.util.*;
class Solution {
    static HashMap<String, Boolean> map = new HashMap<>();
    public int[] solution(int n, String[] words) {
        int idx = 1;
        int cnt = 1;
        int num = 0;
        for(String word : words){
            if(map.get(word) == null){
                map.put(word, true);
                idx ++;
            }
            else{
                return new int[]{idx, cnt};
            }
            
            if(num == 0){
                num += 1;
                continue;
            }
            if(words[num - 1].charAt(words[num - 1].length() - 1) != word.charAt(0)){
                return new int[]{idx - 1, cnt};
            }
            else{
                if(idx > n){
                    idx = 1;
                    cnt += 1;
                }
            }
            num += 1;
        }
        return new int[]{0, 0};
    }
}