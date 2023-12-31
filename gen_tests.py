import random


def read_dicts():
    de = open("data/simp_de.dic").read().split()
    es = open("data/simp_es.dic").read().split()
    en = open("data/simp_en.dic").read().split()
    pl = open("data/simp_pl.dic").read().split()
    return {"de": de, "es": es, "en": en, "pl": pl}


def generate_test(langs, i):
    n = random.randrange(1, 10)
    words = ""
    res = ""
    for _ in range(n):
        lang = random.choice(("de", "es", "en", "pl"))
        words += random.choice(langs[lang]) + "\n"
        res += lang + "\n"
    with open(f"tests/test{i}.in", "w") as f:
        f.writelines(str(n) + "\n" + words)
    with open(f"tests/test{i}.out", "w") as f:
        f.writelines(res)


def main():
    langs = read_dicts()
    for i in range(10):
        generate_test(langs, i)


if __name__ == "__main__":
    main()
