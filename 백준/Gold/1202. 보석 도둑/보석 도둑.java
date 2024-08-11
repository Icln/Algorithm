import java.util.*;
import java.io.*;

public class Main{
	static int n, k;
	static int[] bags;
	static Jewel[] jewels;

	static class Jewel implements Comparable<Jewel>{
		int weight, value;
		Jewel (int weight, int value){
			this.weight = weight;
			this.value = value;
		}

		@Override
		public int compareTo(Jewel o){
			if (this.weight == o.weight){
				return (this.value - o.value) * -1;
			}
			return this.weight - o.weight;
		}
	}
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		bags = new int[k];
		jewels = new Jewel[n];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			jewels[i] = new Jewel(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		}

		for (int i = 0; i < k; i++) {
			bags[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(bags);
		Arrays.sort(jewels);
		PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
		long answer = 0;
		for (int i = 0, j = 0; i < k; i++) {
			while (j < n && jewels[j].weight <= bags[i]){
				pq.offer(jewels[j++].value);
			}

			if (!pq.isEmpty())
				answer += pq.poll();
			
		}
		System.out.println(answer);
	}
}

