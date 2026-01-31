from pydantic import BaseModel, Field


class ScoresOutput(BaseModel):
    """
    Pydantic model for scores uoutput data.
    """
    final_score: float = Field(..., gt=0, description="The final calculated score.")
