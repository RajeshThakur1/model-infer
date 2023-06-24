from pydantic import BaseModel, Field
from typing import Optional

class GetInputText(BaseModel):
    text: str = Field(
        ..., example="This is an example sentence"
    )

