import json, time, hashlib

def log_audit(text):
    record = {
        "timestamp": time.time(),
        "file_hash": hashlib.sha256(text.encode()).hexdigest()
    }

    with open("audit/audit_log.json", "a") as f:
        f.write(json.dumps(record) + "\n")
