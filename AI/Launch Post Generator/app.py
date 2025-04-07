import streamlit as st
from openai import OpenAI

# Set up the app title and layout
st.title("🤖 AI Content Generator")
st.markdown("Generate social media posts or newsletter content using GPT!")

# Initialize OpenAI client
client = None

# Sidebar for API key input
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter your OpenAI API key:", type="password")
    if api_key:
        client = OpenAI(api_key=api_key)  # Correct client initialization

# Main content area
content_type = st.selectbox(
    "Select content type:",
    ["Social Media Post", "Newsletter"]
)

prompt = st.text_area(
    "Enter your prompt or topic:",
    placeholder="e.g., 'Write a tweet about data science trends'",
    height=100
)

char_limit = st.slider("Max response length (characters):", 100, 500, 300)

if st.button("Generate Content"):
    if not client:
        st.error("Please enter your OpenAI API key in the sidebar!")
    elif not prompt:
        st.error("Please enter a prompt!")
    else:
        try:
            with st.spinner("Generating..."):
                # Updated API call with chat completions format
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",  # Updated model name
                    messages=[{
                        "role": "user",
                        "content": f"Write a {content_type.lower()} about: {prompt}. Keep it under {char_limit} characters."
                    }],
                    max_tokens=int(char_limit * 0.75),  # Approximate conversion (1 token ≈ 1.3 chars)
                    temperature=0.7,
                )
                generated_text = response.choices[0].message.content  # Correct response access
                st.success("Generated Content:")
                st.write(generated_text)
        except Exception as e:
            st.error(f"Error: {str(e)}")
