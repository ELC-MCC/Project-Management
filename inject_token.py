"""Inject the sync token into index.html before encryption."""
import sys

token = sys.argv[1] if len(sys.argv) > 1 else ""

with open("index.html") as f:
    html = f.read()

html = html.replace("__SYNC_TOKEN__", token)

with open("index.html", "w") as f:
    f.write(html)

print("Token injected")
