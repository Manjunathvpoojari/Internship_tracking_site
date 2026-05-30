from flask import Flask, jsonify, request, send_from_directory
import sqlite3, os, json
from datetime import datetime

app = Flask(__name__, static_folder='public', static_url_path='')

DB = 'internship.db'

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            hours REAL NOT NULL,
            phase TEXT NOT NULL,
            work_summary TEXT NOT NULL,
            learning_outcome TEXT NOT NULL,
            skills TEXT NOT NULL,
            blockers TEXT NOT NULL DEFAULT 'No Blockers',
            created_at TEXT DEFAULT (datetime('now')),
            updated_at TEXT DEFAULT (datetime('now'))
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS meta (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ─── API ───

@app.route('/api/entries', methods=['GET'])
def get_entries():
    phase = request.args.get('phase')
    conn = get_db()
    if phase and phase != 'all':
        rows = conn.execute('SELECT * FROM entries WHERE phase=? ORDER BY date ASC', (phase,)).fetchall()
    else:
        rows = conn.execute('SELECT * FROM entries ORDER BY date ASC').fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route('/api/entries/<int:entry_id>', methods=['GET'])
def get_entry(entry_id):
    conn = get_db()
    row = conn.execute('SELECT * FROM entries WHERE id=?', (entry_id,)).fetchone()
    conn.close()
    if not row:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(dict(row))

@app.route('/api/entries', methods=['POST'])
def create_entry():
    data = request.json
    required = ['date', 'hours', 'phase', 'work_summary', 'learning_outcome', 'skills']
    for f in required:
        if not data.get(f):
            return jsonify({'error': f'{f} is required'}), 400
    conn = get_db()
    cur = conn.execute(
        '''INSERT INTO entries (date, hours, phase, work_summary, learning_outcome, skills, blockers)
           VALUES (?,?,?,?,?,?,?)''',
        (data['date'], float(data['hours']), data['phase'],
         data['work_summary'], data['learning_outcome'],
         data['skills'], data.get('blockers', 'No Blockers'))
    )
    conn.commit()
    row = conn.execute('SELECT * FROM entries WHERE id=?', (cur.lastrowid,)).fetchone()
    conn.close()
    return jsonify(dict(row)), 201

@app.route('/api/entries/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    data = request.json
    conn = get_db()
    conn.execute(
        '''UPDATE entries SET date=?, hours=?, phase=?, work_summary=?, learning_outcome=?,
           skills=?, blockers=?, updated_at=datetime('now') WHERE id=?''',
        (data['date'], float(data['hours']), data['phase'],
         data['work_summary'], data['learning_outcome'],
         data['skills'], data.get('blockers', 'No Blockers'), entry_id)
    )
    conn.commit()
    row = conn.execute('SELECT * FROM entries WHERE id=?', (entry_id,)).fetchone()
    conn.close()
    return jsonify(dict(row))

@app.route('/api/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    conn = get_db()
    conn.execute('DELETE FROM entries WHERE id=?', (entry_id,))
    conn.commit()
    conn.close()
    return jsonify({'deleted': entry_id})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    conn = get_db()
    total_entries = conn.execute('SELECT COUNT(*) as c FROM entries').fetchone()['c']
    total_hours   = conn.execute('SELECT SUM(hours) as h FROM entries').fetchone()['h'] or 0
    by_phase      = conn.execute('SELECT phase, COUNT(*) as c, SUM(hours) as h FROM entries GROUP BY phase').fetchall()
    conn.close()
    return jsonify({
        'total_entries': total_entries,
        'total_hours': round(total_hours, 1),
        'by_phase': [dict(r) for r in by_phase]
    })

# ─── STATIC ───

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/admin')
def admin():
    return send_from_directory('public', 'admin.html')

if __name__ == '__main__':
    init_db()
    # seed if empty
    conn = get_db()
    count = conn.execute('SELECT COUNT(*) as c FROM entries').fetchone()['c']
    conn.close()
    if count == 0:
        import seed
        seed.run()
    app.run(debug=True, port=5050)
