import tests
from topic6_assignment import tokenize_text, pos_tagging, named_entity_recognition

def run_tests():
    test_cases = {
        "tokenize_text": tests.test_tokenize_text(),
        "pos_tagging": tests.test_pos_tagging(),
        "named_entity_recognition": tests.test_named_entity_recognition(),
    }

    passed_tests = 0
    total_tests = sum(len(cases) for cases in test_cases.values())
    test_counter = 0

    for func, cases in test_cases.items():
        for args in cases:
            test_counter += 1
            input_args, expected = args[:-1], args[-1]
            got = globals()[func](*input_args)

            if got == expected:
                print(f"Test {test_counter}: Correct.")
                passed_tests += 1
            else:
                print(f"Test {test_counter}: Incorrect. Expected: {expected}, Got: {got}")

    print(f"Passed {passed_tests} of {total_tests} tests.")

if __name__ == "__main__":
    run_tests()
