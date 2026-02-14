import random
#game rule
# s == sanke
# w == Water
# g == gun
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}
print("🎮 Welcome to Snake-Water-Gun Game!")
print("Enter 's' for Snake, 'w' for Water, 'g' for Gun")
print("Enter 'q' to Quit the game\n")
user_score = 0
computer_score =0
while True:
    computer = random.choice([-1, 0, 1])
    youstr = input("Enter your choice: ").lower()

    if youstr == 'q':
        print("\nGame Over!")
        break

    if youstr not in youDict:
        print("❌ Invalid input! Try again.\n")
        continue
    you = youDict[youstr]
    print(f"\nYou chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")
    if computer == you:
        print(" 🤝 It's is Draw!")

    elif (you == 1 and computer == -1) or \
         (you == -1 and computer == 0) or \
         (you == 0 and computer == 1):
        print("🎉 You Win!")
        user_score += 1
    else:
        print("😢 You Lose!")
        computer_score += 1
    print(f"\n📊 Score -> You: {user_score} | Computer: {computer_score}")
    print("-" * 50)
print(f"\n🏆 Final Score -> You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("🔥 Congratulations! You won the game!")
elif user_score < computer_score:
    print("💻 Computer won the game!")
else:
    print("🤝 The game ended in a Draw!")