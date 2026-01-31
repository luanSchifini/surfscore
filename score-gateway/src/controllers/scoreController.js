const scoresService = require('../services/scoresService');


class ScoreController {
    async submitScore(req, res) {
        try {
            // Receives the JSON payload
            const scoresPayload = req.body;

            // calls the service
            const result = await scoresService.calculateFinalScore(scoresPayload);

            // returns the response status
            return res.status(200).json(result);
        } catch (error) {
            if (error.message.startsWith('INVALID_DATA')) {
                return res.status(400).json({
                    error: 'Bad Request',
                    message: error.message
                });
            }

            return res.status(500).json({
                error: 'Internal Server Error',
                message: error.message
            });
        }
    }
}

module.exports = new ScoreController();