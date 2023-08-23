import pickle


def check_word(word, probs):
    lang_probs = [1, 1, 1, 1]
    if len(word) == 1:
        return probs[word]
    lang_probs = [i * j for i, j in zip(probs["^" + word[0]], lang_probs)]
    lang_probs = [i * j for i, j in zip(probs[word[-1] + "$"], lang_probs)]
    lang_probs = [
        round(langc / sum(lang_probs), 4) if sum(lang_probs) else 0
        for langc in lang_probs
    ]
    for k in range(len(word)):
        if len(word) - k >= 2:
            lang_probs = [i * j for i, j in zip(probs[word[k : k + 2]], lang_probs)]
        if len(word) - k == 2:
            if word[k : k + 2] + "$" in probs:
                lang_probs = [
                    i * j for i, j in zip(probs[word[k : k + 2] + "$"], lang_probs)
                ]
        if len(word) - k == 3:
            if word[k : k + 3] + "$" in probs:
                lang_probs = [
                    i * j for i, j in zip(probs[word[k : k + 3] + "$"], lang_probs)
                ]
        if len(word) - k == 4:
            if word[k : k + 4] + "$" in probs:
                lang_probs = [
                    i * j for i, j in zip(probs[word[k : k + 4] + "$"], lang_probs)
                ]
        if k == 0:
            if len(word) >= 4:
                if "^" + word[0:4] in probs:
                    lang_probs = [
                        i * j for i, j in zip(probs["^" + word[0:4]], lang_probs)
                    ]
            if len(word) >= 3:
                if "^" + word[0:3] in probs:
                    lang_probs = [
                        i * j for i, j in zip(probs["^" + word[0:3]], lang_probs)
                    ]
            if len(word) >= 2:
                if "^" + word[0:2] in probs:
                    lang_probs = [
                        i * j for i, j in zip(probs["^" + word[0:2]], lang_probs)
                    ]
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
