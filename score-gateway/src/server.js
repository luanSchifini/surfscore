require('dotenv').config();

const app = require('./app');

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Score Gateway running on port ${PORT}`);
    console.log(`Connected to Rules Engine at ${process.env.rulesEngineUrl}`);
});