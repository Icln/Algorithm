import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        Set<String> usedWords = new HashSet<>();
        for (int i = 0; i < words.length; i++) {
            String current = words[i];
            if (i > 0) {
                String prev = words[i - 1];
                if (prev.charAt(prev.length() - 1) != current.charAt(0)) {
                    return new int[]{(i % n) + 1, (i / n) + 1};
                }
            }

            if (usedWords.contains(current)) {
                return new int[]{(i % n) + 1, (i / n) + 1};
            }
            usedWords.add(current);
        }
        return new int[]{0, 0};
    }
}
