import java.util.*;
class Solution {
    public String solution(String s) {
        String[] arr = s.split("");
        System.out.println(Arrays.toString(arr));
        Arrays.sort(arr, Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for (String a : arr){
            sb.append(a);
        }
        
        return sb.toString();
    }
}