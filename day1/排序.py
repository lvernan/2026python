import random
class Sort:
    def __init__(self,n):
        self.len = n
        self.arr = [0]*n
        self.random_num()

    def random_num(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0,99)

    def quick_sort(self,L,R):
        if L >= R:
            return
        i = L
        j = R
        pivot = self.arr[L]
        while i < j:
            while self.arr[j] >= pivot and i < j:
                j -= 1
            while self.arr[i] <= pivot and i < j:
                i += 1
            if i < j:
                self.arr[j],self.arr[i] = self.arr[i],self.arr[j]
        self.arr[i], self.arr[L] = self.arr[L], self.arr[i]
        self.quick_sort(L,i-1)
        self.quick_sort(i+1,R)

    def heapify(self, i, heap_size):
        while True:
            largest = i
            left = i*2 + 1
            right = i*2 + 2
            if left < heap_size and self.arr[left] > self.arr[largest]:
                largest = left
            if right < heap_size and self.arr[right] > self.arr[largest]:
                largest = right
            if largest == i:
                break
            self.arr[i],self.arr[largest] = self.arr[largest],self.arr[i]
            i = largest

    def dui_sort(self):
        for i in range(self.len // 2 - 1, -1, -1):  #建堆
            self.heapify(i,self.len)
        for end in range(self.len - 1 , 0, -1):
            self.arr[0], self.arr[end] = self.arr[end], self.arr[0]
            self.heapify(0, end)

if __name__ == '__main__':
    sort = Sort(10)
    print(sort.arr)
    # quick.quick_sort(0,9)
    # print(quick.arr)
    sort.dui_sort()
    print(sort.arr)