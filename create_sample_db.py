# create_sample_db.py
# Creates a sample SQLite database with player_progress and save_log tables.
import sqlite3
import os

DB = "game_db.sqlite"
if os.path.exists(DB):
    print("Removing existing DB for fresh start.")
    os.remove(DB)

conn = sqlite3.connect(DB)
c = conn.cursor()
c.execute('''
CREATE TABLE player_progress (
    player_id INTEGER PRIMARY KEY,
    player_name TEXT,
    level INTEGER,
    last_played TEXT
)
''')
c.execute('''
CREATE TABLE save_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    save_status TEXT,
    saved_at TEXT,
    FOREIGN KEY(player_id) REFERENCES player_progress(player_id)
)
''')
# insert sample players
players = [
    (1, 'Alice', 5, '2025-09-01'),
    (2, 'Bob', 3, '2025-09-02'),
    (3, 'Carlos', 7, '2025-09-03'),
]
c.executemany("INSERT INTO player_progress (player_id, player_name, level, last_played) VALUES (?,?,?,?)", players)
# insert save logs but miss one to create an integrity issue for demonstration
save_logs = [
    (1,'OK','2025-09-01 10:00'),
    (2,'OK','2025-09-02 11:00'),
    # note: player 3 intentionally has no save_log -> integrity issue
]
for p_id, status, ts in save_logs:
    c.execute("INSERT INTO save_log (player_id, save_status, saved_at) VALUES (?,?,?)", (p_id, status, ts))
conn.commit()
conn.close()
print("Sample DB created:", DB)
