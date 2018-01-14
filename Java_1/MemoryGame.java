import java.io.*;

public class MemoryGame{

	public static void main(String [] args)throws Exception{
		try(BufferedReader bf=new BufferedReader(new InputStreamReader(System.in))){

			StringBuilder sb=new StringBuilder();

			String F1=bf.readLine();
			int N=Integer.parseInt(F1);

			/*enter elements of the array*/
			String arr=bf.readLine();
			int [] A2=new int [N];
			int len=arr.length();
			int n=0;
			for (int i=0; i<len; i++){
				A2[n++]=arr.charAt(i);
			}
		}
		
	}
}