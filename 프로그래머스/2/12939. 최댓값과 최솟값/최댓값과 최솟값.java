import java.util.*;
class Solution {
  public String solution(String s) {
      String answer = "";
      ArrayList<Integer> arr = new ArrayList<Integer>();
      String[] tmp = s.split(" ");
 
      for(int i = 0; i < tmp.length; i++) {
          arr.add(Integer.parseInt(tmp[i]));
      }
      answer = "" + Collections.min(arr) + " " + Collections.max(arr);
      return answer;
  }
}