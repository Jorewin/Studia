from typing import Iterator


def reader(header: str=None) -> Iterator[str]:
    try:
        if header is not None:
            if (first_line := input().strip()) != header:
                yield first_line

        while True:
            yield input().strip()
    except EOFError:
        pass
    finally:
        return
