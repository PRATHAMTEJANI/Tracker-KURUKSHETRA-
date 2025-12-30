from storage import load_data

data = load_data()

print("\n📊 Cognitive Drift Summary\n")

for d in data[-10:]:
    print(f"{d['timestamp']} → {d['state']} ({d['focus_score']})")

avg = sum(d['focus_score'] for d in data) / len(data)
print(f"\n🧠 Average Focus Score: {int(avg)}")

drift = len([d for d in data if d['state'] == "Mind Drift"])
print(f"⚠️ Drift Incidents: {drift}")
