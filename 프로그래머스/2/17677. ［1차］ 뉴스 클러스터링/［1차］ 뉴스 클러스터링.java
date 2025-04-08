import java.util.*;
class Solution {
    static List<String> a = new ArrayList<>();
    static List<String> b = new ArrayList<>();
    static List<String> inter = new ArrayList<>();
    
    public int solution(String str1, String str2) {
        for(int i = 0; i < str1.length() - 1; i++){
            String tmp = str1.substring(i, i + 2);
            if(tmp.matches("[a-zA-Z]+")){
                a.add(tmp.toUpperCase());
            }
        }
        
        for(int i = 0; i < str2.length() - 1; i++){
            String tmp = str2.substring(i, i + 2);
            if(tmp.matches("[a-zA-Z]+")){
                b.add(tmp.toUpperCase());
            }
        }
        
        if (a.isEmpty() && b.isEmpty()) 
            return 65536;
        for (String s : a) {
            if (b.remove(s)) 
                inter.add(s);
        }
        double d = (double)inter.size() / (double)(a.size() + b.size());
        return (int)(d * 65536.0);
    }
}