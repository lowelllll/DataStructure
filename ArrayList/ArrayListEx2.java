package basic;

public class ArrayListEx2 {
	public static void main(String[] args) {
		ArrayList list = new ArrayList();
		
		list.addLast(10);
		list.addLast(20);
		list.addLast(30);
		
		list.add(1, 40);
		list.addFirst(0);
		
		System.out.println(list.get(0));
		System.out.println(list.get(1));
		System.out.println(list.get(2));
		System.out.println(list.get(3));
		System.out.println(list.get(4));
		
		System.out.println(list);
		System.out.println(list.indexOf(2330));
	}
}
