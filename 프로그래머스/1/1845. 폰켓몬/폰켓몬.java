import java.util.*;
class Solution {
    public int solution(int[] nums) {
        Set<Integer> s = new HashSet<Integer>();
        for (int i : nums){
            s.add(i);
        }
        int len = nums.length / 2;
        return len < s.size() ? len: s.size();
    }
}