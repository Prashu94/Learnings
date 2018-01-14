import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;
 
class CodeChef1 {
 
	static PrintWriter writer;
 
	static class FastReader {
		BufferedReader br;
		StringTokenizer st;
 
		FastReader() {
			br = new BufferedReader(new
			                        InputStreamReader(System.in));
		}
 
		FastReader(final InputStream is) {
			if (is != null)
				br = new BufferedReader(new
				                        InputStreamReader(is));
			else new FastReader();
		}
 
		String next() throws IOException {
			while (st == null || !st.hasMoreElements()) {
				st = new StringTokenizer(br.readLine());
			}
			return st.nextToken();
		}
 
		int nextInt() throws IOException {
			return Integer.parseInt(next());
		}
 
		long nextLong() throws IOException {
			return Long.parseLong(next());
		}
 
		double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}
 
		String nextLine() throws IOException {
			return br.readLine();
		}
	}
 
	public static void main (String[] args) throws Exception {
		FastReader reader = new FastReader();
		writer = new PrintWriter(new BufferedOutputStream(System.out));
		int t = reader.nextInt();
		while (t-- > 0) {
			int costR = 0 ;
			int costG = 0 ;
			int n = reader.nextInt();
			int m = reader.nextInt();
			int[][] arr = new int[n][m];
			for (int i = 0 ; i < n; i++) {
				String line = reader.nextLine();
				for (int j = 0; j < m; j++) {
					//R is first
					if ((i + j) % 2 == 0) {
						if (line.charAt(j) == 'G') {
							costR += 3;
						}
					} else {
						if (line.charAt(j) == 'R') {
							costR += 5;
						}
					}
 
					//G is first
					if ((i + j) % 2 == 0) {
						if (line.charAt(j) == 'R') {
							costG += 5;
						}
					} else {
						if (line.charAt(j) == 'G') {
							costG += 3;
						}
					}
 
				}
			}
			if (costG < costR) {
				writer.println(costG);
			} else writer.println(costR);
		}
		writer.close();
	}
}