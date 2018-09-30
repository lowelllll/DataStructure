package basic;

public class ArrayList {
	private int maxSize = 5;
	private int size = 0;
	private Object[] elementData = new Object[maxSize]; // maxSize개의 데이터를 수용할 수 있음.
	
	public boolean addLast(Object element) { // list 마지막 위치에 데이터 추가하기.
		if (size>=maxSize) {
			System.out.println(size);
			maxSize += 100;
			elementData = resize();
			this.addLast(element);
		} else {
			elementData[size] = element;
			size++;
		}
		return true;
	}
	
	public Object[] resize() {
		Object[] newElementData = new Object[maxSize];
		for(int i=0; i<size; i++) {
			if(elementData[i]!=null) {
				newElementData[i] = elementData[i];
			}
		}
		return newElementData;
	}
	
	public boolean add(int index,Object element) {
		if (size>=maxSize) {
			maxSize += 100;
			elementData = resize();
			this.add(index,element);
		} else {
			for(int i=size;i>index;i--) {
				elementData[i] = elementData[i-1];
			}
			
			elementData[index] = element;
			size++;
		}
		return true;
	}
	
	public boolean addFirst(Object element) {
		return add(0, element);
	}
	
	public Object get(int index) {
		return elementData[index]; // ArrayList의 장점! 겁나 빠름~!
	}
	
	public String toString() { // 객체를 문자열로 출력해야할 경우, 이 함수가 호출됨.
		String str = "[";
		for(int i=0; i<size; i++) {
			str += elementData[i];
			if(i < size-1) {
				str += ",";
			}
		}
		return str+"]"; // 리스트의 전체 내용을 출력.
	}
	
	public int size() { // 리스트의 길이 호출.
		return size;
	}
	
	public int indexOf(Object element) { // element값이 존재하면 위치해있는 인덱스를 반환.
		for(int i=0; i<size; i++) {
			if(elementData[i].equals(element)) {
				return i;
			}
		}
		return -1;
	}
	
	public boolean remove(int index) {
		elementData[index] = null;
		for(int i=index;i<size-1;i++) {
			elementData[i] = elementData[i+1];
		}
		if(size<1) {
			elementData[size-1] = null;
		}
		size--;
		return true;
	}
}
