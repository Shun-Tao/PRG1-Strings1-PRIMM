def clean(entry):
    return entry.strip().lower().rstrip(".") # Added rightstrip


signups = [
    "  Alice@Example.com ",
    "alice@example.com",
    "BOB@example.com  ",
    "bob@Example.com",
    "carol@example.com",
    "alice@example.com.", # Added another item
]

accepted = []

for entry in signups:
    cleaned = clean(entry)
    if cleaned in accepted:
        print(f"Rejected, already signed up: {cleaned}")
    else:
        accepted.append(cleaned)
        print(f"Accepted: {cleaned}")

print(f"{len(accepted)} unique sign-ups from {len(signups)} entries.") # 3 unique sign-ups from 5 entries
