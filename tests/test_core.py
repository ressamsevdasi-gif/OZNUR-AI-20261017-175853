import unittest
from ozcod.core import Sistem, StageResult

class FakeAI:
    def __init__(self):
        self.calls = []
    def generate(self, instruction, text):
        self.calls.append((instruction, text))
        return f"ÇIKTI-{len(self.calls)}"

class CoreTests(unittest.TestCase):
    def test_pipeline_order_and_stage_count(self):
        ai = FakeAI()
        progress = []
        result = Sistem(ai, progress.append).calistir("test girdisi")
        self.assertEqual(result, "ÇIKTI-10")
        self.assertEqual(len(ai.calls), 10)  # İlk insan metni doğrudan aktarılır.
        self.assertEqual([x.number for x in progress], [1,3,5,7,9,11,13,15,17,19,21])
        self.assertEqual(progress[0].value, "test girdisi")
        self.assertEqual(progress[-1].value, "ÇIKTI-10")

    def test_empty_input_rejected(self):
        with self.assertRaises(ValueError):
            Sistem(FakeAI()).calistir("  ")

if __name__ == "__main__":
    unittest.main()
