import java.io.*;
import java.util.*;

public class ThirdProgram
{
	static boolean isPermutationoFPalindrome(String phrase){
		int [] table = buildCharFrequencyTable(phrase);
		return checkMaxOneOdd(table);
	}
	static boolean checkMaxOneOdd(int [] table){
		boolean foundOdd=false;

		for (int count : table)
		{
			if(count%2==1){
				if(foundOdd){
					return false;
				}
				foundOdd=true;
			}
		}
	return true;
	}
	/*returns the integer value of the value passed in the argumnet*/
	/*its like you have created an own method for getNumericValue*/
	/*maps each character to a number*/
	static int getCharNumber(Character c){
		int a=Character.getNumericValue('a');
		int z=Character.getNumericValue('z');
		int val=Character.getNumericValue(c);

		if(a<=val && val<=z){
			return val - a;
		}
		return -1;
	}
	static int [] buildCharFrequencyTable(String phrase){
		int [] table = new int[Character.getNumericValue('z')-Character.getNumericValue('a')+1];

		for(char c : phrase.toCharArray()){
			int x = getCharNumber(c);

			if(x!=-1){
				table[x]++;
			}
		}

		return table;
	}
	public static void main(String [] args) throws Exception{
		try(BufferedReader br=new BufferedReader(new InputStreamReader(System.in))){
			/*use this you go away with the privilage of capturing space in the argument as it recognize an split the string into two chracters*/
			String [] nq=br.readLine().split("\\s");

			String s1= nq[0];
			
			System.out.println(isPermutationoFPalindrome(s1));

		}
	}
}