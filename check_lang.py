import pickle


def check_word(word, probs):
    lang_probs = [1, 1, 1, 1]
    lang_probs = [i * j for i, j in zip(probs["^" + word[0]], lang_probs)]
    lang_probs = [i * j for i, j in zip(probs[word[-1] + "$"], lang_probs)]
    lang_probs = [
        round(langc / sum(lang_probs), 4) if sum(lang_probs) else 0
        for langc in lang_probs
    ]
    for substr in [word[i : i + 2] for i in range(len(word) - 1)]:
        lang_probs = [i * j for i, j in zip(probs[substr], lang_probs)]
        lang_probs = [
            round(langc / sum(lang_probs), 4) if sum(lang_probs) else 0
            for langc in lang_probs
        ]
    return lang_probs


def pretty_print_stats(word, lang_probs):
    print(
        """
Word: {0}
-----------
de: {1:%}
es: {2:%}
en: {3:%}
pl: {4:%}
-----------""".format(
            word, *[lang_prob for lang_prob in lang_probs]
        )
    )


def main():
    probs = pickle.load(open("data/probs.pickle", "rb"))

    while True:
        word = input("Give word: ")
        lang_probs = check_word(word, probs)
        print(("de", "es", "en", "pl")[lang_probs.index(max(lang_probs))])


if __name__ == "__main__":
    main()
