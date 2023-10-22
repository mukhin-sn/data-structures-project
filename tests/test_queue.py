"""Здесь надо написать тесты с использованием unittest для модуля queue."""

import unittest
from src.queue import *


class TestQueue(unittest.TestCase):
    def test_queue(self):
        queue_1 = Queue()
        for i in range(5):
            queue_1.enqueue(f'data{i + 1}')
        self.assertEquals(queue_1.head.data, 'data1')
        self.assertEquals(queue_1.tail.data, 'data5')
        with self.assertRaises(AttributeError):
            queue_1.tail.next_node.date

    def test__str__(self):
        queue_2 = Queue()
        for i in range(5):
            queue_2.enqueue(f'data_{i + 1}')
        self.assertEquals(str(queue_2), 'data_1\ndata_2\ndata_3\ndata_4\ndata_5')
