class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        if not self.head:
            return []

        answer = []
        curr = self.head
        next = 0

        while next is not None:
            answer.append(curr.data)
            next = curr.next

        return answer

    def insertAt(self, pos, newNode): # 요소 삽입
        if pos < 1 or pos > self.nodeCount +1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos-1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1: # 맨 처음, 맨 마지막
            self.tail = newNode

        self.nodeCount +=1 
        return True

    def popAt(self, pos):
        """
        pos가 1일때 self.head = self.head.next
        pos가 마지막일때  self.tail = prev
        유일한 노드를 삭제할 때  유일한 노드 = self.head = 1 , self.tail = 1
        :param pos: 위치
        :return:
        """
        if pos < 1 or pos > self.nodeCount: 
            raise IndexError
        result = 0
        if pos == 1:
            if pos == self.nodeCount: # 유일한 노드
                self.tail = None
            result = self.head.data
            self.head = self.head.next

        else:
            prev = self.getAt(pos-1)
            curr = prev.next
            prev.next = curr.next
            result = curr.data
            if pos == self.nodeCount:
                self.tail = prev

        self.nodeCount -= 1;
        return result




