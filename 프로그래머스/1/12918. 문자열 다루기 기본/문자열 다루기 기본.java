class Solution {
    public boolean solution(String s) {
        if (s.length() == 4 || s.length() == 6){
            for (char c: s.toCharArray()){
                if (!Character.isDigit(c))
                    return false;
            }
            return true;
        }
        else
            return false;
        
    }
}