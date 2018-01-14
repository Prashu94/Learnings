import java.io.*;
import java.util.*;

public class FifthProgram
{
	static String compress(String str){
		
		StringBuilder sb = new StringBuilder();
		int countCompress = 0;

		for (int i = 0;i < str.length() ; i++ )
		{
			countCompress++;

			if(i+1 >= str.length() || str.charAt(i) != str.charAt(i+1)){
				sb.append(str.charAt(i));
				sb.append(countCompress);
				countComprsess=0;
			}
		}
		return sb.length() < str.length() ? sb.toString() : str;
	}
	public static void main (String [] args)throws Exception{
	
	}
}