from reader import reader


# title.principals.tsv schema: (tconst, ordering, nconst, category, job, characters)
def mapper(index: int, line: str) -> tuple[str, bool]:
    (tconst, _, _, category, _, _) = line.split('\t')
    if (category in ["actor", "actress", "self"]):
        return (tconst, True)
    else:
        return (tconst, False)


def main():
    for i, line in enumerate(reader()):
        (tconst, is_actor) = mapper(i, line)
        print(tconst, int(is_actor))


if __name__ == "__main__":
    main()
