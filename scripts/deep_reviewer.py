import os
import ast

MAIN_REPO = "/Users/uzair/Documents/binance"
CMD_CENTER = "/Users/uzair/Documents/research-command-center"
OUT_DIR = os.path.join(CMD_CENTER, "communication", "INBOX")

# Add more as we find them
PRIORITY_1_FILES = [
    "scratch/generate_entry_features.py",
    "phase5_2_engine_replay.py",
    "src/engine/youtube_master_scalper.py",
    "src/infrastructure/egress_gate.py",
    "src/research/binance_market_replay.py",
    "experiments/phase5_cost_aware_engine.py"
]

LEAKAGE_KEYWORDS = [
    'shift', 'rolling', 'bfill', 'fillna', 'merge', 'join', 'resample',
    'fit_transform', 'fit', 'transform'
]

def scan_file_for_leakage(file_rel_path):
    full_path = os.path.join(MAIN_REPO, file_rel_path)
    if not os.path.exists(full_path):
        return
        
    print(f"--- Scanning {file_rel_path} ---")
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines):
            for kw in LEAKAGE_KEYWORDS:
                if kw in line:
                    print(f"L{i+1} [{kw}]: {line.strip()}")
    except Exception as e:
        print(f"Error reading {file_rel_path}: {e}")

if __name__ == "__main__":
    for f in PRIORITY_1_FILES:
        scan_file_for_leakage(f)
