import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        List<Integer> tmp = new ArrayList<Integer>();
        
        for (int i = 0; i < nums.length; i++){
            for (int j = i + 1; j < nums.length; j++){
                if (nums[i] == nums[j])
                    continue;
                for (int k = j + 1; k < nums.length; k++){
                    if (nums[i] == nums[k] || nums[j] == nums[k])
                        continue;
                    tmp.add(nums[i] + nums[j] + nums[k]);
                }
            }
        }
        
        for(Integer n : tmp){
            if(isPrime(n.intValue())){
                answer++;
            }
        }
        
        return answer;
    }
    
    private boolean isPrime(int num){
        for (int i = 2; i <= (int)Math.sqrt(num); i++){
            if(num % i == 0){
                return false;
            }
        }
        return true;
    }
}