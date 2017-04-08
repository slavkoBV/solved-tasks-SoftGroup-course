IRREG_PLURAL = {'man': 'men', 'woman': 'women', 'foot': 'feet', 'tooth': 'teeth', 'child': 'children',
                'person': 'people', 'datum': 'data', 'phenomenon': 'phenomena', 'crisis': 'crises',
                'analysis': 'analyses', 'photo': 'photos', 'piano': 'pianos', 'mouse': 'mice',
                'chief': 'chiefs', 'safe': 'safes', 'roof': 'roofs', 'brief': 'briefs', 'radius': 'radii'}

ONLY_SINGULAR = ('mathematics', 'physics', 'phonetics', 'linguistics', 'economics', 'politics',
                 'corps', 'fish', 'crossroads', 'means', 'series', 'headquarters', 'alms', 'species',
                 'dozen', 'swine', 'aircraft', 'knowledge', 'luggage', 'advice', 'money', 'information',
                 'furniture', 'athletics', 'linguistics', 'friendship', 'peace', 'sugar', 'weather', 'ink',
                 'business')

ONLY_PLURAL = ('news', 'trousers', 'scissors', ' goods', 'glasses', 'clothes', 'shorts', 'police',
               'cattle', 'spectacles')


def is_plural(noun):
    """Return True if noun is plural and False otherwise

    """
    if noun.endswith('s') and (noun[-2:] not in ['us', 'is', 'ss']) and (
                noun not in ONLY_SINGULAR):
        return True
    elif noun in IRREG_PLURAL.values() or noun in ONLY_PLURAL:
        return True
    else:
        return False
