import java.io.*;
import java.util.*;

public class GeeksProgram1{
	static int searchElement(int arr[], int n, int key){
		for (int i=0; i<n; i++){
			if (arr[i]==key){
				return i;
			}
		}
		return -1;
	}
	static int insertElement(int arr [],int n, int key){
		arr[n]=key;
		
		return(n+1);
	}
	static int deleteElement(int arr[], int n, int key){
		int position=searchElement(arr,n,key);
		
		if (position==-1){
			System.out.println("ELEMENT NOT FOUND");
			return n;
		}
		for(int i=position; i<n-1; i++){
			arr[i]=arr[i+1];
		}
		return n-1;
	}
	public static void main(String [] args)throws Exception{
		try(BufferedReader br=new BufferedReader(new InputStreamReader(System.in))){
			int p,d;
			String [] nq=br.readLine().split("\\s");
			
			int N=Integer.parseInt(nq[0]);
			int Q=Integer.parseInt(nq[1]);
			int Q1=Integer.parseInt(nq[2]);
			int Q2=Integer.parseInt(nq[3]);
			
			String str = br.readLine(); 
			String [] s_arr=str.split("\\s");

			int [] A=new int [N+20];
			int len=s_arr.length;
			int i=0;
			for (int n=0; n<len; n++){
				A[i++]=Integer.parseInt(s_arr[n]);
			}
			
			int position= searchElement(A,len,Q);
			
			if(position==-1){
				System.out.println("NOT FOUND");
			}
			else{
				System.out.println("FOUND AT:" +(position+1));
			}
			
			p=insertElement(A,len,Q1);
			
			/*After inserting the element in the array*/
			
			for(int n=0; n<p; n++){
				System.out.print(A[n]+ " ");
			}
			
			/*Deleting an element from the array*/
			d=deleteElement(A,len,Q2);
			System.out.println();
			for (int n=0; n<d; n++){
				System.out.print(A[n]+ " ");
			}
		}
		}
	}


