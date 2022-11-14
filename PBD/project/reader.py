from collections.abc import Iterator


def reader() -> Iterator[str]:
    try:
        input()

        while True:
            yield input().strip()
    except EOFError:
        pass
    finally:
        return
