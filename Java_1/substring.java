/*substring of a string*/
import java.io.*;
import java.util.*;
public class substring{

	public static void main(String [] args){

		Scanner sc =new Scanner (System.in);

		/*variable declaration*/

		int c;
		String str,sub;

		System.out.println("Enter a string bro:");
		str=sc.nextLine();

		for (c=0; c<str.length(); c++){
			for (int i=1; i<str.length()-c; i++){
				sub=str.substring(c,c+i);
				System.out.println(sub);
			}
		}
	}
}