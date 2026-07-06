secret_num = 9
guess_count = 0
guess_limit = 3
print(" welcom to my guessing number game ")
print(" i have throught number between 1 and 10 try to guess it ! ")
# While loop that runs until the user runs out of guesses
while guess_count < guess_limit:
    user_guess= int(input("entre your guess : ")
    guess_count+= 1
  if user_guess == secret_num:
      print(" congratulation !! you WON ")
      break
else:
print(" wrong guess try again!)
# If the loop ends and the user hasn't guessed correctly
if guess_count == guess_limit and user_guess != secret_num:
    print("\nGame Over! The correct number was 9.")
  
