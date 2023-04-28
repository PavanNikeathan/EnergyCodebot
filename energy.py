import streamlit as st
# Set up greeting message
st.sidebar.title("Energy Conseumption Chatbot")
st.sidebar.write("Enter a message to start a conversation with the chatbot")
# Define conversation logic
def Energy_chatbot(msg):
    # Convert input message to lowercase
    msg = msg.lower()
# Define conservation-related keywords
energy_keywords = ["energy", "conservation", "save", "usage", "waste"]
appliance_keywords = ["appliances", "electronics", "devices", "power", "usage"]
lighting_keywords = ["lighting", "bulbs", "led", "efficiency"]

# Check for relevant keywords in message and respond accordingly
if any(word in msg for word in energy_keywords):
    response = "Here are some energy conservation tips: \n\n- Use energy-efficient appliances and electronics \n- Turn off appliances and electronics when not in use \n- Use power strips to reduce standby power usage \n- Keep your home well-insulated"
elif any(word in msg for word in appliance_keywords):
    response = "Using energy-efficient appliances and electronics, and turning them off when not in use, can help reduce your energy usage."
elif any(word in msg for word in lighting_keywords):
    response = "Switching to LED light bulbs and turning off lights when you leave a room can save a lot of energy over time."
else:
    response = "I'm sorry, I'm not sure how to help with that. Please ask me about energy conservation!"
return response
# Set up conversation interface
user_input = st.text_input("You:", "")
if user_input:
    bot_response = water_chatbot(user_input)
    st.text_area("Bot:", bot_response)
