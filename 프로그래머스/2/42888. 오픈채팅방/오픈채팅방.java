import java.util.*;
class Solution {
    static HashMap<String, String> name = new HashMap<>();
    static List<String[]> orders = new ArrayList<>();
    public String[] solution(String[] record) {
        for(String r : record){
            String[] tmp = r.split(" ");
            if(tmp[0].equals("Leave")){
                orders.add(new String[]{tmp[1], "님이 나갔습니다."});
            }
            else if(tmp[0].equals("Change")){
                name.put(tmp[1], tmp[2]);
            }
            else{
                if(name.get(tmp[1]) == null)
                    name.put(tmp[1], tmp[2]);    
                else
                    name.put(tmp[1], tmp[2]);
                orders.add(new String[]{tmp[1], "님이 들어왔습니다."});
            }
        }
        
        String[] answer = new String[orders.size()];
        int i = 0;
        for(String[] order: orders){
            answer[i++] = name.get(order[0]) + order[1];
        }
        return answer;
    }
}