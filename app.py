import json
from flask import Flask, render_template
from data.panels import PANELS, TIMELINE_EVENTS, PHASES

app = Flask(__name__)


def _serializable(obj):
    from datetime import date
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


@app.route("/")
def index():
    timeline_json = json.dumps(TIMELINE_EVENTS, default=_serializable)
    phases_json   = json.dumps(PHASES)
    return render_template(
        "index.html",
        panels=PANELS,
        timeline_events_json=timeline_json,
        phases_json=phases_json,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
