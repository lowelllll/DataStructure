package basic;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Stack;

import javax.naming.event.ObjectChangeListener;

public class Calc {
	private Object c;
	
	/**
	 * 문자열로 들어온 수식을 ArrayList로 분할합니다.
	 * @param expr
	 * @return 수식을 피연산자,연산자로 분할한 ArrayList
	 */
	private ArrayList splitTokens (String expr) {
		String[] exp = expr.split(""); // String -> String[] 
		ArrayList tokens = new ArrayList();
		int value = 0;
		String op = "";
		boolean flag = false;
		
		for(String c:exp) { // foreach문 (배열,ArrayList)
			if(c.equals(" ")) {
				continue;
			}
			
			if("0123456789".contains(c)) {
				value = value * 10 +  Integer.parseInt(c);
				flag = true;
			}else {
				if(flag) {
					tokens.add(value);
					value = 0;
				}
				flag = false;
				tokens.add(c);
			}
		}
		
		if(flag) {
			tokens.add(value);
		}
		return tokens;
	}
	
	/**
	 * 중위 표기식을 후위 표기식으로 변경합니다
	 * @param tokens 중위 표기식 ArrayList
	 * @return 후위 표기식 ArrayList
	 */
	private ArrayList infixToPostfix(ArrayList tokens) {
		ArrayList result = new ArrayList();
		HashMap<String, Integer> prec = new HashMap<String,Integer>();
		Stack opStack = new Stack();
		
		prec.put("*", 3);
		prec.put("/", 3);
		prec.put("+", 2);
		prec.put("-", 2);
		prec.put("(", 1);
		
		for(Object c:tokens) {
			if(c.equals("(")) {
				opStack.push(c);
			}else if(c.equals(")")) {
				while(!opStack.peek().equals("(")) {
					Object val = opStack.pop();
					if(!val.equals("(")) {
						result.add(val);
					}
				}
				opStack.pop();
			}else if(prec.containsKey(c)) {
				if(opStack.isEmpty()) {
					opStack.push(c);
				}else {
					if(prec.get(opStack.peek()) >= prec.get(c)) {
						result.add(opStack.pop());
						opStack.push(c);
					}else {
						opStack.push(c);
					}
				}
			}else {
				result.add(c);
			}
		}
		
		while(!opStack.isEmpty()) {
			result.add(opStack.pop());
		}
		
		return result;
	}
	
	/**
	 * 후위 표기식을 계산합니다.
	 * @param expr 후위 표기식 ArrayList
	 * @return 최종 계산 결과
	 */
	private int postFixEval(ArrayList expr) {
		Stack<Integer> valueStack = new Stack<Integer>();
		
		for(Object c:expr) {
			if(c instanceof Integer) {
				valueStack.push((Integer) c);
			}else if(c.equals("+")){
				int num1 = valueStack.pop();
				int num2 = valueStack.pop();
				
				valueStack.push(num2+num1);
			}else if(c.equals("-")){
				int num1 = valueStack.pop();
				int num2 = valueStack.pop();
				
				valueStack.push(num2-num1);
			}else if(c.equals("*")){
				int num1 = valueStack.pop();
				int num2 = valueStack.pop();
				
				valueStack.push(num2*num1);
			}else if(c.equals("/")){
				int num1 = valueStack.pop();
				int num2 = valueStack.pop();
				
				valueStack.push(num2/num1);
			}
		}
		
		int result = valueStack.pop();
		return result;
	}
	
	public int process(String expr) {
		ArrayList postfix = infixToPostfix(splitTokens(expr)); // 중위 표기식을 후위 표기식으로 변경
		int result = postFixEval(postfix); // 후위 표기 수식 계산
		return result;
	}
	
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		String expr = sc.nextLine();
		Calc calc = new Calc();
		int result = calc.process(expr);
		System.out.println(result);
	}
}
