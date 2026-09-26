# MLB Helper

A small Flask web server that presents a collection of infographic HTML pages.
The left sidebar lists the pages (ordered by original creation date); clicking a
page renders it in the right 80% of the window via an iframe.

## Project layout

```
.
├── app.py              # Flask server + ordered page manifest
├── templates/
│   └── index.html      # sidebar + viewer UI
├── pages/              # the infographic HTML files
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

To add, remove, or reorder pages, edit the `PAGES` list in `app.py` and drop the
HTML file in `pages/`. Order in that list is the order shown in the sidebar.

## Run locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py            # http://localhost:8080
```

## Deploy to Cloud Run

From this directory, with the `gcloud` CLI authenticated and a project selected:

```bash
gcloud run deploy mlb-helper \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```

This builds the container from the `Dockerfile`, pushes it, and deploys. Cloud
Run injects the `PORT` env var, which gunicorn binds to automatically. The
command prints the public service URL when it finishes.
