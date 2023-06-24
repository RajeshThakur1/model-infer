from app.utilities import twiq_logger
from typing import Optional
import random


logger = twiq_logger.TwiqLogger(
    twiq_logger.get_logger(__name__),{"model_infrence":"v1"}
)

class GetRandomArray:
    """
    This class is used to get the random array
    """

    def __init__(self) -> None:
        logger.info("Initializing the GetRandomArray")



    def generate_random_array(sentence):
        random.seed(sentence)  # Set a seed based on the sentence for reproducibility
        random_array = [random.random() for _ in range(500)]  # Generate a list of 500 random floats
        return random_array

