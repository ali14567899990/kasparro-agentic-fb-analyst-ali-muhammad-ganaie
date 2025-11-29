import os
import json
import logging
import time
from datetime import datetime

# ---------------------------
# SCHEMA VERSIONING
# ---------------------------
SCHEMA_VERSION = "1.0.0"

# ---------------------------
# BASIC UTILITIES (KEEP)
# ---------------------------

def ensure_dirs(paths):
    for p in paths:
        os.makedirs(p, exist_ok=True)

def save_json(obj, path):
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)

def timestamped_log(path, data):
    save_json(data, path)

# ---------------------------
# LOGGING & OBSERVABILITY
# ---------------------------

def get_logger(agent_name):
    logger = logging.getLogger(agent_name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
    )
    handler.setFormatter(formatter)

    # Prevent duplicate handlers
    if not logger.handlers:
        logger.addHandler(handler)

    return logger

# ---------------------------
# RETRY WITH BACKOFF
# ---------------------------

def retry_with_backoff(func, max_retries=3, min_confidence=0.7):
    """
    Executes a function multiple times until confidence threshold is reached,
    applying exponential backoff between retries.
    """
    last_result = None

    for attempt in range(1, max_retries + 1):
        result = func()
        last_result = result

        conf = result.get("confidence", 0)
        if conf >= min_confidence:
            return result  # success

        # exponential backoff
        time.sleep(1.5 * attempt)

    return last_result  # return the best attempt

# ---------------------------
# STATE SAVING (NEW)
# ---------------------------

def save_state(name, data):
    os.makedirs("state", exist_ok=True)
    with open(f"state/{name}.json", "w") as f:
        json.dump(data, f, indent=2)

# ---------------------------
# SCHEMA VALIDATION
# ---------------------------

def validate_schema(df, expected_fields):
    """
    Validates that all expected fields exist in dataframe.
    Returns:
       (bool, missing_fields_list)
    """
    df_fields = set(df.columns)
    expected_fields = set(expected_fields)

    missing = expected_fields - df_fields

    if missing:
        return False, list(missing)

    return True, []

# ---------------------------
# SCHEMA DRIFT DETECTION
# ---------------------------

def detect_schema_drift(df, expected_fields):
    """
    Detect:
    - missing fields
    - unexpected new fields
    """
    df_fields = set(df.columns)
    expected_fields = set(expected_fields)

    missing = expected_fields - df_fields
    unexpected = df_fields - expected_fields

    return {
        "missing_fields": list(missing),
        "unexpected_fields": list(unexpected),
        "schema_version": SCHEMA_VERSION
    }
