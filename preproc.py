from dicts import rep_rules


def read_dicts(de_path="de.txt", es_path="es.txt", en_path="en.txt", pl_path="pl.txt"):
    de = open(de_path).read()
    es = open(es_path).read()
    en = open(en_path).read()
    pl = open(pl_path).read()
    return (de, es, en, pl)


def simplify_word(word):
    try:
        return "".join(map(lambda x: rep_rules[x.lower()], word))
    except KeyError:
        return ""


def main():
    langs = ["\n".join(map(simplify_word, lang.split())) for lang in read_dicts()]
    print("Writing to file")
    open("simp_de.txt", "w").writelines(langs[0])
    open("simp_es.txt", "w").writelines(langs[1])
    open("simp_en.txt", "w").writelines(langs[2])
    open("simp_pl.txt", "w").writelines(langs[3])


if __name__ == "__main__":
    main()
