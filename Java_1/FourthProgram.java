import java.io.*;
import.java.util.*;

public class FourthProgram
{
	static boolean oneEditAway(String s1,String s2){
		if(s1.length() == s2.length()){
			return oneReplaceAway(s1,s2);
		}else if(s1.length()+1 == s2.length()){
			return oneInsertAway(s1,s2);
		}else if (s1.length()-1 == s2.length())
		{
			return oneInsertAway(s2,s1);
		}
		return false;
		
	}
	static boolean oneReplaceAway(String s1,String s2){
		boolean foundDifference = false;

		for (int i=0; i < s1.length() ; i++ )
		{
			if(s1.charAt(i) != s2.charAt(i)){
				if (foundDifference)
				{
					return false;
				}
				foundDifference=true;
			}
		}
		return true;
	}
	static boolean oneInsertAway(String s1,String s2){
		int index1 = 0;
		int index2 = 0;
		
		while(index2 < s2.length() && index1 < s1.length()){
			
			if(s1.length() != s2.length()){
				
				if (index1 != index2)
				{
					return false;
				}
				index2++;
			}else{
				index1++;
				index2++;
			}
		}
		return true;
	}
	public static void main(String [] args)throws Exception{
		
	}
}