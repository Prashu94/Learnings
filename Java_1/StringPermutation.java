import java.io.*;
import java.util.*;

public class StringPermutation
{
	static String sort(String s){
		char [] c =s.toCharArray();
		Arrays.sort(c);
		return new String(c);
	}
	static boolean permutation(String s, String i){
		if(s.length()!=i.length())
			return false;
		return sort(s).equals(sort(i));
	}
	public static void main(String [] args) throws Exception{
		try(BufferedReader br=new BufferedReader(new InputStreamReader(System.in))){
	
		
		String [] nq=br.readLine().split("\\s");

		String s1=nq[0];
		String s2=nq[1];

			if (permutation(s1,s2)){
			System.out.println("YES");
			}
			else{
			System.out.println("NO");
			}
		}
	}
}