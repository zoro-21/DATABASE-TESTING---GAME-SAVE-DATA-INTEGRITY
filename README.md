# DATABASE-TESTING---GAME-SAVE-DATA-INTEGRITY
(SQLite)
This project demonstrates automated integrity checks for saved game data.

## Why SQLite?
- Lightweight, no DB server setup.
- Fully runnable locally and easy to inspect.

## Setup
1. Python 3.8+
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   pip install -r requirements.txt
   ```
2. Create sample DB:
   ```bash
   python create_sample_db.py
   ```
   This creates `game_db.sqlite` with sample tables and data.
3. Run tests:
   ```bash
   python db_test.py
   ```
   Results are saved to `reports/integrity_report.csv`.
