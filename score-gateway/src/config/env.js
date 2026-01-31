require('dotenv').config();

module.exports = {
    port: process.envPORT || 3000,
    rulesEngineUrl: process.env.RULES_ENGINE_URL || 'http://localhost:5000',
    isDev: process.env.NODE_ENV !== 'production',
}