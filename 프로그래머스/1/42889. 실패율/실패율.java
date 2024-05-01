import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        int[][] cnt = new int[2][N + 1];
        for(int stage : stages){
            for (int i = stage; i > 0; i--){
                if(N < i)
                    continue;
                if(i != stage)
                    cnt[0][i]++;
                cnt[1][i]++;
            }
        }
        
        Map<Integer, Double> map = new HashMap<>();

        for (int i = 1; i <= N; i++){
            if (cnt[1][i] == 0){
                map.put(i, 0.0);
            }
            else{
                map.put(i, (double)(cnt[1][i] - cnt[0][i]) / cnt[1][i]);    
            }       
        }
        
        List<Integer> list = new ArrayList<>(map.keySet());
        list.sort((x,y) -> Double.compare(map.get(y), map.get(x)));
        
        return list.stream().mapToInt(i->i).toArray();
    }
}