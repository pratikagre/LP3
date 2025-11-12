import random

class QuickSort:
    def __init__(self, array):
        self.array = array
    
    # Deterministic partition (last element as pivot)
    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1

        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1
    
    # Randomized partition (random element as pivot)
    def partition_random(self, low, high):
        pivot = random.randint(low, high)
        self.array[pivot], self.array[high] = self.array[high], self.array[pivot]
        return self.partition(low, high)
    
    # Deterministic QuickSort
    def sort_d(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.sort_d(low, pivot - 1)
            self.sort_d(pivot + 1, high)
    
    # Randomized QuickSort
    def sort_r(self, low, high):
        if low < high:
            pivot = self.partition_random(low, high)
            self.sort_r(low, pivot - 1)
            self.sort_r(pivot + 1, high)


# Main program loop
while True:
    print("\nPress Ctrl+C to exit...")
    array = [int(i) for i in input("Enter array: ").split()]
    
    # Deterministic version
    print("\nDeterministic variant of sort:")
    sort1 = QuickSort(array.copy())  # use a copy
    sort1.sort_d(0, len(array) - 1)
    print("Sorted array:", sort1.array)
    
    # Randomized version
    print("\nRandomized variant of sort:")
    sort2 = QuickSort(array.copy())  # use a copy
    sort2.sort_r(0, len(array) - 1)
    print("Sorted array:", sort2.array)
