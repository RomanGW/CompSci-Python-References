import tests
from topic7_assignment import sensory_processing, pathfinding, image_processing
import numpy as np
import cv2

def verify_image_processing(processed_images):
    # Check if processed_images is None or not a dictionary
    if not processed_images or not isinstance(processed_images, dict):
        return False
    def check_processing(image):
        return np.any(image)  # Checks if any of the pixel values are non-zero
    try:
        return all(check_processing(img) for img in processed_images.values())
    except AttributeError:
        return False

def run_tests():
    test_cases = {
        "image_processing": tests.test_image_processing(),
        "sensory_processing": tests.test_sensory_processing(),
        "pathfinding": tests.test_pathfinding()
    }

    function_to_test = {
        "sensory_processing": sensory_processing,
        "pathfinding": pathfinding,
        "image_processing": image_processing,
    }

    passed_tests = 0
    total_tests = sum(len(test_cases[func]) for func in test_cases)
    test_counter = 0

    for func, cases in test_cases.items():
        for case in cases:
            test_counter += 1
            # Check if the function is implemented and callable
            if callable(function_to_test.get(func)):
                if func == "image_processing":
                    test_image_path = case[0]
                    processed_images = function_to_test[func](test_image_path)
                    test_result = verify_image_processing(processed_images)
                    expected = "processing_done"
                else:
                    input_args, expected = case[:-1], case[-1]
                    test_result = function_to_test[func](*input_args) == expected
            else:
                test_result = False  # Assume test failed if function is not callable or not present

            if test_result:
                print(f"Test {test_counter}: Correct.")
                passed_tests += 1
            else:
                print(f"Test {test_counter}: Incorrect. Expected: {expected}, Got: {'processing_failed' if func == 'image_processing' else 'None'}")

    print(f"Passed {passed_tests} of {total_tests} tests.")

if __name__ == "__main__":
    run_tests()
