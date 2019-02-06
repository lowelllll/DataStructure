package prec;

import java.util.LinkedList;
import java.util.Queue;

public class Bfs {
	public static void main(String[] args){
		Graph g = new Graph(8);
		g.addEdge(1, 2);
		g.addEdge(1, 3);
		g.addEdge(1, 4);
		g.addEdge(2, 5);
		g.addEdge(2, 6);
		g.addEdge(3, 5);
		g.addEdge(3, 7);
		g.addEdge(4, 7);
		g.addEdge(4, 8);
		
		g.bfs();
	}
}

class Graph {
	class Node {
		int data;
		LinkedList<Node> adjacent;
		boolean marked;
		
		Node(int data) {
			this.data = data;
			this.adjacent = new LinkedList<Node>();
		}
	}
	
	Node[] nodes;
	int size;
	Graph (int size) {
		nodes = new Node[size];
		this.size = size;
		for(int i = 0; i<size; i++) {
			nodes[i] = new Node(i+1);
		}
	}
	
	void addEdge(int i1, int i2) {
		Node n1 = nodes[i1-1];
		Node n2 = nodes[i2-1];
		
		if(!n1.adjacent.contains(n2)) {
			n1.adjacent.add(n2);
		}
		
		if(!n2.adjacent.contains(n1)) {
			n1.adjacent.add(n1);
		}
	}
	
	void bfs() {
		bfs(0);
	}
	
	void bfs(int index) {
		Node root = nodes[index];
		Queue<Node> queue = new LinkedList<Node>();
		queue.add(root);
		root.marked = true;
		
		while(!queue.isEmpty()) {
			Node r = queue.poll();
			for(Node n:r.adjacent) {
				if(n.marked==false) {
					queue.add(n);
					n.marked=true;
				}
			}
			visit(r);
		}
	}
	
	void visit(Node n) {
		System.out.println(n.data+" ");
	}
}