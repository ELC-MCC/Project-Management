"""Inject the sync token into index.html before encryption.
Reads token from SYNC_TOKEN environment variable (set in CI)."""
import os

token = os.environ.get("SYNC_TOKEN", "")

if not token:
    print("WARNING: No SYNC_TOKEN environment variable set -- leaving placeholder")
    exit(0)

with open("index.html") as f:
    html = f.read()

html = html.replace("__SYNC_TOKEN__", token)

with open("index.html", "w") as f:
    f.write(html)

print("Token injected")
