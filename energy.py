import streamlit as st

# Set up greeting message
st.sidebar.title("Energy Consumption Chatbot")
st.sidebar.write("Enter a message to start a conversation with the chatbot")

# Define conversation logic
def energy_chatbot(msg):
    # Convert input message to lowercase
    msg = msg.lower()

    # Define energy-related keywords
    energy_keywords = ["energy", "conservation", "save", "usage", "waste"]
    carbon_keywords =["carbon foot print"]
    renewable_keywords=["renewable","fossil fuels"]
    appliance_keywords = ["appliances", "electronics", "devices", "power", "usage",]
    lighting_keywords = ["lighting", "bulbs", "led", "efficiency"]

    # Check for relevant keywords in message and respond accordingly
    if any(word in msg for word in energy_keywords):
        response = "Energy consumption refers to the practice of reducing the amount of energy used in various processes and activities without sacrificing the quality of the end product or service. This can be achieved by adopting more efficient technologies, changing our behaviors and habits, and reducing waste.\nHere are some energy conservation tips: \n\n- Use energy-efficient appliances and electronics \n- Turn off appliances and electronics when not in use \n- Use power strips to reduce standby power usage \n- Keep your home well-insulated"
    elif any(word in msg for word in carbon_keywords):
        response ="Carbon footprint refers to the amount of greenhouse gas emissions, primarily carbon dioxide, that is released into the atmosphere as a result of human activities such as driving a car, using electricity, and consuming food or goods. It is a measure of the impact of these activities on the environment, specifically on climate change. The carbon footprint is typically measured in units of carbon dioxide equivalents (CO2e), which takes into account the different potency of other greenhouse gases such as methane and nitrous oxide. The goal of reducing carbon footprint is to mitigate climate change and its effects on the environment and human health.\nHere are some basic ideas related to carbon footprint:\n 1.Greenhouse gases: The primary greenhouse gases that contribute to global warming are carbon dioxide (CO2), methane (CH4), and nitrous oxide (N2O), as well as some fluorinated gases.\n2.Emissions sources: Carbon emissions come from a variety of sources including burning fossil fuels for transportation and energy, deforestation and land use changes, agricultural activities such as livestock farming and fertilizer use, and industrial processes.\n3.Impact: Climate change caused by increased greenhouse gas emissions has a wide range of negative impacts, including rising sea levels, more extreme weather events, food and water shortages, and loss of biodiversity.Carbon footprint reduction: Reducing one's carbon footprint can be achieved through a variety of strategies, including increasing energy efficiency, using renewable energy sources, reducing consumption of meat and dairy products, driving less, and reducing waste.\n4.Carbon offsetting: Carbon offsetting is the practice of investing in projects that reduce greenhouse gas emissions, such as renewable energy projects, to compensate for one's own emissions.\n Key Advantage is Enables modern living\n Key Disadvantage Resource depletion "
    elif any(word in msg for word in appliance_keywords):
        response = "Using energy-efficient appliances and electronics, and turning them off when not in use, can help reduce your energy usage."
    elif any(word in msg for word in renewable_keywords):
        response = "Sustainable energy, also known as renewable energy, refers to energy sources that are obtained from natural resources that can be replenished or regenerated over time, such as solar, wind, hydropower, geothermal, and biomass. \nUnlike fossil fuels, which are finite and non-renewable, sustainable energy sources have a lower environmental impact and do not contribute to climate change or air pollution.Sustainable energy plays a critical role in the transition to a low-carbon economy and in the mitigation of climate change. It offers numerous benefits, such as reducing greenhouse gas emissions, improving energy security and independence, creating jobs, and increasing access to affordable and clean energy. As a result, many countries and organizations have set ambitious goals to increase their use of sustainable energy and reduce their dependence on fossil fuels."
    elif any(word in msg for word in lighting_keywords):
        response = "Switching to LED light bulbs and turning off lights when you leave a room can save a lot of energy over time."
    else:
        response = "I'm sorry, I'm not sure how to help with that. Please ask me about energy conservation!"

    return response

# Set up conversation interface
user_input = st.text_input("You:", "")
if user_input:
    bot_response = energy_chatbot(user_input)
    st.text_area("Bot:", bot_response)
