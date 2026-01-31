from pydantic import BaseModel, Field
from typing import List


class ScoresInput(BaseModel):
    """
    Pydantic model for scores input data.
    """
    scores: List[float] = Field(..., min_length=3, description="A list of score values given by the Judges.")
