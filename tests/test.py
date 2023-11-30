import subprocess
import unittest

class JSONParser_Test(unittest.TestCase):
    def tests_step_1_invalid(self):
        testargs = ["python", "json_parser.py", "tests/step1/invalid.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_1_valid(self):
        testargs = ["python", "json_parser.py", "tests/step1/valid.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)

    def tests_step_2_invalid(self):
        testargs = ["python", "json_parser.py", "tests/step2/invalid.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_2_invalid_2(self):
        testargs = ["python", "json_parser.py", "tests/step2/invalid2.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_2_invalid_3(self):
        testargs = ["python", "json_parser.py", "tests/step2/invalid3.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_2_valid(self):
        testargs = ["python", "json_parser.py", "tests/step2/valid.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)

    def tests_step_3_invalid(self):
        testargs = ["python", "json_parser.py", "tests/step3/invalid.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_3_valid(self):
        testargs = ["python", "json_parser.py", "tests/step3/valid.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)

    def tests_step_4_invalid(self):
        testargs = ["python", "json_parser.py", "tests/step4/invalid.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_4_valid(self):
        testargs = ["python", "json_parser.py", "tests/step4/valid.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)

    def tests_step_4_valid_2(self):
        testargs = ["python", "json_parser.py", "tests/step4/valid2.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)

    def tests_step_5_invalid_1(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid1.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_invalid_2(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid2.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_invalid_3(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid3.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_invalid_4(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid4.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_invalid_5(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid5.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_invalid_6(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid6.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_invalid_7(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid7.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_8(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid8.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_9(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid9.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_10(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid10.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_11(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid11.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_12(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid12.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_13(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid13.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_14(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid14.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_15(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid15.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_16(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid16.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_17(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid17.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_19(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid19.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_20(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid20.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_21(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid21.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_22(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid22.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_23(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid23.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_24(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid24.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_25(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid25.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_26(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid26.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_27(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid27.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_28(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid28.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_29(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid29.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_30(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid30.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_31(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid31.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_32(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid32.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_invalid_33(self):
        testargs = ["python", "json_parser.py", "tests/step5/invalid33.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_valid_1(self):
        testargs = ["python", "json_parser.py", "tests/step5/valid1.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)

    def tests_step_5_valid_2(self):
        testargs = ["python", "json_parser.py", "tests/step5/valid2.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)

    def tests_step_5_valid_3(self):
        testargs = ["python", "json_parser.py", "tests/step5/valid3.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)