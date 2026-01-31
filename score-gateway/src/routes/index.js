const express = require('express');
const scoreController = require('../controllers/scoreController');

const router = express.Router();

router.post('/scores/submit', scoreController.submitScore);

module.exports = router;