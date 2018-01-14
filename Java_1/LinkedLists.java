/*A Simple Java Program to create a linked list and traverse it*/

class LinkedLists
{
	Node head;
	
	/*Linked List node, this inner class is made static so that main class can acces it*/
	static class Node
	{
		int data;
		Node next;
		Node (int d){ data  = d; next =null;}
	}

	/*Adding a node at the front of the linked list*/

	public void push(int newData){
		Node new_node = new Node(newData);

		new_node.next = head;
		head = new_node;
	}

	/*Adding a node after*/

	public void insertAfter(Node prev_node, int newData){
		if(prev_node == null){
			System.out.println("NULL NODE");
			return;
		}
		Node new_node = new Node(newData);

		new_node.next = prev_node.next;
		prev_node.next= new_node;

	}

	/*appending a node*/

	public void append(int newData){
		Node new_node =new Node(newData);

		if(head == null){
			head = new Node(newData);
			return;
		}

		new_node.next = null;
		
		Node last = head;

		while(last.next != null){
			last=last.next;
		}

		last.next= new_node;
		return;
	}
	public void printList(){
		Node n =head;

		while(n!=null){
			System.out.println(n.data+ " ");
			n=n.next;
		}
	}

	public static void main(String [] args){
		LinkedLists iList= new LinkedLists();

		iList.append(6);

		iList.push(5);

		iList.push(4);

		iList.append(1);

		iList.insertAfter(iList.head.next, 8);

		System.out.println("Linked List:");

		iList.printList();
	}
}