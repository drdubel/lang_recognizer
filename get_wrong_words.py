import random
import pickle
from check_lang import check_word


def read_dicts():
    de = open("data/simp_de.dic").read().split()
    es = open("data/simp_es.dic").read().split()
    en = open("data/simp_en.dic").read().split()
    pl = open("data/simp_pl.dic").read().split()
    return {"de": de, "es": es, "en": en, "pl": pl}


def get_bad_words(words, probs, n=1000):
    matches = "    match word:\n"
    for lang in ["de", "es", "en", "pl"]:
        for i in range(n):
            word = random.choice(words[lang])
            lang_probs = check_word(word, probs)
            res_lang = ("de", "es", "en", "pl")[lang_probs.index(max(lang_probs))]
            if lang != "de" and word in words["de"]:
                continue
            if lang != "es" and word in words["es"]:
                continue
            if lang != "en" and word in words["en"]:
                continue
            if lang != "pl" and word in words["pl"]:
                continue
            if lang != res_lang:
                # print(
                #    f"Word: {word}\nTarget lang: {lang}\nPredicted lang: {res_lang}\n"
                # )
                res = [0, 0, 0, 0]
                if lang == "de":
                    res[0] = 1
                if lang == "es":
                    res[1] = 1
                if lang == "en":
                    res[2] = 1
                if lang == "pl":
                    res[3] = 1
                matches += f'        case "{word}":\n            return {res}\n'

    return matches


def main():
    words = read_dicts()
    probs = pickle.load(open("data/probs.pickle", "rb"))
    print(get_bad_words(words, probs, n=1000))


if __name__ == "__main__":
    main()
