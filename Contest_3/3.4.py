class MaxHeap:
    def __init__(self):
        """
        Инициализация кучи. Куча представлена списком.
        """
        self.heap = []  # Список для хранения элементов кучи

    def insert(self, value):
        """
        Добавляет элемент в кучу и восстанавливает её свойства.
        """
        self.heap.append(value)  # Добавляем элемент в конец списка
        self._sift_up(len(self.heap) - 1)  # Восстанавливаем свойства кучи, начиная с добавленного элемента

    def extract(self):
        """
        Извлекает и удаляет максимальный элемент из кучи.
        """
        if not self.heap:
            return None  # Если куча пуста, возвращаем None
        max_value = self.heap[0]  # Максимальный элемент — корень кучи
        last_value = self.heap.pop()  # Удаляем последний элемент из кучи
        if self.heap:
            self.heap[0] = last_value  # Перемещаем последний элемент в корень
            self._sift_down(0)  # Восстанавливаем свойства кучи, начиная с корня
        return max_value  # Возвращаем извлеченный максимальный элемент

    def _sift_up(self, index):
        """
        Восстанавливает свойства кучи, поднимая элемент вверх.
        """
        parent = (index - 1) // 2  # Индекс родителя текущего элемента
        while index > 0 and self.heap[index] > self.heap[parent]:
            # Если текущий элемент больше родителя, меняем их местами
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent  # Переходим к родителю
            parent = (index - 1) // 2  # Обновляем индекс родителя

    def _sift_down(self, index):
        """
        Восстанавливает свойства кучи, опуская элемент вниз.
        """
        left_child = 2 * index + 1  # Индекс левого потомка
        right_child = 2 * index + 2  # Индекс правого потомка
        largest = index  # Индекс наибольшего элемента (изначально текущий элемент)

        # Сравниваем текущий элемент с левым потомком
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child  # Левый потомок больше текущего элемента

        # Сравниваем текущий элемент с правым потомком
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child  # Правый потомок больше текущего элемента

        # Если наибольший элемент — не текущий, меняем их местами
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._sift_down(largest)  # Рекурсивно восстанавливаем свойства кучи


# Основной код
n = int(input())  # Считываем количество команд
heap = MaxHeap()  # Создаем кучу

for _ in range(n):
    command = input().split()  # Читаем команду
    if command[0] == '0':
        # Команда Insert: добавляем число в кучу
        value = int(command[1])  # Считываем число
        heap.insert(value)  # Добавляем число в кучу
    else:
        # Команда Extract: извлекаем максимальный элемент из кучи
        max_value = heap.extract()  # Извлекаем максимальный элемент
        print(max_value)  # Выводим извлеченный элемент