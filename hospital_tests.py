import unittest
from hospital_1 import Queue, Patient

class HospitalTests(unittest.TestCase):
    def test(self):
        hospital = Queue()
        hospital.enqueue(Patient("John", "05-06-2025"))
        hospital.enqueue(Patient("Albert", "06-07-2025"))
        hospital.enqueue(Patient("Jane", "07-08-2025"))

        a = hospital.peek()

        self.assertEqual(a.name, "John")

        b = hospital.dequeue()

        self.assertEqual(a.name, b.name)

        c = hospital.dequeue()
        d = hospital.dequeue()

        names = [b.name, c.name, d.name]
        
        self.assertListEqual(names, ["John", "Albert", "Jane"])

if __name__ == "__main__":
    unittest.main()
