import tracemalloc
import functools


def memoty_usage(func):
    def get_memory_stat(current, peak):
        print(f"\n\033[37mFunction Name       :\033[35;1m {func.__name__}\033[0m")
        print(f"\033[37mCurrent memory usage:\033[36m {current / 10 ** 6}MB\033[0m")
        print(f"\033[37mPeak                :\033[36m {peak / 10 ** 6}MB\033[0m")
        print(f"\033[37mDiff               :\033[36m {(peak - current) / 10 ** 6}MB\033[0m")

    @functools.wraps(func)
    def function_wrapper(*args, **kwargs):
        tracemalloc.start()

        result = func(*args, **kwargs)

        current, peak = tracemalloc.get_traced_memory()
        get_memory_stat(current, peak)
        tracemalloc.stop()

        return result
    return function_wrapper
