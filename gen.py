import random


def read_dicts():
    de = open("data/de.dic").read().split()
    es = open("data/es.dic").read().split()
    en = open("data/en.dic").read().split()
    pl = open("data/pl.dic").read().split()
    return (de, es, en, pl)


def main():
    pass


if __name__ == "__main__":
    main()
