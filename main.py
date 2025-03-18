import streamlit as st
from image import trigent_logo
from server import generate_article

# Set page configuration
st.set_page_config(
    page_title="Trigent AI Studio", layout="wide", initial_sidebar_state="expanded"
)

# Custom CSS for aesthetics
st.markdown(
    """
    <style>
        .main {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .sidebar .sidebar-content {
            font-size: 16px;
        }
        .stButton>button {
            background-color: #2c3e50;
            color: #ffffff;
            border: none;
            padding: 0.5em 1em;
            border-radius: 5px;
        }
        hr {
            border: 0;
            height: 1px;
            background: #ddd;
            margin: 2em 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Title and Introduction
st.title("Trigent AI Studio Email-Classifier")
st.markdown(
    """
Welcome to **Trigent AI Studio** – your next-generation platform for creating, deploying, and managing AI-driven workflows.
Experience the power of an intuitive interface combined with advanced AI capabilities designed to elevate your business.
"""
)

# Overview Section
st.header("Platform Overview")
st.markdown(
    """
**Discover the Advantages of Trigent AI Studio:**

- **Intuitive Visual Interface:** Easily design and manage AI workflows with our user-friendly drag-and-drop system.
- **Customizable Solutions:** Adapt every aspect of your workflow to meet your unique business requirements.
- **Scalability & Robustness:** Ideal for both small projects and enterprise-level deployments.
- **Innovative & Open-Source:** Built on a strong, community-driven foundation with ongoing enhancements.
"""
)

st.markdown("---")

# Interactive API Chat Section
st.header("Interactive API Chat")
st.markdown(
    "Below is a chat interface that demonstrates how Trigent AI Studio processes your queries **with full context**."
)

# 1) Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2) Display all messages so far
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 3) Get user input from the chat box
user_input = st.text_input(label="Enter your email content...", placeholder="Enter your email content...")

if user_input:
    # Show the user's message
    with st.chat_message("user"):
        st.write(user_input)
    # Store user message in session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 4) Build the conversation prompt from the entire history
    #    so the LLM can recall all prior messages
    full_conversation = "You are a helpful assistant. Use the conversation below to inform your next response.\n\n"
    for message in st.session_state.messages:
        role = "User" if message["role"] == "user" else "Assistant"
        full_conversation += f"{role}: {message['content']}\n"
    # Append a final line for the LLM to complete
    full_conversation += "Assistant:"

    # 5) Generate the assistant's response, passing the entire conversation
    with st.spinner("Thinking..."):
        try:
            response = generate_article({"question": full_conversation})
            response_text = response.get("text", "No response received.")
        except Exception as e:
            response_text = f"An error occurred: {e}"

    # 6) Display assistant response and store it
    with st.chat_message("assistant"):
        st.write(response_text)
    st.session_state.messages.append({"role": "assistant", "content": response_text})

# Sidebar
st.sidebar.image(trigent_logo)
st.sidebar.header("About Trigent AI Studio")
st.sidebar.markdown(
    """
Trigent AI Studio is a cutting-edge platform that simplifies the creation of AI workflows, enabling you to harness modern AI technology with ease.

**Our Mission:**  
To empower organizations by providing a flexible and user-friendly platform that drives innovation through seamless AI integration.

**Key Features:**
- Visual Workflow Builder: Create complex AI flows with minimal coding.
- Powerful API Integration: Connect effortlessly with custom AI models and services.
- Community-Driven Development: Benefit from continuous improvements and shared expertise.

For more information, explore our [GitHub Repository](https://github.com/saifpashaTrigent/AiStudio).
"""
)
st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 Trigent AI Studio. All rights reserved.")
