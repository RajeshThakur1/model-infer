from pydantic import BaseModel, Field
from typing import Optional

class GetWrongWordIndex(BaseModel):
    text: str = Field(
        ..., example="I wrk as an AI Engineer"
    )

