import unittest
from text_editor_2 import Stack

class TextEditorTest(unittest.TestCase):
    def tests(self):
        text_editor = Stack()

        text_editor.push("type: H")

        self.assertEqual(text_editor.peek(), "type: H")

        text_editor.push("type: e")

        self.assertEqual(text_editor.peek(), "type: e")

        text_editor.push("type: l")

        self.assertEqual(text_editor.peek(), "type: l")

        self.assertEqual(text_editor.pop(), "type: l")
        self.assertEqual(text_editor.peek(), "type: e")

if __name__ == "__main__":
    unittest.main()
