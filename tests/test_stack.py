"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):
    def test_stack(self):
        stack_1 = Stack()
        stack_1.push(24)
        stack_1.push(125)
        stack_1.push(736)

        with self.assertRaises(AttributeError):
            stack_1.top.next_node.next_node.next_node.data

        self.assertEquals(stack_1.top.data, 736)
        self.assertEquals(stack_1.top.next_node.data, 125)
        self.assertEquals(stack_1.pop(), 736)
        self.assertEquals(stack_1.top.data, 125)
        self.assertEquals(stack_1.top.next_node.data, 24)
        self.assertEquals(stack_1.pop(), 125)
        self.assertEquals(stack_1.top.next_node, None)
