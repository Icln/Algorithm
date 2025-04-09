import java.util.*;
class Solution {
    static HashMap<Integer, List<Integer>> map = new HashMap<>();
    static HashMap<String, Integer> language = new HashMap<>();
    static HashMap<String, Integer> position = new HashMap<>();
    static HashMap<String, Integer> history = new HashMap<>();
    static HashMap<String, Integer> food = new HashMap<>();
    static void powerSet(int cnt, int idx, String l, String p, String h, String f, int cur, int score){
        if(cnt == 4){
            List<Integer> scores;
            if(map.get(cur) == null)
                scores = new ArrayList<>();
            else
                scores = map.get(cur);
            scores.add(score);
            map.put(cur, scores);
            return;
        }
        
        if(idx == 0){
            powerSet(cnt + 1, idx + 1, l, p, h, f, cur + language.get(l), score);
            powerSet(cnt + 1, idx + 1, l, p, h, f, cur + language.get("-"), score);    
        }
        else if(idx == 1){
            powerSet(cnt + 1, idx + 1, l, p, h, f, cur + position.get(p), score);
            powerSet(cnt + 1, idx + 1, l, p, h, f, cur + position.get("-"), score);    
        }
        else if(idx == 2){
            powerSet(cnt + 1, idx + 1, l, p, h, f, cur + history.get(h), score);
            powerSet(cnt + 1, idx + 1, l, p, h, f, cur + history.get("-"), score);    
        }
        else {
            powerSet(cnt + 1, idx + 1, l, p, h, f, cur + food.get(f), score);
            powerSet(cnt + 1, idx + 1, l, p, h, f, cur + food.get("-"), score);    
        }
    }
    static int binarySearch(List<Integer> tmp, int score){
        int l = 0, r = tmp.size();
        while(l < r){
            int mid = (l + r) / 2;
            if(tmp.get(mid) < score)
                l = mid + 1;
            else
                r = mid;
        }    
        return tmp.size() - l;
    } 
  
    public int[] solution(String[] info, String[] query) {
        language.put("cpp", 1000);
        language.put("java", 2000);
        language.put("python", 3000);
        language.put("-", 4000);
        
        position.put("backend", 100);
        position.put("frontend", 200);
        position.put("-", 400);
        
        
        history.put("junior", 10);
        history.put("senior", 20);
        history.put("-", 40);
        
        food.put("chicken", 1);
        food.put("pizza", 2);
        food.put("-", 4);
        
        for(String i : info){
            String[] tmp = i.split(" ");
            Integer key = language.get(tmp[0]) + position.get(tmp[1]) + history.get(tmp[2]) + food.get(tmp[3]);
            
            powerSet(0, 0, tmp[0], tmp[1], tmp[2], tmp[3], 0, Integer.parseInt(tmp[4]));        
        }
        
        for (List<Integer> value : map.values()) {
            Collections.sort(value); 
        }
        
        int[] answer = new int[query.length];
        int i = 0;
        for(String q : query){
            String[] condition = q.split(" ");
            Integer tmp = 0;
            tmp += language.get(condition[0]);
            tmp += position.get(condition[2]);
            tmp += history.get(condition[4]);
            tmp += food.get(condition[6]);
            
            if(map.get(tmp) == null){
                answer[i++] = 0;
                continue;
            }
            List<Integer> arr = map.get(tmp);
            answer[i++] = binarySearch(arr, Integer.parseInt(condition[7]));
        }
        return answer;
    }
}