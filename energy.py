import streamlit as st

# Set up greeting message
st.sidebar.title("Water Conservation Chatbot")
st.sidebar.write("Enter a message to start a conversation with the chatbot")

# Define conversation logic
def water_chatbot(msg):
    # Convert input message to lowercase
    msg = msg.lower()

    # Define water conservation-related keywords
    conservation_keywords = ["water", "conservation", "save", "usage", "waste"]
    shower_keywords = ["shower", "bath", "faucet"]
    irrigation_keywords = ["irrigation", "lawn", "garden", "plants"]
    consumption_keywords = ["meter", "bill", "monitor"]

    # Check for relevant keywords in message and respond accordingly
    if any(word in msg for word in conservation_keywords):
        response = "Here are some water conservation tips: \n\n- Fix leaky faucets \n- Take shorter showers \n- Water your lawn in the morning or evening \n- Install a low-flow toilet"
    elif any(word in msg for word in shower_keywords):
        response = "Taking shorter showers and turning off the water while you soap up can save a lot of water over time."
    elif any(word in msg for word in irrigation_keywords):
        response = "Consider planting drought-resistant plants or installing a drip irrigation system to conserve water in your garden."
    elif any(word in msg for word in consumption_keywords):
        response = "To monitor your water consumption, you can check your meter or review your water bill. You can also install a smart water meter to track your usage in real-time."
    else:
        response = "I'm sorry, I'm not sure how to help with that. Please ask me about water conservation!"

    return response

# Set up conversation interface
user_input = st.text_input("You:", "")
if user_input:
    bot_response = water_chatbot(user_input)
    st.text_area("Bot:", bot_response)
