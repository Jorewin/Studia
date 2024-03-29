from typing import Tuple
from reader import reader


# title.principals.tsv schema: (tconst, ordering, nconst, category, job, characters)
def mapper(index: int, line: str) -> Tuple[str, int]:
    tconst, _, _, category, _, _ = line.split('\t')
    if category in ["actor", "actress", "self"]:
        return tconst, 1
    else:
        return tconst, 0

def main():
    sep='\t'
    
    for i, line in enumerate(reader("tconst\tordering\tnconst\tcategory\tjob\tcharacters")):
        tconst, actor_count = mapper(i, line)
        print(tconst, actor_count, sep='\t')

if __name__ == "__main__":
    main()
