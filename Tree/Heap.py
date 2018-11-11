# 자료구조 Heap 

class MaxHeap: # 최대 힙

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        """
        느슨한 정렬로 요소 삽입
        :param item: 
        :return: 
        """
        self.data.append(item)
        idx = len(self.data)-1
        parent_idx = idx // 2

        while parent_idx:
            if self.data[idx] > self.data[parent_idx]:
                self.data[idx], self.data[parent_idx] = self.data[parent_idx], self.data[idx]
                idx = parent_idx
                parent_idx = idx // 2
            else:
                break

    def remove(self):
        """
        최대 값을 삭제
        :return:  최대 값
        """
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1) # 최댓값 삭제
            self.max_heapify(1)
        else:
            data = None
        return data

    def max_heapify(self, idx):
        left = idx * 2
        right = (idx * 2)+1
        smallest = idx

        if left < len(self.data) and self.data[left] > self.data[smallest]:
            smallest = left

        if right < len(self.data) and self.data[right] > self.data[smallest]:
            smallest = right

        if smallest != idx: # 현재 idx가 최댓값의 idx가 아니면
            self.data[idx], self.data[smallest] = self.data[smallest], self.data[idx]
            self.max_heapify(smallest)



h = MaxHeap()

h.insert(30)
h.insert(50)
h.insert(20)
h.insert(60)
h.insert(10)
h.insert(4)

h.remove()

print(h.data)