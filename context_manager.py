from time import perf_counter


class StopwatchContextManager:

    def __init__(self):
        self.time_passed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        self.time_passed = self.end - self.start
        return False
