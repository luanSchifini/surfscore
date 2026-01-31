import pytest


class TestScoresEndpoints:
    """
    Test suite for the Scores API endpoints.
    """

    @pytest.mark.parametrize("scores, expected_final_score", [
        ([9.0, 7.0, 8.0, 9.0, 6.0], 8.00),
        ([9.0, 7.0, 6.0], 7.00),
        ([10.0, 8.55, 9.1, 7.2], 8.82)
    ])
    def test_given_valid_scores_input_when_calculate_then_return_200(self, scores, expected_final_score, client):
        """
        Test given valid scores,
        When calculate score endpoint is called,
        Then it should return the final calculated score and status code 200.
        """
        # Arrange
        payload = {"scores": scores}

        # Act
        response = client.post("/scores/calculate", json=payload)

        # Assert
        assert response.status_code == 200
        assert response.json() == {"final_score": expected_final_score}


    @pytest.mark.parametrize("invalid_scores", [
        None,
        "invalid scores",
        [8.0],
        [7.0, 8.0, 9.0, "ten"],
        [],
        [8.0, 9.0],
    ])
    def test_given_malformed_json_when_calculate_then_return_422(self, invalid_scores, client):
        """
        Test malformed JSON input,
        When calculate score enpoint is called,
        Then it should return an error with status code 422.
        """
        # Arrange
        payload = {"scores": invalid_scores}

        # Act
        response = client.post("/scores/calculate", json=payload)

        # Assert
        assert response.status_code == 422

    @pytest.mark.parametrize("invalid_scores, error_hint", [
        ([7.0, -1.0, 9.0], "scores must be between 0 and 10"),
        ([6.0, 11.0, 8.0], "scores must be between 0 and 10"),
    ])
    def test_given_invalid_scores_when_calculate_then_return_400(self, invalid_scores, error_hint, client):
        """
        Test given invalid scores input,
        When calculate score enpoint is called,
        Then it should return an error with status code 400.
        """
        # Arrange
        payload = {"scores": invalid_scores}

        # Act
        response = client.post("/scores/calculate", json=payload)

        # Assert
        assert response.status_code == 400
        assert error_hint in response.json().get("detail").lower()