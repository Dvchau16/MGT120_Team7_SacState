from datetime import date

# ── Sacramento State Brand Colors ─────────────────────────────────────────────
COLORS = {
    "sac_green":      "#043927",
    "sac_green_dark": "#021A0F",
    "sac_green_deep": "#010C05",
    "sac_gold":       "#C4A35A",
    "sac_gold_light": "#E8D5A3",
    "cream":          "#F5F0E6",
}

# ── Timeline data ──────────────────────────────────────────────────────────────
T_START = date(2026, 6, 1)
T_END   = date(2030, 6, 1)
SPAN    = (T_END - T_START).days

def pct(d):
    return round(((d - T_START).days / SPAN) * 100, 2)

PHASES = [
    {"label": "Phase 0", "stat": "$0 · 5 decisions",  "start": 0,  "end": 5,  "color": "rgba(4,57,39,0.75)"},
    {"label": "Phase 1", "stat": "3 agreements",       "start": 5,  "end": 12, "color": "rgba(4,57,39,0.55)"},
    {"label": "Phase 2", "stat": "12 agreements",      "start": 12, "end": 25, "color": "rgba(10,92,58,0.55)"},
    {"label": "Phase 3", "stat": "25 agreements",      "start": 25, "end": 50, "color": "rgba(10,92,58,0.40)"},
    {"label": "Phase 4", "stat": "50 agreements",      "start": 50, "end": 75, "color": "rgba(196,163,90,0.25)"},
]

TIMELINE_EVENTS = [
    {"color": "#C4A35A", "date": date(2026, 9, 1),  "label": "3 agreements"},
    {"color": "#C4A35A", "date": date(2027, 1, 1),  "label": "12 agreements"},
    {"color": "#C4A35A", "date": date(2027, 9, 1),  "label": "25 agreements"},
    {"color": "#C4A35A", "date": date(2028, 9, 1),  "label": "50 agreements"},
    *[{"color": "#5AAAE8", "date": date(y, m, 1), "label": "Advisory Council"}
      for y, m in [(2027,3),(2027,10),(2028,3),(2028,10),(2029,3),(2029,10)]],
    *[{"color": "#5AD88A", "date": date(y, 10, 1), "label": "Career Fair Survey"}
      for y in [2026, 2027, 2028, 2029]],
    *[{"color": "#E87A5A", "date": date(y, 2, 6), "label": "Feb 6 Deadline"}
      for y in [2027, 2028, 2029, 2030]],
    *[{"color": "#C875E8", "date": date(y, m, 1), "label": "EF Roundtable"}
      for y, m in [(2027,4),(2027,11),(2028,4),(2028,11),(2029,4),(2029,11)]],
]

for ev in TIMELINE_EVENTS:
    ev["position"] = pct(ev["date"])


# ── Panels ─────────────────────────────────────────────────────────────────────
PANELS = [
    # ── HOOK ──────────────────────────────────────────────────────────────────
    {
        "id": "p0",
        "type": "masthead",
        "bg": "#010C05",
        "image": None,
        "content": {
            "name": "The Hornet Register",
            "subtitle": "Sacramento State · Business Administration · MGT 120 · June 2026",
        }
    },
    {
        "id": "p1",
        "type": "article_hero",
        "bg": "#021A0F",
        "image": "images/ryan.jpg",
        "image_label": "Ryan — Student silhouette, laptop at night",
        "kicker": "The Student",
        "headline": "He did everything right.",
        "persona": {
            "byline": "Business Administration Senior · Sacramento State · Class of 2026",
            "sidebar": [
                {
                    "label": "First-Generation Student",
                    "desc": "No alumni network. No internship playbook. No roadmap. The institution was the only guide.",
                },
                {
                    "label": "$142,935",
                    "desc": "The cost of four years for his family — tuition, fees, living expenses. Paid in full.",
                },
                {
                    "label": "4 Years. 0 Internships.",
                    "desc": "Passed every class the institution required. He did everything they asked. Still no offer.",
                },
            ]
        },
        "fake_body": True,
    },
    {
        "id": "p2",
        "type": "stark",
        "bg": "#010C05",
        "image": None,
        "headline": "The degree was supposed to be enough.",
        "dateline": "Sacramento State Career Fair · Spring 2026 · Filed for record",
        "ghost_lines": [
            "Dear Applicant,",
            "We have reviewed your application and appreciate your interest in this position.",
            "After careful consideration, we have decided to move forward with other candidates",
            "whose experience more closely aligns with the requirements of this role.",
            "We appreciate the time you invested and wish you well in your search.",
            "",
            "Sincerely,",
            "Recruiting Team",
        ],
    },
    # ── CONTEXT ───────────────────────────────────────────────────────────────
    # Each panel answers one question: why is this happening?
    {
        "id": "p3",
        "type": "stat_giant",
        "bg": "#010C05",
        "image": None,
        "kicker": "Canvassing Data · On Campus",
        "stat": "0%",
        "stat_label": "of students canvassed had ever used Big Interview — the mock interview platform Sacramento State already licenses. The tool exists. The requirement does not.",
        "fake_body": True,
    },
    {
        "id": "p4",
        "type": "article",
        "bg": "#021A0F",
        "image": "images/empty_chair.jpg",
        "image_label": "Empty chair at a faculty curriculum table — surrounded by filled chairs",
        "kicker": "Curriculum Design",
        "headline": "Employers are not in this room.",
        "headline_muted_from": "this room.",
        "caption": "Every course at Sacramento State is built against internally-defined learning outcomes. Employers are absent from every stage of writing them.",
        "fake_body": True,
    },
    {
        "id": "p5",
        "type": "stat_giant",
        "bg": "#010C05",
        "image": None,
        "stat": "2028",
        "stat_color": "#F5F0E6",
        "stat_size": "clamp(96px, 18vw, 220px)",
        "stat_label": "The year a curriculum change made today reaches a student. The system is working exactly as designed.",
        "fake_body": True,
    },
    {
        "id": "p6",
        "type": "pull_quote",
        "bg": "#021A0F",
        "image": "images/brodd.jpg",
        "image_label": "Professor Brodd — Former Dept. Chair",
        "kicker": "Faculty Incentives",
        "quote": "My tenure was based on research publications and service to the school — not because my students got jobs.",
        "attribution": "Professor Brodd · Former Department Chair · Sacramento State",
        "fake_body": True,
    },
    {
        "id": "p7",
        "type": "split_stat",
        "bg": "#010C05",
        "image": None,
        "kicker": "Hiring Manager · Primary Interview",
        "left_stat":  "9 in 10",
        "left_label": "candidates at Sac State career fairs could not articulate their career goal",
        "left_color": "rgba(245,240,230,0.20)",
        "connector": "·",
        "right_stat":  "52%",
        "right_label": "Class of 2023 underemployed within 12 months of graduation (NSSE 2023)",
        "right_color": "#C4A35A",
        "fake_body": True,
    },
    {
        "id": "p8",
        "type": "article",
        "bg": "#021A0F",
        "image": "images/geology.jpg",
        "image_label": "Geology Dept. — top 10 in CA for licensure",
        "kicker": "The Exception",
        "headline": "One department. One person. Doesn't scale.",
        "headline_muted_from": "Doesn't scale.",
        "fake_body": True,
    },
    # ── SOLUTION ──────────────────────────────────────────────────────────────
    {
        "id": "p9",
        "type": "three_asks",
        "bg": "#043927",
        "image": None,
        "kicker": "The Proposal",
        "asks": [
            {
                "word": "A Pipeline.",
                "note": "Formal employer agreements. 3 by Fall 2026. 50 by Year 3. 100 guaranteed slots per semester."
            },
            {
                "word": "A Signal.",
                "note": "Employer expectations reaching the curriculum before February 6 — every year, on a schedule."
            },
            {
                "word": "An Infrastructure.",
                "note": "A system that works for the student who cannot afford to say no to an offer."
            },
        ],
        "fake_body": True,
    },
    {
        "id": "p10",
        "type": "phase_zero",
        "bg": "#021A0F",
        "image": None,
        "kicker": "Where It Starts · June 2026",
        "cascade": [
            {"value": "5",          "label": "DECISIONS"},
            {"value": "Zero",       "label": "COSTS"},
            {"value": "June 2026",  "label": "START DATE"},
        ],
        "context": "Five decisions the Provost can make this summer. No budget line. No employer at the table. No approval chain beyond the office.",
        "fake_body": True,
    },
    {
        "id": "p11",
        "type": "pipeline_stat",
        "bg": "#010C05",
        "image": None,
        "kicker": "The Employer Pipeline",
        "left_stat":  "3%",
        "left_color": "rgba(245,240,230,0.20)",
        "left_label": "of target reached · fall 2026",
        "right_stat":  "100%",
        "right_color": "#C4A35A",
        "right_label": "50 agreements · year 3 · 100 guaranteed slots/sem",
        "fake_body": True,
    },
    {
        "id": "p12",
        "type": "timeline",
        "bg": "#021A0F",
        "image": None,
    },
    {
        "id": "p13",
        "type": "impact_grid",
        "bg": "#010C05",
        "image": None,
        "kicker": "Year 3 · Full Scale",
        "stats": [
            {"number": "30,200", "label": "students in the system"},
            {"number": "100%",   "label": "of majors with a graded mock interview requirement"},
            {"number": "100",    "label": "guaranteed internship slots per semester"},
            {"number": "2029",   "label": "first year placement data in factbook"},
        ],
        "fake_body": True,
    },
    # ── REFRAME ───────────────────────────────────────────────────────────────
    {
        "id": "p13b",
        "type": "reframe",
        "bg": "#010C05",
        "image": None,
        "line1": "They're not hiring.",
        "line2": "That's exactly the point.",
        "context": "In a soft market, the candidates who get the few available jobs are the ones with applied experience and a warm introduction. The institution that builds this now is not scrambling when hiring rebounds. Sacramento State needs to already be at the table.",
    },
    # ── RESOLUTION ────────────────────────────────────────────────────────────
    {
        "id": "p14",
        "type": "article",
        "bg": "#043927",
        "image": "images/resolution.jpg",
        "image_label": "Ryan — offer letter, Year 3",
        "kicker": "Year 3 · Resolution",
        "kicker_muted": True,
        "headline": "He got the job.",
        "headline_color": "#E8D5A3",
        "fake_body": True,
    },
    # ── IMPLEMENTATION ────────────────────────────────────────────────────────
    {
        "id": "p14b",
        "type": "action_grid",
        "bg": "#021A0F",
        "image": None,
        "kicker": "Who Moves First · Authority Already Exists",
        "actors": [
            {
                "who": "The Provost",
                "when": "June 2026",
                "what": "Five policy changes — cap approval timelines, add employer-alignment question to tenure file, create a competency fast-track, configure intake form, update one workflow. No budget. No Senate vote.",
            },
            {
                "who": "University Enterprises",
                "when": "Now",
                "what": "Employer outreach starts immediately. Three signed agreements by December. Each employer commits to two slots and one annual survey. Target: regional tech, health systems, state agencies.",
            },
            {
                "who": "Career Center",
                "when": "Fall 2026",
                "what": "Replace one career fair event with Employer-in-Residence: one employer, one department, ten pre-scheduled student meetings through Handshake. The scheduling already works — this is a configuration.",
            },
            {
                "who": "Faculty",
                "when": "Year 2",
                "what": "Capstone course designation. Students produce a portfolio artifact assessed by practitioners drawn from the employer council — not faculty alone.",
            },
        ],
    },
    # ── CLOSE ─────────────────────────────────────────────────────────────────
    {
        "id": "p15",
        "type": "close",
        "bg": "#010C05",
        "image": None,
        "headline": "The degree has to mean something.",
        "subtitle": "30,200 students · Questions.",
        "fake_body": True,
    },
]
