import unittest
from call_center_4 import Call, CallCenter

class CallCenterTests(unittest.TestCase):
    def tests(self):
        callCenter = CallCenter()

        callCenter.add_call(Call("123", "20:00"))
        callCenter.add_call(Call("321", "20:01"))

        self.assertEqual(callCenter.incoming_calls.peek().caller_id, "123")
        
        callCenter.process_call()

        self.assertEqual(callCenter.processed_calls.peek().caller_id, "123")
        self.assertEqual(callCenter.incoming_calls.peek().caller_id, "321")

        callCenter.process_call()

        self.assertEqual(callCenter.processed_calls.peek().caller_id, "321")

        callCenter.end_call()

        self.assertEqual(callCenter.processed_calls.peek().caller_id, "123")

if __name__ == "__main__":
    unittest.main()
