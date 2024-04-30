class Solution {
    boolean solution(String s) {
        int pNum = 0, yNum = 0;
        String[] arr = s.toLowerCase().split("");
        
        for (int i = 0; i < arr.length; i++){
            if ("p".equals(arr[i]))
                pNum++;
            else if ("y".equals(arr[i]))
                yNum++;
        }
        
        if (pNum == yNum)
            return true;
        else
            return false;
    }
}