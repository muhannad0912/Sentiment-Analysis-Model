from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float

def get_mood(input_text: str, *, threshold: float) -> Mood:
    sentiment = TextBlob(input_text).sentiment.polarity
    
    if sentiment >= threshold:
        mood = Mood("😄", sentiment)
    else:
        mood = Mood("😞", sentiment)
        
    return mood

# Set the initial threshold value
threshold = 0.5

# Start the while loop
while True:
    # Get user input
    input_text = input("Enter a text: ")
    
    # Check if the user wants to exit the loop
    if input_text.lower() == "exit":
        print("Exiting the program...")
        break
    
    # Get the mood based on the input text
    mood = get_mood(input_text, threshold=threshold)
    
    # Print the mood emoji and sentiment
    print(f"Mood: {mood.emoji}")
    print(f"Sentiment: {mood.sentiment}")