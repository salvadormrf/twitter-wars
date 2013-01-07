import re
import enchant
from enchant.tokenize import get_tokenizer, URLFilter

# create dictionary for GB English
d = enchant.Dict("en_GB")

class HashFilter(enchant.tokenize.Filter):
    """ Filter skipping over Twitter hashes.
                #\w+
    """
    _pattern = re.compile(r"#\w+")
    def _skip(self, word):
        if self._pattern.match(word):
            return True
        return False


class MentionFilter(enchant.tokenize.Filter):
    """ Filter skipping over Twitter mentions.
                @\w+
    """
    _pattern = re.compile(r"@\w+")
    def _skip(self, word):
        if self._pattern.match(word):
            return True
        return False


def check_spelling(text):
    # TODO check if language is not English
    # TODO use dictionary with persons names
    valid_words = []
    invalid_words = []
    unchecked_words = []
    
    tknzr = get_tokenizer("en_GB", (URLFilter, HashFilter, MentionFilter))
    for (word, pos) in tknzr(text):
        try:
            valid = d.check(word) # check if word is valid
        except enchant.errors.Error as e:
            unchecked_words.append(word)
            #logger.debug("Unable to check if word is valid: '%s' reason: '%s'" % (word, e))
        else:
            l = valid_words if valid else invalid_words
            l.append(word)
        
    return {"valid": valid_words, "invalid": invalid_words, "unchecked": unchecked_words}


# London -0.351468, 51.38494, 0.14788, 51.672343
# Exeter -3.570203, 50.687391, -3.456359, 50.761465
london_bounding_box = [-0.351468, 51.38494, 0.14788, 51.672343]
exeter_bounding_box = [-3.570203, 50.687391, -3.456359, 50.761465]

def find_city(coordinates):
    # ugly...
    # use a coordinate package for this...
    lat, long = coordinates
    
    if long >= exeter_bounding_box[0] and long <= exeter_bounding_box[2]:
        if lat >= exeter_bounding_box[1] and lat <= exeter_bounding_box[3]:
            return "exeter"
    if long >= london_bounding_box[0] and long <= london_bounding_box[2]:
        if lat >= london_bounding_box[1] and lat <= london_bounding_box[3]:
            return "london"
        
    return None
