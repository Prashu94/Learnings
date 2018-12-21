package com.basics.java;
import java.io.*;
import java.util.*;
class Vehicle implements Comparable<Vehicle>{
	int number;
	String name;
	double price;
	public Vehicle(int n ,String name,double price) {
		this.number=n;
		this.name=name;
		this.price=price;
	}
	public int getPostion() {return number;}
	public String getName() {return name;}
	public double getPrice() {return price;}
	@Override
	public int compareTo(Vehicle v) {
		// TODO Auto-generated method stub
		if(v.getPostion()%2==1) {
			return 1;
		}
		else {
			return 0;
		}
	}
}
class PositionCompare implements Comparator<Vehicle>{

	@Override
	public int compare(Vehicle v1, Vehicle v2) {
		// TODO Auto-generated method stub
		if (v1.getPostion() < v2.getPostion()) return -1;
		if (v1.getPostion() > v2.getPostion()) return 1;
		else return 0;
	}
	
}
public class Solution1 {
static int getOddPostion(int n) {
	if (n%2==1) {
		return 1;
	}
	else{
		return 0;
	}
	
}
	public static void main(String[] args)throws Exception {
		// TODO Auto-generated method stub
		try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
			String [] nq = br.readLine().split("\\s");
			ArrayList<Vehicle> list = new ArrayList<Vehicle>();
			int number;
			String name;
			Double price;
			int N = Integer.parseInt(nq[0]);
			
			for (int i = 0; i<N ;i++) {
				number=Integer.parseInt(br.readLine());
				name=br.readLine();
				price=Double.parseDouble(br.readLine());
				list.add(new Vehicle(number,name,price));
			}
			PositionCompare pos = new PositionCompare();
			Collections.sort(list, pos);
			for (Vehicle v : list) {
				int n = v.getPostion();
				if (getOddPostion(n)==1) {
				System.out.println(v.getPostion()+" "+v.getName()+" "+v.getPrice());
				}
			}
					
		}
	}

}
