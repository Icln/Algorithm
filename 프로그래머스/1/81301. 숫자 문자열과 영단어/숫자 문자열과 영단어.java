import java.util.*;
class Solution {
    public int solution(String s) {
        HashMap<String, String> m = new HashMap<String, String>();
        m.put("zero", "0");
        m.put("one", "1");
        m.put("two", "2");
        m.put("three", "3");
        m.put("four", "4");
        m.put("five", "5");
        m.put("six", "6");
        m.put("seven", "7");
        m.put("eight", "8");
        m.put("nine", "9");
        m.put("0", "0");
        m.put("1", "1");
        m.put("2", "2");
        m.put("3", "3");
        m.put("4", "4");
        m.put("5", "5");
        m.put("6", "6");
        m.put("7", "7");
        m.put("8", "8");
        m.put("9", "9");
        
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            for (int j = s.length() - 1; j >= i ; j--){
                String tmp = s.substring(i, j + 1);
                if (m.containsKey(tmp))
                    sb.append(m.get(tmp));
            }
        }
        
        return Integer.parseInt(sb.toString());
    }
}