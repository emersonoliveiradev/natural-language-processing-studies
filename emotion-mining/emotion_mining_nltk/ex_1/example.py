import nltk

base = [("eu sou admirada por muitos", "alegria"),
        ("me sinto completamente amado", "alegria"),
        ("amar e maravilhoso", "alegria"),
        ("estou me sentindo muito animado novamente", "alegria"),
        ("eu estou muito bem hoje", "alegria"),
        ("que belo dia para dirigir um carro novo", "alegria"),
        ("o dia est� muito bonito", "alegria"),
        ("estou contente com o resultado do teste que fiz no dia de ontem",
         "alegria"),
        ("o amor e lindo", "alegria"),
        ("nossa amizade e amor vai durar para sempre", "alegria"),
        ("estou amedrontado", "medo"),
        ("ele esta me ameacando a dias", "medo"),
        ("isso me deixa apavorada", "medo"),
        ("este lugar e apavorante", "medo"),
        ("""se perdermos outro jogo seremos
         eliminados e isso me deixa com pavor""", "medo"),
        ("tome cuidado com o lobisomem", "medo"),
        ("se eles descobrirem estamos encrencados", "medo"),
        ("estou tremendo de medo", "medo"),
        ("eu tenho muito medo dele", "medo"),
        ("estou com medo do resultado dos meus testes", "medo")]


stop_words_manually = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles',
                       'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta', 'ir',
                       'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro',
                       'para', 'que', 'sem', 'talvez', 'tem', 'tendo', 'tenha',
                       'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns',
                       'vou']

# nltk.download('stopwords')
stop_words_nltk = nltk.corpus.stopwords.words('portuguese')
print(stop_words_nltk)


def remove_stop_words_common(text):
    new_base = []
    for (phrase, emotion) in text:
        new_phrase = []
        for word in phrase.split():
            if word not in stop_words:
                new_phrase.append(word)

        new_base.append((new_phrase, emotion))

    return new_base


def remove_stop_words_comprehension(text):
    new_base = []
    for (phrase, emotion) in text:
        new_phrase = [
            word for word in phrase.split() if word not in stop_words_nltk]

        new_base.append((new_phrase, emotion))

    return new_base


def remove_stop_words_lambda(text):
    pass


print(remove_stop_words_comprehension(base))
