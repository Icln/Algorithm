import java.io.*;
import java.util.*;

class Homework implements Comparable<Homework> {
	int idx;
	int deadline;
	int ramen;

	public Homework(int idx, int deadline, int ramen) {
		this.idx = idx;
		this.deadline = deadline;
		this.ramen = ramen;
	}

	@Override
	public int compareTo(Homework o) {
		if(this.deadline == o.deadline) return o.ramen - this.ramen;
		return this.deadline - o.deadline;
	}
}

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int result = 0;
		List<Homework> homeworkList = new ArrayList<>();
		PriorityQueue<Integer> ramens = new PriorityQueue<>();	

		for(int i = 1; i <= n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			homeworkList.add(new Homework(i, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
		}

		Collections.sort(homeworkList);
		for(int i = 0; i < n; i++) {
			Homework tmp = homeworkList.get(i);
			if(ramens.size() < tmp.deadline) ramens.add(tmp.ramen);
			else if(ramens.size() == tmp.deadline) {
				if(ramens.peek() < tmp.ramen) {
					ramens.poll();
					ramens.add(tmp.ramen);
				}
			}
		}

		while(!ramens.isEmpty()) 
			result += ramens.poll();

		System.out.println(result);

	}
}