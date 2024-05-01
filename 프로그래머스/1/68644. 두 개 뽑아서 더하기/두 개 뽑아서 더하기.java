import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> s = new HashSet<Integer>();
        for (int i = 0; i < numbers.length; i ++){
            int tmp = 0;
            for (int j = i + 1; j < numbers.length; j ++){
                tmp = numbers[i] + numbers[j];
                s.add(tmp);
            }
        }
        
        int[] answer = new int[s.size()];
        int idx = 0;
        for(Integer i : s){
            answer[idx++] = i.intValue();
        }
        Arrays.sort(answer);
        
        return answer;
    }
}