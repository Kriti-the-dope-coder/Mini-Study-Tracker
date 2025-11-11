# Mini Study Tracker
# Features:
# - Multi-user (in memory): data[name][subject] -> list of entries
# - Add entry: Subject, Topic, Confidence (1–3)
# - View summary: topics list + average confidence; weakest & strongest
# - Mood reflector: choose a mood for advice/quote

data = {}

def ensure_user_bucket(name: str):
    if name not in data:
        data[name] = {}
    return data[name]

def add_entry(user_bucket):
    print("\n Add Study Entry")
    subject = input("Enter Subject: ").strip().title()
    while not subject:
        subject = input("Subject cannot be empty. Enter Subject: ").strip().title()

    topic = input("Enter Topic: ").strip().title()
    while not topic:
        topic = input("Topic cannot be empty. Enter Topic: ").strip().title()

    # Confidence input with validation (must be 1, 2, or 3)
    while True:
        raw = input("Enter confidence level (1=no, 2=somewhat, 3=full): ").strip()
        if raw.isdigit() and int(raw) in (1, 2, 3):
            confidence = int(raw)
            break
        print("Please enter 1, 2, or 3.")

    entry = {"Topic": topic, "Confidence": confidence}

    if subject not in user_bucket:
        user_bucket[subject] = []
    user_bucket[subject].append(entry)

    # Tiny motivational line
    if confidence == 1 or confidence == 2 or confidence == 3:
        print("Logged")

def compute_summary_rows(user_bucket):
    """
    Returns a list of rows: [{ 'Subject', 'TopicsCSV', 'AvgConf', 'Count' }]
    TopicsCSV lists unique topics in insertion order; AvgConf rounded to 1 decimal.
    """
    rows = []
    for subject, entries in user_bucket.items():
        if not entries:
            continue
        # topics list
        topics = [e["Topic"] for e in entries]
        # keep order, remove duplicates lightly
        seen, uniq_topics = set(), []
        for t in topics:
            if t not in seen:
                seen.add(t)
                uniq_topics.append(t)
        topics_csv = ", ".join(uniq_topics)

        # average confidence
        avg = sum(e["Confidence"] for e in entries) / len(entries)
        avg = round(avg, 1)

        rows.append({
            "Subject": subject,
            "TopicsCSV": topics_csv,
            "AvgConf": avg,
            "Count": len(entries),
        })
    return rows

def print_summary(user_bucket):
    print("\n📊 Summary")
    if not user_bucket or all(len(v) == 0 for v in user_bucket.values()):
        print("No entries yet.")
        return

    rows = compute_summary_rows(user_bucket)
    # sort by subject name for stable display
    rows.sort(key=lambda r: r["Subject"])

    print(f"{'Subject':14s} {'Topics covered':32s} {'AvgConf':7s}")
    for r in rows:
        topics_show = (r["TopicsCSV"][:29] + '...') if len(r["TopicsCSV"]) > 32 else r["TopicsCSV"]
        print(f"{r['Subject']:14s} {topics_show:32s} {r['AvgConf']:>7.1f}")

    # Weakest = lowest AvgConf; tie -> fewer entries
    weakest = sorted(rows, key=lambda r: (r["AvgConf"], r["Count"]))[0]
    # Strongest = highest AvgConf; tie -> more entries
    strongest = sorted(rows, key=lambda r: (-r["AvgConf"], -r["Count"]))[0]

    print(f"\nWeakest: {weakest['Subject']} (avg {weakest['AvgConf']})")
    print(f"Strongest: {strongest['Subject']} (avg {strongest['AvgConf']})")

def mood_reflector():
    moods = {
        "1": ("Tired",       "Do a 15-minute light review, then take a break."),
        "2": ("Stressed",    "Journal your worries and fear."),
        "3": ("Unmotivated", "Set a 5-minute timer. Don't force yourself to learn, just try to complete a small task."),
        "4": ("Focused",     "Perfect time to tackle your weakest subject first."),
        "5": ("Happy",       "Use your energy to go deeper in one topic you love."),
    }
    print("\n🌿 Mood Reflector")
    print(" 1) Tired  2) Stressed  3) Unmotivated  4) Focused  5) Happy")
    choice = input("Choose your mood (1–5): ").strip()
    if choice in moods:
        name, tip = moods[choice]
        print(f"\nMood: {name}\nAdvice: {tip}")
    else:
        print("Please choose a number 1–5.")

def switch_user():
    new_name = input("\nEnter user name: ").strip().title()
    while not new_name:
        new_name = input("Name cannot be empty. Enter user name: ").strip().title()
    return new_name

# Main Loop
print("Welcome to Study Tracker")
current_name = input("Please enter your name: ").strip().title()
while not current_name:
    current_name = input("Name cannot be empty. Please enter your name: ").strip().title()

print("\nWelcome,", current_name)
user_bucket = ensure_user_bucket(current_name)

while True:
    print("\n 1. Add new study entry\n 2. View summary\n 3. Mood reflector\n 4. Switch user\n 5. Exit")
    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        add_entry(user_bucket)
    elif choice == "2":
        print_summary(user_bucket)
    elif choice == "3":
        mood_reflector()
    elif choice == "4":
        current_name = switch_user()
        print("Switched to:", current_name)
        user_bucket = ensure_user_bucket(current_name)
    elif choice == "5":
        print("\nGoodbye!\n")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 5.\n")
