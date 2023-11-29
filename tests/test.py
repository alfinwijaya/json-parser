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

    def tests_step_5_fail_1(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail1.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_fail_2(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail2.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_fail_3(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail3.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_fail_4(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail4.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_fail_5(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail5.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_fail_6(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail6.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_fail_7(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail7.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_8(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail8.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_9(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail9.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_10(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail10.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_11(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail11.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_12(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail12.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_13(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail13.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_14(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail14.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_15(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail15.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_16(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail16.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_17(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail17.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_19(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail19.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_20(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail20.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_21(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail21.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_22(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail22.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_23(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail23.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_24(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail24.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_25(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail25.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_26(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail26.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_27(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail27.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_28(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail28.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_29(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail29.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_30(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail30.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_31(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail31.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_32(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail32.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
    
    def tests_step_5_fail_33(self):
        testargs = ["python", "json_parser.py", "tests/step5/fail33.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)

    def tests_step_5_pass_1(self):
        testargs = ["python", "json_parser.py", "tests/step5/pass1.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)

    def tests_step_5_pass_2(self):
        testargs = ["python", "json_parser.py", "tests/step5/pass2.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)

    def tests_step_5_pass_3(self):
        testargs = ["python", "json_parser.py", "tests/step5/pass3.json"]
        result = subprocess.run(testargs, capture_output=True, text=True)
        self.assertEqual(0, result.returncode)