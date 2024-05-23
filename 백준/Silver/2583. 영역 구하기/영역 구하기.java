import java.io.*;
import java.util.*;

public class Main {
	static final int dx[] = {0, 0, 1, -1};
	static final int dy[] = {1, -1, 0, 0};
	static int n,m,count;
	static int square[][];
	
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		square = new int[n][m];
		
		for(int i=0; i<k; i++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			
			for(int y=y1; y<y2; y++) { 
				for(int x=x1; x<x2; x++){ 
					square[y][x] = 1;
				}
			}
		}
		
		ArrayList<Integer> areaCount = new ArrayList<>();
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(square[i][j] == 0) {
					count = 0; 
					dfs(i,j);
					areaCount.add(count);
				}
			}
		}
		
		Collections.sort(areaCount); 
		sb.append(areaCount.size()).append('\n'); 
		for(int i : areaCount)  {
			sb.append(i + " ");
		}
		
		System.out.println(sb);
	}
	
	static void dfs(int x, int y) {
		square[x][y] = 1;
		count ++; 
		
		for(int k=0; k<4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			
			if(0<=nx && nx<n && 0<=ny && ny < m) {
				if(square[nx][ny] == 0) {
					dfs(nx,ny);
				}
			}
		}
	}

}