from conv_data import rep_rules


def read_dicts():
    de = open("data/de.dic").read().split()
    es = open("data/es.dic").read().split()
    en = open("data/en.dic").read().split()
    pl = open("data/pl.dic").read().split()
    return (de, es, en, pl)


def simplify_word(word):
    try:
        return "".join(map(lambda x: rep_rules[x.lower()], word))
    except KeyError:
        return ""


def main():
    langs = ["\n".join(map(simplify_word, lang.split())) for lang in read_dicts()]
    print("Writing to file")
    open("data/simp_de.txt", "w").writelines(langs[0])
    open("data/simp_es.txt", "w").writelines(langs[1])
    open("data/simp_en.txt", "w").writelines(langs[2])
    open("data/simp_pl.txt", "w").writelines(langs[3])


if __name__ == "__main__":
    main()
