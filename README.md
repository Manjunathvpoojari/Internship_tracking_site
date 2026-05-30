# 📓 MVP — VTU Internship Journal 2026

A full-stack web app to manage and showcase your VTU internship daily log.
**Stack:** Python Flask · SQLite · Vanilla HTML/CSS/JS — no build tools needed.

---

## 🖥️ How to Run (VS Code — Step by Step)

### Step 1 — Install Python
If you don't have Python installed:
- Go to https://www.python.org/downloads/
- Download and install Python 3.10 or later
- During installation, **tick "Add Python to PATH"** ✅

Verify it works — open VS Code terminal (`Ctrl + ~`) and type:
```
python --version
```
You should see something like `Python 3.11.x`

---

### Step 2 — Open the Project in VS Code
1. Open VS Code
2. Go to **File → Open Folder**
3. Select the `internship-app` folder

---

### Step 3 — Open the Terminal in VS Code
Press `` Ctrl + ` `` (backtick) to open the integrated terminal.

---

### Step 4 — Install Flask
In the VS Code terminal, run:
```
pip install flask
```
That's the only dependency. No npm, no build steps.

---

### Step 5 — Run the App
In the terminal, run:
```
python app.py
```

You'll see:
```
✅ Server running!
   Public view  →  http://localhost:5050
   Admin panel  →  http://localhost:5050/admin
```

Open your browser and go to **http://localhost:5050**

> The database (`internship.db`) is created automatically on first run
> and seeded with all your Feb–Apr entries. Nothing to set up manually.

---

### Step 6 — Stop the Server
Press `Ctrl + C` in the terminal.

---

## 📂 Project Structure

```
internship-app/
├── app.py              ← Flask server + API routes
├── seed.py             ← All journal entries (Feb–Apr)
├── requirements.txt    ← Just "flask"
├── internship.db       ← Auto-created SQLite database
└── public/
    ├── index.html      ← Public journal view
    └── admin.html      ← Admin panel (add/edit/delete)
```

---

## 🌐 Pages

| URL | What it does |
|-----|-------------|
| `http://localhost:5050` | Public portfolio view with all entries |
| `http://localhost:5050/admin` | Admin panel — add, edit, delete entries |

---

## ➕ Adding May 2026 Entries

### Method 1 — Via Admin Panel (Easiest)
1. Open http://localhost:5050/admin
2. Click **"+ New Entry"**
3. Fill in the form — set Phase to **"May"**
4. Click Save

### Method 2 — Via seed.py (For Bulk Adding)
Open `seed.py` and scroll to the bottom where it says `# ── MAY ──`

Add entries like this:
```python
{
    "date": "2026-05-01", "hours": 5, "phase": "May",
    "work_summary": "Today we started the project phase. Team was finalized and we began planning the app architecture...",
    "learning_outcome": "Gained understanding of team collaboration in real-world project development...",
    "skills": "Flutter, Android Studio, Git",
    "blockers": "No Blockers."
},
```

Then in the terminal run:
```
python seed.py
```

> ⚠️ WARNING: seed.py adds entries on top of existing ones.
> If you already ran it once, don't run it again or you'll get duplicates.
> Only use seed.py if you deleted internship.db and want to start fresh.

### To reset the database completely:
1. Delete `internship.db`
2. Add your May entries to `seed.py`
3. Run `python app.py` — it will reseed automatically

---

## 🔌 API Reference

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/entries` | All entries |
| GET | `/api/entries?phase=May` | Filter by phase |
| GET | `/api/entries/:id` | Single entry |
| POST | `/api/entries` | Create new entry |
| PUT | `/api/entries/:id` | Update entry |
| DELETE | `/api/entries/:id` | Delete entry |
| GET | `/api/stats` | Aggregate stats |

---

## 🎨 Features

**Public View (`/`)**
- Animated hero with your name and internship summary
- Live stats bar (total days, hours, entries)
- Phase filter buttons: Phase 1 / Phase 2 / Phase 3 / April / **May** (new)
- Search bar — search by date, skills, topic, or any keyword
- Every entry is a card — click to expand full work summary + learning outcome + blockers
- Entries with "No Blockers" don't show the blocker section (clean)

**Admin Panel (`/admin`)**
- Stats bar with per-phase entry counts including May
- Table with search + phase filter
- View / Edit / Delete any entry
- Add new entries with a full form
- Default phase for new entries is "May" (auto-set)

---

## 🔮 Future Updates Checklist

Things you can add later:

- [ ] Export journal as PDF
- [ ] Weekly hours chart (bar chart per week)
- [ ] Skills frequency chart
- [ ] Password protect the admin panel
- [ ] Dark/light mode toggle
- [ ] Print-friendly view for internship report submission
- [ ] GitHub integration to show commit history alongside entries

---

## ❓ Common Issues

**"python is not recognized"**
→ Python is not in your PATH. Reinstall Python and check "Add to PATH" during setup.
→ Try `python3` instead of `python`

**"No module named flask"**
→ Run `pip install flask` in the terminal

**Port already in use**
→ Change the port in `app.py`: `app.run(debug=True, port=5051)` and open `http://localhost:5051`

**Database has duplicate entries**
→ Delete `internship.db` and run `python app.py` to start fresh

**Changes not showing in browser**
→ Hard refresh: `Ctrl + Shift + R`
