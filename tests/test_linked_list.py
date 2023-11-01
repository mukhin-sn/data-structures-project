"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import *


class TestLinkedList(unittest.TestCase):
    def test_node_class(self):
        node = Node(123, 100)
        self.assertEquals(node.data, 123)
        self.assertEquals(node.next_node, 100)

    def test_insert_beginning(self):
        ll = LinkedList()
        for i in range(3, 0, -1):
            ll.insert_beginning({"xx": i})

        self.assertEquals(str(ll), "{'xx': 1} -> {'xx': 2} -> {'xx': 3} -> None")

    def test_insert_at_end(self):
        ll = LinkedList()
        for i in range(3):
            ll.insert_at_end({"xx": i})

        self.assertEquals(str(ll), "{'xx': 0} -> {'xx': 1} -> {'xx': 2} -> None")
