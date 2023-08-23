import re
import pickle

from string import ascii_lowercase


def read_dicts():
    de = open("data/simp_de.dic").read().split()
    es = open("data/simp_es.dic").read().split()
    en = open("data/simp_en.dic").read().split()
    pl = open("data/simp_pl.dic").read().split()
    lde = len("".join(de))
    les = len("".join(es))
    lenn = len("".join(en))
    lpl = len("".join(pl))
    return ((de, es, en, pl), (lde, les, lenn, lpl))


def count_substring(substr, de, es, en, pl, lde, les, lenn, lpl):
    sum_len = sum([lde, les, lenn, lpl])
    dec = len(re.findall(substr, "\n".join(de), re.MULTILINE)) / (lde / sum_len * 100)
    esc = len(re.findall(substr, "\n".join(es), re.MULTILINE)) / (les / sum_len * 100)
    enc = len(re.findall(substr, "\n".join(en), re.MULTILINE)) / (lenn / sum_len * 100)
    plc = len(re.findall(substr, "\n".join(pl), re.MULTILINE)) / (lpl / sum_len * 100)
    return (dec, esc, enc, plc)


def count_substrings(substrs, langs, lens, debug=False):
    for substr in substrs:
        langcs = count_substring(substr, *langs, *lens)
        langpercs = [
            round(langc / sum(langcs), 4) if sum(langcs) else 0 for langc in langcs
        ]
        if debug:
            print(
                """
Susbtring: {0}
-----------
de: {1:%} - {5}
es: {2:%} - {6}
en: {3:%} - {7}
pl: {4:%} - {8}
-----------""".format(
                    substr, *langpercs, *langcs
                )
            )
        yield (substr, langpercs)


def main():
    langs, lens = read_dicts()
    substrs = [i + j for i in ascii_lowercase + "^" for j in ascii_lowercase + "$"]
    probs = dict(tuple(count_substrings(substrs, langs, lens, debug=True)))
    with open("data/probs.pickle", "wb") as f:
        pickle.dump(probs, f)
    print(probs)
    # while True:
    #    substr = input("give substring: ")
    #    probs = dict(tuple(count_substrings([substr], langs, lens, debug=True)))


if __name__ == "__main__":
    main()
