IRREG_PLURAL = {'man': 'men', 'woman': 'women', 'foot': 'feet', 'tooth': 'teeth', 'child': 'children',
                'person': 'people', 'datum': 'data', 'phenomenon': 'phenomena', 'crisis': 'crises',
                'analysis': 'analyses', 'photo': 'photos', 'piano': 'pianos', 'mouse': 'mice',
                'chief': 'chiefs', 'safe': 'safes', 'roof': 'roofs', 'brief': 'briefs', 'radius': 'radii'}

PRONOUNS = {'i': 'we', 'you': 'you', 'he': 'they', 'she': 'they', 'it': 'they'}

ONLY_SINGULAR = ('mathematics', 'physics', 'phonetics', 'linguistics', 'economics', 'politics',
                 'corps', 'fish', 'crossroads', 'means', 'series', 'headquarters', 'alms', 'species',
                 'dozen', 'swine', 'aircraft', 'knowledge', 'luggage', 'advice', 'money', 'information',
                 'furniture', 'athletics', 'linguistics', 'friendship', 'peace', 'sugar', 'weather', 'ink',
                 'business')

ONLY_PLURAL = ('news', 'trousers', 'scissors', ' goods', 'glasses', 'clothes', 'shorts', 'police',
               'cattle', 'spectacles')

VERB_NOT_PC = ('concern', 'wish', 'believe', 'imagine', 'please', 'hope', 'dislike', 'have', 'fit', 'depend', 'own',
               'guess', 'consist', 'impress', 'object', 'recognize', 'like', 'smell', 'hate', 'astonish', 'forget',
               'know', 'need', 'be', 'involve', 'possess', 'seem', 'think', 'suppose', 'feel', 'surprise', 'remember',
               'cost', 'touch', 'agree', 'deserve', 'love', 'see', 'include', 'hear', 'refuse', 'belong', 'prefer',
               'satisfy', 'mean', 'realize', 'want', 'taste', 'understand', 'sound', 'contain')

VOWEL = ('a', 'e', 'i', 'o', 'u')

CONSONANT = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'z')

VERBS_1s_STRESS = ('happen', 'open', 'offer', 'enter', 'suffer', 'consider', 'indicate', 'complicate', 'whisper',
                   'order', 'blossom')


def get_plural(noun):
    """Return plural form of noun or pronoun if it exists

    """
    if noun in IRREG_PLURAL.keys():
        return IRREG_PLURAL[noun]
    elif noun in ONLY_PLURAL or noun in PRONOUNS.values():
        return noun
    elif noun in PRONOUNS.keys():
        return PRONOUNS[noun]
    elif noun[-1] == 'y' and noun[-2] not in VOWEL:
        return noun[:-1] + 'ies'
    elif noun[-1] == 'o' and noun[-2] in VOWEL:
        return noun + 's'
    elif noun[-1] == 'f':
        return noun[:-1] + 'ves'
    elif noun[-2:] == 'fe':
        return noun[:-2] + 'ves'
    elif noun[-1] in ('a', 'o', 'i', 's', 'x') or noun[-2:] in ('ss', 'sh', 'ch'):
        return noun + 'es'
    else:
        return noun + 's'


def get_predicate_ps(verb):
    """Return verb of 3-rd person singular in present simple

    """
    if verb[-1] in ('s', 'x', 'z', 'o') or verb[-2:] in ('ch', 'sh'):
        return verb + 'es'
    elif verb[-1] == 'y' and verb[-2] not in VOWEL:
        return verb[:-1] + 'ies'
    else:
        return verb + 's'


def get_predicate_pc(verb):
    """Return verb in present continuous

    """
    if (verb[-1] == 'e') and (verb[-2:] not in ('ee', 'ie')):
        return verb[:-1] + 'ing'
    elif verb[-2:] == 'ie':
        return verb[:-2] + 'ying'
    elif verb[-3] in VOWEL and verb[-2] in VOWEL:
        return verb + 'ing'
    elif verb in VERBS_1s_STRESS:
        return verb + 'ing'
    elif verb[-1] in CONSONANT and verb[-2] in VOWEL:
        return verb + verb[-1] + 'ing'
    else:
        return verb + 'ing'


def get_article(article, number, subject):
    """Return correct article

    """
    if subject in PRONOUNS.values() or subject in PRONOUNS.keys():
        return ''
    elif subject in ONLY_PLURAL and article not in ('a', 'an'):
        return article
    elif number > 1 and article in ('a', 'an') or subject in ONLY_PLURAL:
        return ''
    elif article == 'a' and subject[0] in VOWEL:
        return 'an'
    else:
        return article


def word_lower(article, subject, predicate):
    return article.lower(), subject.lower(), predicate.lower()


#################################################################################

def present_simple(article, subject, number, predicate):
    """Return sentence in Present Simple

    """
    if number <= 0:
        return None
    article, subject, predicate = word_lower(article, subject, predicate)
    article = get_article(article, number, subject)
    if number > 1 and (subject not in ONLY_SINGULAR) or subject in ONLY_PLURAL:
        subject = get_plural(subject)
    else:
        if subject not in ('i', 'you', 'we', 'they'):
            predicate = get_predicate_ps(predicate)
    if not article:
        return ' '.join((subject.title(), predicate))
    else:
        return ' '.join((article.title(), subject, predicate))


def present_continuous(article, subject, number, predicate):
    """Return sentence in Present Continuous

    """

    if number <= 0:
        return None
    article, subject, predicate = word_lower(article, subject, predicate)
    article = get_article(article, number, subject)
    if predicate in VERB_NOT_PC:
        return present_simple(article, subject, number, predicate)
    if number > 1 and (subject not in ONLY_SINGULAR) or subject in ONLY_PLURAL:
        subject = get_plural(subject)
        predicate = 'are ' + get_predicate_pc(predicate)
    else:
        if subject == 'i':
            predicate = 'am ' + get_predicate_pc(predicate)
        else:
            predicate = 'is ' + get_predicate_pc(predicate)
    if not article:
        return ' '.join((subject.title(), predicate))
    else:
        return ' '.join((article.title(), subject, predicate))


#######################################################################

if __name__ == '__main__':
    print(present_simple('A', 'Boy', 1, 'Go'))
    print(present_continuous('A', 'Apple', 1, 'fall'))
    print(present_simple('a', 'chief', 1, 'work'))
    print(present_continuous('the', 'flower', 2, 'blossom'))
