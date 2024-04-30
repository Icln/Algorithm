import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int maxV = 0;
        int maxH = 0;
        for(int i = 0; i < sizes.length; i++){
            int v = Math.max(sizes[i][0], sizes[i][1]);
            int h = Math.min(sizes[i][0], sizes[i][1]);
            maxV = Math.max(maxV, v);
            maxH = Math.max(maxH, h);
        }
        return maxV * maxH;
    }
}