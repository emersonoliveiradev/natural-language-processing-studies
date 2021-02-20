import nltk
# nltk.download('stopwords')
# nltk.download('rslp')

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
stop_words_nltk = nltk.corpus.stopwords.words('portuguese')


def remove_stop_words(text):
    """
        Responsável pela remoção das Stop Words presentes nas tuplas

        :param text: Base de dados de texto e classes correspondentes
        :type: list

        :return: Listas de palavras e classes correspondentes
        :rtype: list
    """
    new_base = []
    for (phrase, emotion) in text:
        new_phrase = [
            word for word in phrase.split() if word not in stop_words_nltk]

        new_base.append((new_phrase, emotion))

    return new_base


def stemmer_apply(text):
    """
        Responsável pela substituição de cada palavra presente na lista dentro
        da tupla pelo seu radical.

        :param text: Base de dados de texto e classes correspondentes
        :type: list

        :return: Base de dados de texto com stemmer e classes correspondentes
        :rtype: list
    """
    new_base = []
    stemmer = nltk.stem.RSLPStemmer()

    for (phrase, emotion) in text:
        new_phrase = [stemmer.stem(word) for word in phrase]

        new_base.append((new_phrase, emotion))

    return new_base


def search_words(text):
    """
        Responsável por burcar todas as palavras presentes na lista ignorando
        as classes

        :param text: Base de dados de texto e classes correspondentes
        :type: list

        :return: Todas as palavras encontradas
        :rtype: list
    """
    all_words = []
    [all_words.extend(phrase) for phrase, _ in text]

    return all_words


def search_frequency(words):
    """
        Responsável por determinar a frequência que cada palavra possui

        :param words: Lista de palavras
        :type: list

        :return: Cada palavra da lista sem repetição e sua frequência
        :rtype: nltk.probability.FreqDist
    """
    return nltk.FreqDist(words)


def search_unique_words(words_frequency):
    """
        Responsável por uma lista de palavras sem repetição

        :param words_frequency: Lista de palavras e frequência
        :type: nltk.probability.FreqDist

        :return: Cada palavra da lista sem repetição e sua frequência
        :rtype: dict_keys
    """
    words_frequency = words_frequency.keys()
    return words_frequency


def words_extractor(doc):
    """
        Responsável por a partir de duas listas retornar um dicionário
        contendo cada palavra e o valor booleano para sua presença
        na outra lista.

        :param doc: Lista de palavras
        :type: list

        :return: Cada palavra da lista e seu correspondente booleano
        :rtype: dict
    """
    doc = set(doc)
    features = {}

    for word in unique_words:
        features[str(word)] = (word in doc)

    return features


def train_classifier(base):
    """
        Responsável por a partir de duas listas retornar um dicionário
        contendo cada palavra e o valor booleano para sua presença
        na outra lista.

        :param doc: Lista de palavras
        :type: list

        :return: Cada palavra da lista e seu correspondente booleano
        :rtype: dict
    """

    return nltk.NaiveBayesClassifier.train(base)


def phrase_normalization(phrase):
    """
        Reponsável por normalizar uma frase de entrada para o formato esperado
        pela função  classify ou prob_classify da biblioteca NLTK.
        Aplica a remoção de stop_words, extração de palavras e extração do 
        radical de cada palavra.

        :param phrase: Frase qualquer
        :type: str

        :return: Cada palavra da frase em seu formato de radical
        :rtype: dict
    """
    phrase = [
        word for word in phrase.split() if word not in stop_words_nltk]

    stemmer = nltk.stem.RSLPStemmer()
    phrase = [stemmer.stem(word) for word in phrase]

    return words_extractor(phrase)


text_without_stop_words = remove_stop_words(base)
text_with_stemmer = stemmer_apply(text_without_stop_words)

words = search_words(text_with_stemmer)
words_frequency = search_frequency(words)
# print(words_frequency.most_common(50))

unique_words = search_unique_words(words_frequency)

complete_base_to_classifier = nltk.classify.apply_features(
    words_extractor,
    text_with_stemmer)

classifier = train_classifier(complete_base_to_classifier)
#print(classifier.labels())
#print(classifier.show_most_informative_features())


test_phrase = "hoje estou apavorado"
test_phrase = phrase_normalization(test_phrase)
print(type(test_phrase))
label_detected = classifier.classify(test_phrase)
print(label_detected)

distribution = classifier.prob_classify(test_phrase)
for label in distribution.samples():
    print(label, " - ", distribution.prob(label))
