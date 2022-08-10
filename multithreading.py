"""Reference: Corey Schafer's video on YouTube"""
import concurrent.futures
import time

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping...{seconds} second(s)"

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in seconds]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")