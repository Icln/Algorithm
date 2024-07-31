import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static String[] strings;
    static Map<Character, Integer> map = new HashMap<>();
    static int[] arr = new int[26];
    static class Node implements Comparable<Node> {
        char c;
        int num;
        int word;
        public Node(char c, int num) {
            this.c = c;
            this.num = num;
            this.word = 0;
        }

        @Override
        public int compareTo(Node o) {
            return (num - o.num) * -1;
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        strings = new String[n];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            strings[i] = s;
            for (int j = 0; j < s.length(); j++) {
                arr[s.charAt(j) - 'A'] += (int)Math.pow(10, s.length()- 1 - j);
            }
        }

        List<Node> list = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            if (arr[i] != 0) {
                list.add(new Node((char)('A' + i), arr[i]));
            }
        }

        Collections.sort(list);
        int tmp = 9;
        for (Node n : list) {
            n.word = tmp--;
            map.put(n.c, n.word);
        }

        long answer = 0;
        for (int i = 0; i < n; i++){
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < strings[i].length(); j++) {
                sb.append(map.get(strings[i].charAt(j)));
            }
            answer += Integer.parseInt(String.valueOf(sb));
        }

        System.out.println(answer);
    }
}
