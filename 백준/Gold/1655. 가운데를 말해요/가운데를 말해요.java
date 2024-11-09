import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
	static PriorityQueue<Integer> minHeap = new PriorityQueue<>();
	static PriorityQueue<Integer> maxHeap = new PriorityQueue<>((o1, o2) -> o2 - o1);

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			int x = Integer.parseInt(br.readLine());
			if (maxHeap.size() == minHeap.size())
				maxHeap.offer(x);
			else
				minHeap.offer(x);
			if (!minHeap.isEmpty() && maxHeap.peek() > minHeap.peek()) {
				minHeap.offer(maxHeap.poll());
				maxHeap.offer(minHeap.poll());
			}
			sb.append(maxHeap.peek()).append("\n");
		}
		System.out.print(sb);
	}
}
