class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    data_node = []

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        Queue.data_node = []

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_data = Node(data, None)
        if self.head is None:
            self.head = new_data
            self.tail = self.head
        else:
            self.tail.next_node = new_data
            self.tail = new_data
        Queue.data_node.append(self.tail.data)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""

        if self.tail is None:
            return ""
        else:
            return "\n".join(Queue.data_node)
