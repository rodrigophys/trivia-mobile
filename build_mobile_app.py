#!/usr/bin/env python3
from pathlib import Path
import sqlite3, json, shutil, sys

PROJECT = Path.home() / "Documents" / "CANON" / "Python Trivia Code"
DB = PROJECT / "trivia.db"
HERE = Path(__file__).resolve().parent
DIST = HERE / "dist"

if not DB.exists():
    raise SystemExit(f"Could not find: {DB}")

DIST.mkdir(exist_ok=True)

def rows(con, table):
    return [dict(r) for r in con.execute(f"SELECT * FROM {table}")]

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row

payload = {
    "questions": rows(con, "questions"),
    "associations": rows(con, "associations"),
    "attempts": rows(con, "attempts"),
    "learning_state": rows(con, "learning_state"),
    "association_attempts": rows(con, "association_attempts"),
    "association_learning_state": rows(con, "association_learning_state"),
}
con.close()

(DIST / "data.json").write_text(
    json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
    encoding="utf-8"
)

for name in ["index.html", "manifest.webmanifest", "sw.js"]:
    shutil.copy2(HERE / name, DIST / name)

print("✓ Mobile app built from your CURRENT trivia.db")
print(f"✓ Questions: {len(payload['questions'])}")
print(f"✓ Associations: {len(payload['associations'])}")
print(f"✓ Existing attempts exported: {len(payload['attempts'])}")
print()
print(f"READY FOLDER: {DIST}")
print()
print("Upload the CONTENTS of that dist folder to a static host.")
