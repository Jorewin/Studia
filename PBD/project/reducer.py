from reader import reader


def reducer(tconst: str, is_actor: list[bool]) -> tuple[tconst, int]:
    return (tconst, sum(is_actor))


def main():
    for tconst, is_actor in reader().split('\t'):
        print(*reducer(*line.split()))


if __name__ == "__main__":
    main()
