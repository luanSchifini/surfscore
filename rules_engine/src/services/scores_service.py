from typing import List
from rules_engine.config import logger


class ScoresService:
    """
    Domain Service responsible for the Surf Score calculation rules.
    """

    @staticmethod
    def calculate_final_score(scores: List[float]) -> float:
        """
        Calculate the final score from a given scores list,
        by removing the highest and lowest values and averaging the rest.

        :param scores: The scores list
        :return: Returns the final calculated score
        """
        if not isinstance(scores, list):
            logger.error(f"[ScoresService] Invalid Input Type: Provided scores must be a list")
            raise ValueError("Invalid Input Type: Provided scores must be a list")
        
        if len(scores) < 3:
            logger.error(f"[ScoresService] Provided scores list is not valid, at least 3 scores are required")
            raise ValueError("Provided scores list is not valid, at least 3 scores are required")

        for index, score in enumerate(scores):
            if not isinstance(score, (int, float)):
                logger.error(f"[ScoresService] All scores must be numeric values")
                raise ValueError(f"All scores must be numeric values, invalid value at index {index}: {score}")

            if score < 0.0 or score > 10.0:
                logger.error(f"[ScoresService] Scores must be between 0 and 10")
                raise ValueError(f"Scores must be between 0 and 10, invalid value at index {index}: {score}")

        # Remove the highest and lowest scores from the given scores list
        sorted_scores = sorted(scores)
        filtered_scores = sorted_scores[1:-1]

        # Calculate the final score as the average of the given scores list
        average = sum(filtered_scores) / len(filtered_scores)
        final_score = round(average, 2)

        logger.info(f"[ScoresService] Final score calculated successfully for scores: {scores}")

        return final_score
