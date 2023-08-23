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
    bad_words = []
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
                bad_words.append(word)
                print(
                    f"Word: {word}\nTarget lang: {lang}\nPredicted lang: {res_lang}\n"
                )
    return bad_words


def main():
    words = read_dicts()
    probs = pickle.load(open("data/probs.pickle", "rb"))
    print(get_bad_words(words, probs, n=100))


if __name__ == "__main__":
    main()
