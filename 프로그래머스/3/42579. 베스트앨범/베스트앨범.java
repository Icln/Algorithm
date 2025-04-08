import java.util.*;
class Solution {
    static HashMap<String, PriorityQueue<Cnt>> songs = new HashMap<>();
    static HashMap<String, Integer> nums = new HashMap<>();
    static List<Genre> order = new ArrayList<>();
    static int len = 0;
    static class Cnt implements Comparable<Cnt>{    
        int play;
        int key;
        
        public Cnt(int play, int key){
            this.play = play;
            this.key = key;
        }
        
        @Override
        public int compareTo(Cnt o){
            if(this.play == o.play)
                return this.key- o.key;
            return -(this.play - o.play);
        }
    }
    
    static class Genre implements Comparable<Genre>{    
        String genre;
        int sum;
        
        public Genre(String genre, int sum){
            this.genre = genre;
            this.sum = sum;
        }
        
        @Override
        public int compareTo(Genre o){
            return -(this.sum - o.sum);
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        for(int i = 0; i < plays.length; i++){
            if(nums.get(genres[i]) == null)
                nums.put(genres[i], plays[i]);
            else
                nums.put(genres[i], nums.get(genres[i]) + plays[i]);
                
            PriorityQueue<Cnt> tmp;
            if(songs.get(genres[i]) == null){
                tmp = new PriorityQueue<>();
                len += 1;    
            }
                
            else{
                tmp = songs.get(genres[i]);
                if(tmp.size() < 2)
                    len += 1;
            }
            tmp.add(new Cnt(plays[i], i));
            songs.put(genres[i], tmp);
        }
        
        for(Map.Entry<String, Integer> entry : nums.entrySet()){
            order.add(new Genre(entry.getKey(), entry.getValue()));
        }
        
        Collections.sort(order);
        int[] answer = new int[len];
        int idx = 0;
        for(Genre g : order){
            PriorityQueue<Cnt> pq = songs.get(g.genre);
            int s = pq.size();
            for(int i = 0; i < s; i++){
                if(i == 2) break;
                Cnt cnt = pq.poll();
                answer[idx ++] = cnt.key;
            }
        }
        return answer;
    }
}

