from app.utilities import twiq_logger
from typing import Optional
from spellchecker import SpellChecker   # Import the library

logger = twiq_logger.TwiqLogger(
    twiq_logger.get_logger(__name__),{"model_infrence":"v1"}
)

class GetWrongTextIndex:
    """
    This class is used to extract the index of the wrong words
    """

    def __init__(self) -> None:
        logger.info("Initializing the GetWrongWordIndexClass")

    def get_wrong_word_index(self, sentence, misspell=None):
        spell = SpellChecker()
        words = sentence.split()
        misspell_words = spell.unknown(words)
        misspell_indexes = [{word:i,'corrected_word':spell.correction(word)} for i, word in enumerate(words) if word in misspell_words]

        return misspell_indexes

