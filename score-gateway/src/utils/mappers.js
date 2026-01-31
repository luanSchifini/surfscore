const mapRulesEngineScoresResponse = (scoresResponse) => {
    return {
        finalScore: scoresResponse.final_score
    };
};

module.exports = mapRulesEngineScoresResponse;