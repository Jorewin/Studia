from typing import Generator, Tuple
from reader import reader


def reducer(tconst: str) -> Generator[Tuple[str, int], int, None]:
    actor_count_sum = 0
    actor_count = yield tconst, actor_count_sum

    while actor_count is not None:
        actor_count_sum += actor_count
        actor_count = yield tconst, actor_count_sum
    yield tconst, actor_count_sum

def main():
    sep='\t'
    data = reader()

    try:
        line = next(data)
    except StopIteration:
        return
    current_tconst, actor_count = line.split(sep)
    reduce = reducer(current_tconst)
    next(reduce)
    reduce.send(int(actor_count))

    for line in data:
        tconst, actor_count = line.split(sep)

        if tconst != current_tconst:
            print(*next(reduce), sep=sep)
            current_tconst = tconst
            reduce = reducer(current_tconst)
            next(reduce)
        reduce.send(int(actor_count))
    print(*next(reduce), sep=sep)

if __name__ == "__main__":
    main()
