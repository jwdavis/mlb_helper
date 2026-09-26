"""MLB Helper — a small Flask app that serves a set of infographic HTML pages.

A left sidebar lists the available pages; clicking one renders it in the right
80% of the window. Pages are ordered by their original creation date (baked in
below, since filesystem timestamps don't survive a Cloud Run container build).
"""

import os

from flask import Flask, abort, render_template, send_from_directory

app = Flask(__name__)

PAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages")

# Ordered by original file creation date (oldest first). Each entry is the
# on-disk filename plus the human-friendly title shown in the sidebar.
PAGES = [
    ("mlb-overview.html",          "MLB Race to October — Overview"),
    ("data-foundation.html",       "The Data Foundation"),
    ("rag-retrieval-pattern.html", "RAG · The Retrieval Pattern"),
    ("chat-to-workflow.html",      "From Chat to Workflow"),
    ("scaffold-brief-agent.html",  "Scaffold the Brief Agent"),
    ("fan-facing-agent.html",      "The Fan-Facing Agent"),
    ("cx-agent-studio.html",       "What is CX Agent Studio"),
    ("reading-instructions.html",  "Reading the Instructions"),
    ("front-office-analyst.html",  "The Front Office Analyst"),
    ("deploy-agent-runtime.html",  "Deploy to Agent Runtime"),
]

# Filenames we're allowed to serve, for path-traversal safety.
ALLOWED = {filename for filename, _ in PAGES}


@app.route("/")
def index():
    return render_template("index.html", pages=PAGES)


@app.route("/pages/<path:filename>")
def page(filename):
    if filename not in ALLOWED:
        abort(404)
    return send_from_directory(PAGES_DIR, filename)


@app.route("/healthz")
def healthz():
    return "ok", 200


if __name__ == "__main__":
    # Cloud Run provides the port via the PORT env var (defaults to 8080).
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
