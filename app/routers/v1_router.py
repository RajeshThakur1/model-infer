from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKey
from app.middlewares.auth_apikey import get_api_key
from app.utilities import twiq_logger
from app.services.get_index.get_incorrect_word_index import GetWrongTextIndex
from app.routers import datamodels
wrong_word_index = GetWrongTextIndex()

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


@router.post("/get_wrong_word_index")
async def get_wrong_word_index(
    input: datamodels.GetWrongWordIndex, api_key: APIKey = Depends(get_api_key)
):
    text = input.text
    resp = wrong_word_index.get_wrong_word_index(text)
    return {"status_code": 200, "message": "EXTRACTED", "data": resp}