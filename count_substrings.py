import re
import pickle

from string import ascii_lowercase


def read_dicts() -> tuple:
    de = open("data/simp_de.dic").read().split()
    es = open("data/simp_es.dic").read().split()
    en = open("data/simp_en.dic").read().split()
    pl = open("data/simp_pl.dic").read().split()
    return (de, es, en, pl)


def count_substring(substr, de, es, en, pl):
    dec = len(re.findall(substr, "\n".join(de)))
    esc = len(re.findall(substr, "\n".join(es)))
    enc = len(re.findall(substr, "\n".join(en)))
    plc = len(re.findall(substr, "\n".join(pl)))
    return (dec, esc, enc, plc)


def count_substrings(langs, substrs, debug=False):
    for substr in substrs:
        langcs = count_substring(substr, *langs)
        langpercs = [
            round(langc / sum(langcs, 2) * 100, 3) if sum(langcs) else 0
            for langc in langcs
        ]
        if debug:
            print(
                """
Susbtring: {0}
-----------
de: {1}% - {5}
es: {2}% - {6}
en: {3}% - {7}
pl: {4}% - {8}
-----------""".format(
                    substr, *langpercs, *langcs
                )
            )
        yield (substr, langpercs)


def main():
    langs = read_dicts()
    substrs = [i + j for i in ascii_lowercase[:4] for j in ascii_lowercase[:5]]
    probs = dict(tuple(count_substrings(langs, substrs)))
    with open("data/probs.pickle", "wb") as f:
        pickle.dump(probs, f)
    print(probs)


if __name__ == "__main__":
    main()
