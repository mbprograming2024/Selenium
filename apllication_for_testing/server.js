const express = require('express');
const bodyParser = require('body-parser');
const sqlite3 = require('sqlite3').verbose();

// Initialize app and database
const app = express();
const db = new sqlite3.Database(':memory:');

// Middleware
app.use(bodyParser.json());
app.use(express.static(__dirname));

// Create a users table
db.serialize(() => {
    db.run(`
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    `);

    // Insert sample user
    db.run('INSERT INTO users (username, password) VALUES (?, ?)', ['admin', 'password123']);
});

// Login endpoint
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    db.get('SELECT * FROM users WHERE username = ? AND password = ?', [username, password], (err, row) => {
        if (err) {
            return res.status(500).json({ success: false, message: 'Internal server error.' });
        }

        if (row) {
            res.json({ success: true });
        } else {
            res.json({ success: false, message: 'Invalid username or password.' });
        }
    });
});

// Start server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
