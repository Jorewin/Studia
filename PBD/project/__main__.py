from reader import reader
from mapper import mapper

# title.principals.tsv schema: (tconst, ordering, nconst, category, job, characters)
def main():
    results = {}

    for i, line in enumerate(reader()):
        (tconst, is_actor) = mapper(i, line)
        if results.get(tconst) is None:
            results[tconst] = [is_actor]
        else:
            results[tconst].append(is_actor)
    print(results)


if __name__ == "__main__":
    main()
