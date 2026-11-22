#!/usr/bin/env python3
"""Fetch AQW server boosts from the Artix calendar and write boosts/boosts.json.

Same source and parsing as aqw-lodestar and aqw-wiki-enhanced: the calendar page
embeds FullCalendar events as JS objects ({title: '...', start: 'YYYY-MM-DD', end: ...}).
The calendar only gives a start date, so end dates follow aqw-wiki-enhanced's convention:
core doubles run 48 h (72 h from a Friday), resource boosts run one day.
"""
import json, re, sys, urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

URL = "https://www.artix.com/calendar/"
OUT = Path(__file__).resolve().parent.parent / "boosts" / "boosts.json"
KEEP_DAYS_BACK = 7

CORE = [  # (kind, keywords)
    ("xp", ["double exp", "double xp"]),
    ("class", ["double class"]),
    ("rep", ["double rep"]),
    ("gold", ["double gold"]),
    ("all", ["double all"]),
]


def classify(title):
    low = title.lower().replace("#", "")
    for kind, keys in CORE:
        if any(k in low for k in keys):
            return "core", kind
    if "boost" in low:
        return "resource", "resource"
    return None, None


def clean(title):
    title = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), title)
    title = title.replace("\\'", "'").strip()
    return re.sub(r"\s+\d{1,2}\.\d{1,2}\.\d{2,4}$", "", title).strip()


def parse(html):
    events = []
    for chunk in re.split(r"title:\s*", html)[1:]:
        t = re.match(r"'((?:[^'\\]|\\.)+)'", chunk)
        s = re.search(r"start:\s*'(\d{4}-\d{2}-\d{2})", chunk)
        if not t or not s:
            continue
        title = clean(t.group(1))
        group, kind = classify(title)
        if not group:
            continue
        start = date.fromisoformat(s.group(1))
        e = re.search(r"end:\s*'(\d{4}-\d{2}-\d{2})", chunk[:400])
        end = date.fromisoformat(e.group(1)) if e else None
        events.append({"title": title, "group": group, "kind": kind, "start": start, "end": end})

    # de-duplicate (the calendar sometimes lists an event twice)
    seen, unique = set(), []
    for ev in sorted(events, key=lambda x: (x["start"], x["title"])):
        key = (ev["title"], ev["start"])
        if key not in seen:
            seen.add(key)
            unique.append(ev)

    for i, ev in enumerate(unique):
        if ev["end"] and ev["end"] > ev["start"]:
            continue  # calendar gave a real (exclusive) end date
        days = 1 if ev["group"] == "resource" else (3 if ev["start"].weekday() == 4 else 2)
        end = ev["start"] + timedelta(days=days)
        # a core boost stops when the next core boost starts
        nxt = next((o for o in unique[i + 1:] if o["group"] == ev["group"] and o["start"] > ev["start"]), None)
        if nxt and ev["group"] == "core" and nxt["start"] < end:
            end = nxt["start"]
        ev["end"] = end
    return unique


def main():
    req = urllib.request.Request(URL, headers={"User-Agent": "icefritz.me boost tracker (+https://icefritz.me/boosts/)"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    events = parse(html)
    if not events:
        sys.exit("No boosts found on the calendar; leaving the old file in place.")
    cutoff = date.today() - timedelta(days=KEEP_DAYS_BACK)
    boosts = [
        {"name": ev["title"], "group": ev["group"], "kind": ev["kind"],
         "start": ev["start"].isoformat(), "end": ev["end"].isoformat()}
        for ev in events if ev["end"] >= cutoff
    ]
    data = {"source": URL, "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "boosts": boosts}
    old = json.loads(OUT.read_text()) if OUT.exists() else {}
    if old.get("boosts") == boosts:
        print("No change in boosts.")
        return
    OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print(f"Wrote {len(boosts)} boosts to {OUT}")


if __name__ == "__main__":
    main()
