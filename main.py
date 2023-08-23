import re


def read_dicts():
    de = open("simp_de.txt").read().split()
    es = open("simp_es.txt").read().split()
    en = open("simp_en.txt").read().split()
    pl = open("simp_pl.txt").read().split()
    return (de, es, en, pl)


def count_substring(substr, de, es, en, pl):
    dec = len(re.findall(substr, "\n".join(de)))
    esc = len(re.findall(substr, "\n".join(es)))
    enc = len(re.findall(substr, "\n".join(en)))
    plc = len(re.findall(substr, "\n".join(pl)))
    langsc = (dec, esc, enc, plc)
    return langsc


def main():
    langs = read_dicts()
    while True:
        langsc = count_substring(input("substring: "), *langs)
        print("de: {}\nes: {}\nen: {}\npl: {}\n".format(*langsc))


if __name__ == "__main__":
    main()
