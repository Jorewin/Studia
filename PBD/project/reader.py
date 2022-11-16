from collections.abc import Iterator


def reader(skip_header: bool) -> Iterator[str]:
    try:
        if skip_header:
            input()

        while True:
            yield input().strip()
    except EOFError:
        pass
    finally:
        return
