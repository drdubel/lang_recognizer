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
        if sum(langpercs) != 0:
            yield (substr, langpercs)


def main():
    langs, lens = read_dicts()
    substrs = (
        list(ascii_lowercase)
        + [
            "^abge",
            "^ange",
            "^anti",
            "^ausg",
            "^auss",
            "^comp",
            "^cons",
            "^cont",
            "^desa",
            "^desc",
            "^dese",
            "^desp",
            "^durc",
            "^enca",
            "^entr",
            "^esca",
            "^hera",
            "^hype",
            "^inte",
            "^micr",
            "^nach",
            "^nieb",
            "^niec",
            "^nied",
            "^niek",
            "^niem",
            "^nien",
            "^nieo",
            "^niep",
            "^nier",
            "^nies",
            "^nieu",
            "^niew",
            "^niez",
            "^nonc",
            "^over",
            "^para",
            "^poly",
            "^prze",
            "^przy",
            "^pseu",
            "^scha",
            "^schl",
            "^schw",
            "^semi",
            "^sobr",
            "^supe",
            "^tran",
            "^tras",
            "^uber",
            "^unco",
            "^unde",
            "^unre",
            "^unte",
            "^verk",
            "^vers",
            "^zusa",
            "able$",
            "ador$",
            "ally$",
            "ania$",
            "anie$",
            "aniu$",
            "ante$",
            "ario$",
            "arse$",
            "ated$",
            "chen$",
            "cion$",
            "dura$",
            "ende$",
            "ente$",
            "ento$",
            "eren$",
            "erer$",
            "eres$",
            "eria$",
            "iach$",
            "iami$",
            "ical$",
            "idad$",
            "ismo$",
            "ista$",
            "izar$",
            "jaca$",
            "less$",
            "ling$",
            "lity$",
            "ment$",
            "ndem$",
            "nden$",
            "nder$",
            "ndes$",
            "nego$",
            "nemu$",
            "ness$",
            "ngen$",
            "ngly$",
            "niem$",
            "niom$",
            "nych$",
            "nymi$",
            "ring$",
            "rous$",
            "scie$",
            "stem$",
            "sten$",
            "ster$",
            "stes$",
            "test$",
            "tico$",
            "ting$",
            "tion$",
            "tive$",
            "wana$",
            "ysmy$",
        ]
        + [i + j for i in ascii_lowercase + "^" for j in ascii_lowercase + "$"]
        + [i + j + "$" for i in ascii_lowercase + "^" for j in ascii_lowercase]
        + ["^" + i + j for i in ascii_lowercase for j in ascii_lowercase + "$"],
    )[0]
    probs = dict(tuple(count_substrings(substrs, langs, lens, debug=True)))
    with open("data/probs.pickle", "wb") as f:
        pickle.dump(probs, f)
    print(probs)
    # while True:
    #    substr = input("give substring: ")
    #    probs = dict(tuple(count_substrings([substr], langs, lens, debug=True)))


if __name__ == "__main__":
    main()
