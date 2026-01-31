const request = require('supertest');
const axios = require('axios');
const app = require('../../src/app');

jest.mock('axios');

describe('Scores API Integration Tests', () => {
    const validScoresPayload = {
        scores: [10, 10, 20, 30, 30]
    }
    const malformedPayloads = [
        {
            scenario: 'scores payload is a string',
            payload: {scores: 'not-an-array'},
        },
        {
            scenario: 'scores payload is a number',
            payload: {scores: 1},
        },
        {
            scenario: 'scores payload is an empty array',
            payload: {scores: []},
        },
        {
            scenario: 'scores payload is an array with less than three values',
            payload: {scores: [10, 20]},
        },
        {
            scenario: 'scores payload has non-numeric values',
            payload: {scores: [10, 'twenty', 30, 40, 50]},
        },
    ];

    beforeEach(() => {
        jest.clearAllMocks();
    })

    it('SUCCESS: Should return 200 when given valid scores payload', async () => {
        // Arrange
        axios.post.mockResolvedValue({
            data: {final_score: 20}
        }); // Mock the external service response

        // Act
        const response = await request(app)
            .post('/api/scores/submit')
            .send(validScoresPayload);

        // Assert
        expect(response.statusCode).toBe(200);
        expect(response.body).toHaveProperty('finalScore', 20);
        expect(axios.post).toHaveBeenCalledTimes(1);
    })

    test.each(malformedPayloads)(
        `ERROR: Should return 400 when given $scenario`,
        async ({ payload }) => {
            // Arrange

            // Act
            const response = await request(app)
                .post('/api/scores/submit')
                .send(payload)

            // Assert
            expect(response.statusCode).toBe(400);
            expect(response.body).toHaveProperty('error', 'Bad Request');
            expect(axios.post).toHaveBeenCalledTimes(0);
        }
    );

    it('ERROR: Should return 500 when external service fails', async () => {
        // Arrange
        axios.post.mockRejectedValue(new Error('External service error')); // Mock the external service failure

        // Act
        const response = await request(app)
            .post('/api/scores/submit')
            .send(validScoresPayload);

        // Assert
        expect(response.statusCode).toBe(500);
        expect(response.body).toHaveProperty('error', 'Internal Server Error');
        expect(axios.post).toHaveBeenCalledTimes(1);
    })
});