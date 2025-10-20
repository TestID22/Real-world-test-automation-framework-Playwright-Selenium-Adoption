from contextlib import ContextDecorator


class TestStep(ContextDecorator):
    # TODO: Add logger
    def __init__(self, test_step):
        self.test_step = test_step

    def __enter__(self):
        print(f"\n START STEP {self.test_step}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"\n  FAILED STEP: {self.test_step} ")
            print(f"\n  Error: {exc_val}")
        else:
            print(f"\n PASSED STEP: {self.test_step} ")
            # Returning False lets exceptions propagate
        return False