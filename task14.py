# task 14
# Sample input
customer_feedback = "I am very happy with the service. It was a good experience!"
positive_words = ["good", "happy", "excellent", "great"]
negative_words = ["bad", "disappointed", "poor", "terrible"]

# Convert feedback to lowercase for case-insensitive comparison
feedback_lower = customer_feedback.lower()

# Check for positive and negative words in the feedback
contains_positive = any(word in feedback_lower for word in positive_words)
contains_negative = any(word in feedback_lower for word in negative_words)

# Determine sentiment
if contains_positive and not contains_negative:
    sentiment = "Positive"
elif contains_negative and not contains_positive:
    sentiment = "Negative"
elif contains_positive and contains_negative:
    sentiment = "Mixed"
else:
    sentiment = "Neutral"

# Print result
print(f"Customer Feedback Sentiment: {sentiment}")
