import java.util.*;
class Solution {
    public int[] solution(String[] info, String[] query) {
        Map<String, List<Integer>> scoreMap = new HashMap<>();
        
        for (String applicant : info) {
            String[] data = applicant.split(" ");
            int score = Integer.parseInt(data[4]);
            
            generateCombinations(data, 0, "", scoreMap, score);
        }
        
        for (List<Integer> scores : scoreMap.values()) {
            Collections.sort(scores);
        }
        
        int[] answer = new int[query.length];
        for (int i = 0; i < query.length; i++) {
            String q = query[i].replaceAll(" and ", " ");
            String[] parts = q.split(" ");
            String key = parts[0] + parts[1] + parts[2] + parts[3];
            int targetScore = Integer.parseInt(parts[4]);
            
            List<Integer> scores = scoreMap.getOrDefault(key, new ArrayList<>());
            answer[i] = countScoresAboveThreshold(scores, targetScore);
        }
        
        return answer;
    }
    
    private void generateCombinations(String[] data, int index, String current, Map<String, List<Integer>> scoreMap, int score) {
        if (index == 4) {
            scoreMap.computeIfAbsent(current, k -> new ArrayList<>()).add(score);
            return;
        }
        
        generateCombinations(data, index + 1, current + data[index], scoreMap, score);
        generateCombinations(data, index + 1, current + "-", scoreMap, score);
    }
    
    private int countScoresAboveThreshold(List<Integer> scores, int threshold) {
        if (scores.isEmpty()) return 0;
        
        int left = 0;
        int right = scores.size();
        
        while (left < right) {
            int mid = (left + right) / 2;
            if (scores.get(mid) < threshold) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return scores.size() - left;
    }
}