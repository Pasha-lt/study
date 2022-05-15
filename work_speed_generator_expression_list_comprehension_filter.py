from datetime import datetime

new_dict = {i: i for i in range(100000000)}


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(f"{func.__name__}", datetime.now() - start)
        return result

    return wrapper


@timeit
def generator_expression_a():
    assert 9000000 in (data for data in new_dict.keys())


@timeit
def list_comprehension_a():
    assert 9000000 in [data for data in new_dict.keys()]


@timeit
def filter_a():
    assert filter(lambda w: 9000000 in w, new_dict.keys())


filter_a()  # filter_a 0:00:00.000011
generator_expression_a()  # generator_expression_a 0:00:00.267713
list_comprehension_a()  # list_comprehension_a 0:00:03.957104
