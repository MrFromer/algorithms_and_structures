class MinHeap:
    def __init__(self):
        # Инициализация кучи. Куча представлена списком.
        self.heap = []  # Список для хранения элементов кучи

    def insert(self, value):
        """
        Добавляет элемент в кучу и восстанавливает её свойства.
        """
        self.heap.append(value)  # Добавляем элемент в конец списка
        self._sift_up(len(self.heap) - 1)  # Восстанавливаем свойства кучи, начиная с добавленного элемента

    def extract_min(self):
        """
        Извлекает и удаляет минимальный элемент из кучи.
        """
        if not self.heap:
            return None  # Если куча пуста, возвращаем None
        min_value = self.heap[0]  # Минимальный элемент — корень кучи
        last_value = self.heap.pop()  # Удаляем последний элемент из кучи
        if self.heap:
            self.heap[0] = last_value  # Перемещаем последний элемент в корень
            self._sift_down(0)  # Восстанавливаем свойства кучи, начиная с корня
        return min_value  # Возвращаем извлеченный минимальный элемент

    def _sift_up(self, index):
        """
        Восстанавливает свойства кучи, поднимая элемент вверх.
        """
        parent = (index - 1) // 2  # Индекс родителя текущего элемента
        while index > 0 and self.heap[index] < self.heap[parent]:
            # Если текущий элемент меньше родителя, меняем их местами
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent  # Переходим к родителю
            parent = (index - 1) // 2  # Обновляем индекс родителя

    def _sift_down(self, index):
        """
        Восстанавливает свойства кучи, опуская элемент вниз.
        """
        left_child = 2 * index + 1  # Индекс левого потомка
        right_child = 2 * index + 2  # Индекс правого потомка
        smallest = index  # Индекс наименьшего элемента (изначально текущий элемент)

        # Сравниваем текущий элемент с левым потомком
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child  # Левый потомок меньше текущего элемента

        # Сравниваем текущий элемент с правым потомком
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child  # Правый потомок меньше текущего элемента

        # Если наименьший элемент — не текущий, меняем их местами
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)  # Рекурсивно восстанавливаем свойства кучи


def heap_sort(arr):
    """
    Сортирует массив с использованием Min-Heap.
    """
    heap = MinHeap()  # Создаем кучу
    for num in arr:
        heap.insert(num)  # Добавляем все элементы массива в кучу

    sorted_arr = []  # Список для хранения отсортированных элементов
    while heap.heap:
        # Извлекаем минимальный элемент из кучи и добавляем его в результат
        sorted_arr.append(heap.extract_min())
    return sorted_arr  # Возвращаем отсортированный массив


# Основной код
n = int(input())  # Считываем количество элементов в массиве
arr = list(map(int, input().split()))  # Считываем массив чисел

# Сортируем массив с помощью Min-Heap
sorted_arr = heap_sort(arr)

# Выводим отсортированный массив, разделяя элементы пробелами
print(" ".join(map(str, sorted_arr)))