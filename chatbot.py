import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r'\bhi\b|\bhello\b|\bhey\b', user_input):
        return "Hello! How can I help you today?"

    elif re.search(r'product|item|service', user_input):
        return "We offer electronics, clothing, and home appliances."

    elif re.search(r'price|cost|rate', user_input):
        return "Our prices vary by product. Please specify the item name."

    elif re.search(r'order|delivery|status', user_input):
        return "Please provide your order ID to check the status."

    elif re.search(r'contact|support|help', user_input):
        return "You can contact our support at support@example.com."

    elif re.search(r'thank', user_input):
        return "You're welcome! 😊"

    elif re.search(r'exit|bye|quit', user_input):
        return "Thank you for visiting! Have a great day 👋"

    else:
        return "Sorry, I didn't understand that. Please try again."
