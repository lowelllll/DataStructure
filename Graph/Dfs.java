package prec;

import java.util.LinkedList;
import java.util.Stack;

class Graph {
	class Node {
		int data;
		LinkedList<Node> adjacent; // 인접한 노드
		boolean marked; // 순회했는지
		
		Node (int data) {
			this.data = data;
			this.marked = false;
			adjacent = new LinkedList<Node>();
		}
	}
	
	Node[] nodes;
	Graph (int size) {
		nodes = new Node[size];
		for (int i = 0; i < size; i++) {
			nodes[i] = new Node(i+1);
		}
	}
	
	void addEdge(int i1, int i2) {
		Node n1 = nodes[i1-1];
		Node n2 = nodes[i2-1];
		
		if (!n1.adjacent.contains(n2)) { // 상대방이 있는지 확인
			n1.adjacent.add(n2);
		}
		
		if (!n2.adjacent.contains(n1)) {
			n2.adjacent.add(n1);
		}
	}
	
	void dfs() {
		dfs(0);
	}
	
	void dfs(int index) { // 스택
		Node root = nodes[index];
		Stack<Node> stack = new Stack<Node>();
		stack.push(root);
		root.marked = true;
		
		while (!stack.isEmpty()) {
			Node r = stack.pop();
			for (Node n:r.adjacent) {
				if (n.marked == false) {
					n.marked = true;
					stack.push(n);
				}
			}
			visit(r);
		}
	}
	
	void dfsR(Node r) { // 재귀
		if (r == null) return;
		r.marked = true;
		visit(r);
		
		for(Node n: r.adjacent) {
			if (n.marked == false) {
				dfsR(n);
			}
		}
	}
	
	void dfsR(int index) {
		Node r = nodes[index];
		dfsR(r);
	}
	
	void dfsR() {
		dfsR(0);
	}
	
	void visit(Node n) { // 출력함수
		System.out.println(n.data + " ");
	}
}

public class Dfs {
	public static void main (String[] args) {
		Graph g = new Graph(7);
		g.addEdge(1, 5);
		g.addEdge(1, 2);
		g.addEdge(2, 4);
		g.addEdge(2, 3);
		g.addEdge(5, 7);
		g.addEdge(5, 6);
		
		g.dfs(); // 1 2 3 4 5 6 7
		// g.dfsR(); 1 5 7 6 2 4 3 
	} 
}
