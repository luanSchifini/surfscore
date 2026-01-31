from fastapi import APIRouter, HTTPException, status
from rules_engine.config import logger
from rules_engine.src.schemas import ScoresInput, ScoresOutput
from rules_engine.src.services import ScoresService

api_router = APIRouter()


@api_router.post("/calculate", response_model=ScoresOutput)
def calculate(scores_input: ScoresInput) -> ScoresOutput:
    """
    Enpoint to calculate the final score based on the provided input scores.
    """
    try:
        # Calculate the final score
        final_score = ScoresService.calculate_final_score(scores_input.scores)

        return ScoresOutput(final_score=final_score)
    except ValueError as e:
        logger.error(f"Score calculation error for scores: {scores_input.scores}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error during score calculation for scores: {scores_input.scores}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal score calculation error")
