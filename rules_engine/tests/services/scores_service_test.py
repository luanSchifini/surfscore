import pytest
from rules_engine.src.services import ScoresService


class TestScoresService:
    """
    Test suite for the ScoresService class.
    """

    @pytest.mark.parametrize("scores, expected_final_score", [
        # Standard case: remove 9.0 and 6.0, avg(9, 7, 8) = 8.0
        ([9.0, 7.0, 8.0, 9.0, 6.0], 8.0),
        # Minimal case: remove 9 and 6, avg(7) = 7.0
        ([9.0, 7.0, 6.0], 7.0), 
        # Float precision check
        ([10.0, 8.55, 9.1, 7.2], 8.82) # (8.55+9.1)/2 = 8.825 -> rounds to 8.82 or 8.83? Check your rounding strategy.
    ])
    def test_given_valid_scores_when_calculate_final_score_then_return_corret_final_score(self, scores, expected_final_score):
        # Arrange

        # Act
        final_score = ScoresService.calculate_final_score(scores)

        # Arrange
        assert final_score == expected_final_score

    @pytest.mark.parametrize("invalid_scores, expected_error", [
        # Invalid input types
        (None, ValueError),
        (12345, ValueError),
        ("invalid scores", ValueError),
        ({"score1": 9.0, "score2": 8.0}, ValueError),

        # Domain logic violations
        ([], ValueError),
        ([8.0], ValueError),
        ([8.0, 9.0], ValueError),

        # Mixed types
        ([7.0, 8.0, 9.0, "ten"], ValueError),

        # Range violations
        ([-7.0, -8.0, -9.0], ValueError),
        ([11.0, 10.0, 9.0], ValueError),
    ])
    def test_given_invalid_scores_when_calculate_final_score_then_return_an_error(self, invalid_scores, expected_error):
        # Arrange

        # Act / Assert
        with pytest.raises(expected_error):
            ScoresService.calculate_final_score(invalid_scores)
