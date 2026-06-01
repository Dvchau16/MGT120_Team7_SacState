from datetime import date

COLORS = {
    "sac_green":      "#043927",
    "sac_green_dark": "#021A0F",
    "sac_green_deep": "#010C05",
    "sac_gold":       "#C4A35A",
    "sac_gold_light": "#E8D5A3",
    "cream":          "#F5F0E6",
}

T_START = date(2026, 6, 1)
T_END   = date(2030, 6, 1)
SPAN    = (T_END - T_START).days

def pct(d):
    return round(((d - T_START).days / SPAN) * 100, 2)

PHASES = [
    {"label": "Phase 0", "stat": "No Cost.",  "start": 0,  "end": 5,  "color": "rgba(4,57,39,0.75)"},
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


PANELS = [
    {
        "id": "p0",
        "type": "masthead",
        "bg": "#010C05",

        "image": "images/SSlogo.jpg",
        "content": {
            "name": "The Hornet Register",
            "subtitle": "Team 7 · MGT 120 · Spring 2026",
        }
    },
    {
        "id": "p1",
        "type": "article_hero",
        "bg": "#021A0F",

        "image": "images/ryan.jpg",
        "image_label": "Student silhouette · laptop at night · campus",
        "kicker": "The Student",
        "headline": "He did everything right.",
        "persona": {
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
                    "label": "4 Years. No Offer.",
                    "desc": "Passed every class the institution required. Did everything they asked. Still no placement.",
                },
            ]
        },
        "body_text": "Business Administration, Class of 2026. He showed up. Passed every class. Did everything the institution asked.",
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
            "We have reviewed your application and appreciate your interest.",
            "After careful consideration, we have decided to move forward with other candidates whose experience more",
            "closely aligns with the requirements of the role.",
            "We wish you the best in your continued search.",
            "",
            "— Recruiting Team",
            " ",
        ],
    },
    {
        "id": "p3",
        "type": "stat_giant",
        "bg": "#010C05",

        "image": None,
        "stat": "Unused.",
        "stat_size": "clamp(52px, 9vw, 120px)",
        "stat_label": "Big Interview is Sacramento State's licensed mock interview platform — free to every enrolled student. Every student surveyed had never opened it. No major requires it.",
        "body_text": "Students found opportunities through a professor or a personal contact — not through Handshake, not the Career Center. The tool exists. The mandate does not.",
    },
    {
        "id": "p4",
        "type": "article",
        "bg": "#021A0F",

        "image": "images/table_empty_chair.png",
        "image_label": "Empty chair at a faculty curriculum table — surrounded by filled chairs",
        "kicker": "Curriculum Design",
        "headline": "Employers are not in this room.",
        "headline_muted_from": "this room.",
        "caption": "Every course at Sacramento State is built against internally-defined learning outcomes. Employers are absent from every stage of writing them.",
        "body_text": "A faculty member told us she doesn't consider employer feedback when building courses — not from indifference, but because the institution never built a door for that signal to walk through.",
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
        "body_text": "Miss the February 6th catalog deadline at any stage and the fix waits another full year. The Geology Department Head is meeting with faculty now. Her change won't appear in the catalog until 2028.",
    },
    {
        "id": "p6",
        "type": "pull_quote",
        "bg": "#021A0F",

        "image": "images/brodd_AI.png",
        "image_label": "(Former) Dept. Chair · Sacramento State",
        "kicker": "Faculty Incentives",
        "quote": "My tenure was based on research publications and service to the school — not because my students got jobs.",
        "attribution": "(Former) Department Chair · Sacramento State",
        "body_text": "The system evaluates faculty on research output and satisfaction scores. Course redesign earns no tenure credit, no protected time, no compensation. The rational move is to leave the existing course alone.",
    },
    {
        "id": "p7",
        "type": "split_stat",
        "bg": "#010C05",

        "image": None,
        "kicker": "Hiring Manager · Primary Interview · On Record",
        "left_stat":  "9 in 10",
        "left_label": "candidates at Sac State career fairs could not articulate their career goal",
        "left_color": "rgba(245,240,230,0.20)",
        "connector": "·",
        "right_stat":  "52%",
        "right_label": "Class of 2023 underemployed within 12 months of graduation (NSSE 2023)",
        "right_color": "#C4A35A",
        "body_text": "In a soft market, the candidates who get the few available jobs have applied experience and warm introductions — exactly what this pipeline produces.",
    },
    {
        "id": "p8",
        "type": "article",
        "bg": "#021A0F",

        "image": "images/geologyAI.png",
        "image_label": "Geology Dept. · Top 10 in CA for professional licensure",
        "kicker": "The Exception",
        "headline": "One department. One person. Doesn't scale.",
        "headline_muted_from": "Doesn't scale.",
        "body_text": "Top 10 in California for professional geologist licensure pass rates. Students at the USGS, CalTrans, state water agencies. The system works — because one department chair knows every hiring manager by name. That's not a system. That's a single point of failure.",
    },
    {
        "id": "p9",
        "type": "three_asks",
        "bg": "#043927",

        "image": None,
        "kicker": "The Turning Point · Three Structural Changes",
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
        "body_text": "This is not a wishlist. Every item below is achievable with existing authority, existing tools, and existing staff.",
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
        "body_text": "Approval timeline cap. Employer-alignment question in tenure review. Competency fast-track. Handshake intake configuration. One workflow update.",
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
        "body_text": "Sacramento has state agencies, health systems, environmental consulting, and technology employers. The constraint is outreach capacity, not employer interest.",
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
            {"number": "31,000", "label": "students in the system"},
            {"number": "100%",   "label": "of majors with a graded mock interview requirement"},
            {"number": "100",    "label": "guaranteed internship slots per semester"},
            {"number": "2029",   "label": "first placement data in the Factbook"},
        ],
        "body_text": "Every student passing through a required junior-year course is in the system. The Factbook shows internship placement rates alongside graduation rates for the first time.",
    },
    {
        "id": "p13b",
        "type": "reframe",
        "bg": "#010C05",

        "image": None,
        "line1": "They're not hiring.",
        "line2": "That's exactly the point.",
        "context": "In a soft market, the candidates who get the few available jobs are the ones with applied experience and a warm introduction. The institution that builds this now isn't scrambling when hiring rebounds. Sacramento State needs to already be at the table.",
    },
    {
        "id": "p14",
        "type": "article",
        "bg": "#043927",

        "image": "images/student_recruiter.jpg",
        "image_label": "Ryan · Offer letter · Year 3",
        "kicker": "Year 3 · Resolution",
        "kicker_muted": True,
        "headline": "He got the job.",
        "headline_color": "#E8D5A3",
        "body_text": "He didn't apply cold. He walked in warm — introduced, prepared, credentialed. His parents get their return on $142,935. The degree meant something because the institution made it mean something.",
    },
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
                "what": "Employer outreach begins immediately. Three signed agreements by December. Each employer commits to two slots and one annual survey. Target: regional tech, health systems, state agencies.",
            },
            {
                "who": "Career Center",
                "when": "Fall 2026",
                "what": "Employer-in-Residence replaces one career fair event. One employer, one department, ten pre-scheduled student meetings through Handshake. The scheduling already works — this is a configuration.",
            },
            {
                "who": "Faculty",
                "when": "Year 2",
                "what": "Capstone course designation. Students produce a portfolio artifact assessed by practitioners drawn from the employer council — not faculty alone.",
            },
        ],
    },
    {
        "id": "p15",
        "type": "close",
        "bg": "#010C05",

        "image": None,
        "headline": "The degree has to mean something.",
        "subtitle": "31,000 students. They did everything right. Now it's the institution's turn.",
        "footer": "The Hornet Register · Team 7 · MGT 120 · Spring 2026",
    },
]
