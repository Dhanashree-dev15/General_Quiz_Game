import json

print("=" * 60)
print("🎯            WELCOME TO QUIZ GAME          🎯")
print("=" * 60)

name = input("👤 Enter Your Name: ")

print(f"\n😊 Hello, {name}! Best of Luck.")
input("👉 Press Enter to Start the Quiz...")

print("\nLoading Questions...")
print("=" * 60)

with open("questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

score = 0

for i, q in enumerate(questions, start=1):

    print("\n" + "=" * 60)
    print(f"📖 Question {i} of {len(questions)}")
    print("=" * 60)

    print(q["question"])
    print()

    for index, option in enumerate(q["options"], start=1):
        print(f"{index}. {option}")

    while True:
        choice = input("\n👉 Enter Your Answer (1-4): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(q["options"]):
            break
        else:
            print("⚠️ Please Enter a Valid Option (1-4).")

    selected = q["options"][int(choice) - 1]

    if selected == q["answer"]:
        print("\n✅ Correct Answer!")
        score += 1
    else:
        print("\n❌ Wrong Answer!")
        print("✅ Correct Answer:", q["answer"])

print("\n" + "=" * 60)
print("🏆              QUIZ COMPLETED              🏆")
print("=" * 60)

percentage = (score / len(questions)) * 100

print(f"👤 Name       : {name}")
print(f"📚 Total      : {len(questions)}")
print(f"✅ Correct    : {score}")
print(f"❌ Wrong      : {len(questions)-score}")
print(f"📊 Percentage : {percentage:.2f}%")

print("\n🎖️ Grade:")

if percentage >= 90:
    print("🌟 A+ (Outstanding)")
elif percentage >= 75:
    print("🥇 A (Excellent)")
elif percentage >= 60:
    print("🥈 B (Good)")
elif percentage >= 40:
    print("🥉 C (Average)")
else:
    print("📚 F (Need More Practice)")

print()

if percentage >= 90:
    print("🎉 Amazing! You are a Champion!")
elif percentage >= 75:
    print("👏 Very Good! Keep it up.")
elif percentage >= 60:
    print("👍 Good Job! Practice a little more.")
elif percentage >= 40:
    print("🙂 Nice Try! Keep Learning.")
else:
    print("💪 Don't Give Up! Practice Makes Perfect.")

print("=" * 60)
print("🙏 Thank You For Playing!")
print("=" * 60)