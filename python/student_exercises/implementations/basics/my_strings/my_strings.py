import string


def compteMots(phrase):
    return len(phrase.split())


def inverser(mot):
    return mot[::-1]


def estPalindrome(mot):
    return mot == inverser(mot)


def compteCaracteres(mot):
    return len(mot)


def compterLesLettres(mot):
    lettres = string.ascii_letters
    count = 0
    for lettre in mot:
        if lettre in lettres:
            count += 1
    return count


def compteVoyelles(mot):
    vowels = "aeiouyAEIOUY"
    count = 0
    for lettre in mot:
        if lettre in vowels:
            count += 1
    return count


def compteConsonnes(mot):
    vowels = "aeiouyAEIOUY"
    count = 0
    for lettre in mot:
        if lettre not in vowels and lettre in string.ascii_letters:
            count += 1
    return count


def concatenation(mot1, mot2):
    return mot1 + mot2
