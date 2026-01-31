const express = require('express');
const cors = require('cors');
const routes = require('./routes');

const app = express();


// Globals Middlewares
app.use(cors());  // Allows CORS for all origins
app.use(express.json());  // Parses incoming JSON requests

// Base Routes
app.use('/api', routes);

// Health Check Endpoint
app.get('/health', (req, res) => res.json({ status: 'ok'}));

module.exports = app;