class Solution {
    public int[] solution(long n) {
        String str = String.valueOf(n);
	    int[] answer = new int[str.length()];
	    for(int i= str.length() - 1; i>=0;i--) {
	        answer[str.length()-1-i] = str.charAt(i)-'0';
	    }
	    return answer;
    }
}