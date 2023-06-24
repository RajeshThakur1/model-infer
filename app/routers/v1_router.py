from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKey
from app.middlewares.auth_apikey import get_api_key
from app.utilities import twiq_logger
from app.routers import datamodels
import random
random_array = GetRandomArray()

logger = twiq_logger.TwiqLogger(
    twiq_logger.get_logger(__name__), {"model_inference": "v1"}
)


router = APIRouter(
    tags=["Inference"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def health_check():
    """Check the health of services
    author: andy
    Returns:
        [json]: json object with a status code 200 if everything is working fine else 400.
    """
    return {"message": "Status = Healthy"}


@router.post("/get_random_array")
async def get_wrong_word_index(
    input: datamodels.GetInputText, api_key: APIKey = Depends(get_api_key)
):
    text = input.text
    random.seed(sentence)  # Set a seed based on the sentence for reproducibility
    random_array = [random.random() for _ in range(500)]  # Generate a list of 500 random floats
    return random_array
    return {"status_code": 200, "message": "EXTRACTED", "data": random_array}
