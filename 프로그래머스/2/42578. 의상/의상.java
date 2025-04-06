import java.util.*;
class Solution {
    static Map<String, Integer> map = new HashMap<>();
    public int solution(String[][] clothes) {
        int answer = 1;
        for (String[] cloth : clothes){
            if(map.get(cloth[1]) == null){
                map.put(cloth[1], 1);
            }
            else{
                map.put(cloth[1], map.get(cloth[1]) + 1);
            }
        }
        
        for (Integer num : map.values()){
            answer *= (num + 1);
        }
        
        return answer - 1;
    }
}