import os

from ..src.wordcount import main


def test_migracion():

    main()

    if not os.path.exists("data/output/wordcount.tsv"):
        raise FileExistsError("El archivo wordcount.tsv no existe en data/output/")

    results = {}
    with open("data/output/wordcount.tsv", "r", encoding="utf-8") as f:
        for line in f.readlines():
            key, value = line.strip().split("\t")
            results[key] = value

    assert results.get("computational", 0) == "3"
    assert results.get("analytics", 0) == "5"
