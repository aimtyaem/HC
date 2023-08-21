# Create a new Scanner object to read input from the console.
scanner = input

# Print a welcome message to the user.
print("Welcome to the interview feedback form.")

# Ask the user to rate their overall experience on a scale of 1 to 5, where 1 is "very bad" and 5 is "very good".
print("How would you rate your overall experience with the interview?" +
      "\n1. Very bad" +
      "\n2. Bad" +
      "\n3. Neutral" +
      "\n4. Good" +
      "\n5. Very good")

# Read the user's response.
rating = int(scanner())

# Ask the user to provide a comment about their experience.
print("Please provide a comment about your experience.")

# Read the user's comment.
comment = scanner()

# Print a thank you message to the user.
print("Thank you for your feedback.")

