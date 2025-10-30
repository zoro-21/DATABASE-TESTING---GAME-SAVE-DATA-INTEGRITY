# db_test.py
# Runs integrity checks on the sample game DB and writes a CSV report.
import sqlite3
import pandas as pd
import os

DB = "game_db.sqlite"
if not os.path.exists(DB):
    print("Database not found. Run create_sample_db.py first.")
    raise SystemExit

conn = sqlite3.connect(DB)
query_missing_save = '''
SELECT p.player_id, p.player_name, p.level, p.last_played
FROM player_progress p
LEFT JOIN save_log s ON p.player_id = s.player_id
WHERE s.log_id IS NULL
'''
df_missing = pd.read_sql(query_missing_save, conn)

os.makedirs("reports", exist_ok=True)
out_csv = "reports/integrity_report.csv"
df_missing.to_csv(out_csv, index=False)
print("Integrity report written to", out_csv)
if df_missing.empty:
    print("No missing saves found. Database integrity checks passed.")
else:
    print("Missing saves detected for players:")
    print(df_missing)
conn.close()
