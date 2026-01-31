const axios = require('axios');
const mapRulesEngineScoresResponse = require('../utils/mappers');

class ScoresService {
    constructor(pythonEngineUrl) {
        this.pythonEngineUrl = process.env.PYTHON_ENGINE_URL || 'http://localhost:5000/';
    }
    
    async calculateFinalScore(scoresPayload) {
        // Verifies the payload structure
        if (!scoresPayload.scores || !Array.isArray(scoresPayload.scores)) {
            console.log('[ScoresService] Malformed payload: scores must be an array of numbers');
            throw new Error('INVALID_DATA: scores must be an array of numbers');
        };

        if (scoresPayload.scores.length <= 2) {
            console.log('[ScoresService] Malformed payload: scores must have at least thre values');
            throw new Error('INVALID_DATA: scores must have at least three values');
        };

        if (scoresPayload.scores.some(score => typeof score !== 'number')) {
            console.log('[ScoresService] Malformed payload: scores must be an array of numbers');
            throw new Error('INVALID_DATA: all scores must be numbers');
        };

        try {
            // Calls the python engine
            const response = await axios.post(`${this.pythonEngineUrl}/scores/calculate`, scoresPayload);

            return mapRulesEngineScoresResponse(response.data);
        } catch (error) {
            console.log('[ScoresService] Error:', error.message);
            throw new Error('EXTERNAL_API_ERROR: Unable to process scores data')
        }
    }
};

module.exports = new ScoresService();