# You can run this program thousands of times and never see the problem.
# That’s what makes this type of problem quite difficult to debug as
# it can be quite hard to reproduce and can cause random-looking errors to show up.
import concurrent.futures


counter = 0
counter_non_thread = 0


def increment_counter(fake_value):
    global counter
    for _ in range(100):
        counter += 1


def non_thread_counter_increase():
    global counter_non_thread
    for _ in range(100):
        counter_non_thread += 1


if __name__ == "__main__":
    fake_data = [x for x in range(5000)]
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5000) as executor:
        executor.map(increment_counter, fake_data)
    print(f"Counter = {counter}")
    non_thread_counter_increase()
    print(f"counter_non_thread = {counter_non_thread}")
