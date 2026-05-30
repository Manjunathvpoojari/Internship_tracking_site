# MVP — VTU Internship Journal App

A full-stack web application to view and manage your VTU internship daily log.

## Stack
- **Backend**: Python Flask
- **Database**: SQLite (file: `internship.db`)
- **Frontend**: Vanilla HTML/CSS/JS (no build step needed)

## Setup & Run

### 1. Install dependencies
```bash
pip install flask
```

### 2. Run the app
```bash
python app.py
```

The server starts at **http://localhost:5050**

- **Public view** → http://localhost:5050/
- **Admin panel** → http://localhost:5050/admin

The database is auto-created and seeded with all 73 entries on first run.

## Features

### Public View (/)
- Hero with internship summary
- Live stats (total entries, hours, phases)
- Phase filter buttons (All / Phase 1 / Phase 2 / Phase 3 / April)
- Every entry shown as a card with date, hours, phase, skills
- Click any card to expand and read full work summary, learning outcome, and blockers

### Admin Panel (/admin)
- Stats bar with per-phase counts
- Full data table with search and phase filter
- **View** any entry in detail
- **Edit** any entry (all fields editable)
- **Delete** any entry (with confirmation)
- **Add new entry** via a form with all fields

## API Endpoints
| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/entries | All entries (optional ?phase=) |
| GET | /api/entries/:id | Single entry |
| POST | /api/entries | Create entry |
| PUT | /api/entries/:id | Update entry |
| DELETE | /api/entries/:id | Delete entry |
| GET | /api/stats | Aggregate stats |

## Data Fields
Each entry has: `date`, `hours`, `phase`, `work_summary`, `learning_outcome`, `skills`, `blockers`
