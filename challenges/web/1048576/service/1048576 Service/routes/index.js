const express = require('express');
const router = express.Router();
const { execFile } = require('child_process');
const path = require('path');

router.get('/', (req, res) => {
    res.render('index', { title: 'CTF Challenge' });
});

router.post('/update-grid', (req, res) => {
    // Call the backend script with the provided data
    const data = req.body;
    const jsonData = JSON.stringify(data);
    const scriptPath = path.join(__dirname, '../backend/index.js');
    execFile('node', [scriptPath, jsonData], (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing script: ${error.message}`);
            res.status(500).json({ error: 'Failed to execute script' });
            return;
        }
        if (stderr) {
            console.error(`Script returned an error: ${stderr}`);
            res.status(500).json({ error: 'Script returned an error' });
            return;
        }
        try {
            const result = JSON.parse(stdout);
            res.json(result);
        } catch (parseError) {
            console.error(`Error parsing result: ${parseError.message}`);
            res.status(500).json({ error: 'Failed to parse result' });
        }
    });
});

module.exports = router;
