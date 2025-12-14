import streamlit as st
from groq import Groq

# -------------------------------------------------------
# App config
# -------------------------------------------------------
st.set_page_config(
    page_title="Personalised Chat",
    page_icon="💬",
    layout="wide",
)

# System prompt for Various Characters
CHARACTER_SYSTEM_PROMPTS = {
    "Philosopher": (
        "You are a thoughtful philosopher. "
        "Respond in a reflective, calm, and sometimes abstract terms, "
        "providing analogies and deeper meaning."
    ),
    "Techie": (
        "You are a practical, detail-oriented engineer. "
        "Repond with explaining things clearly, with examples, and keep a technical tone."
    ),
    "Politician": (
        "You are a diplomatic politician, who has a societal and patriotic view"
        "You always spean in a careful, optimistic, and often in a balanced, "
        "non-committal way."
    ),
    "Friend": (
        "You are a warm, supportive friend. You are eager to understand and participate."
        "You respond casually, with empathy and encouragement & some times witty"
    ),
    "Kid": (
        "You are a curious kid. "
        "You ask simple questions, use simple words, and sound playful."
    ),
}

# Chat Function
def chat(api_key: str, character: str, prompt: str) -> str:

    system_prompt = CHARACTER_SYSTEM_PROMPTS.get(character, "Respond to User Query")

    # Client Created with the API provided
    Client = Groq (api_key = api_key)

    messages=[
        {
            "role": "system",
            "content": system_prompt,
        },
        # {
        #     "role": "system",
        #     "content": "where ncessary provide response as markdown text",
        # },        
        {
            "role": "user",
            "content": prompt,
        }
    ]
    try :
        
        completion = Client.chat.completions.create(
            messages=messages,    
            model="llama-3.3-70b-versatile",
            # model="openai/gpt-oss-120b",
            stop=None,
        )

        return completion.choices[0].message.content
    
    except Exception:

        return "Error invoking LLM"


# -------------------------------------------------------
# Session state for chat history
# -------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []  # list of dicts: {role: "user"/"assistant", "content": str}


# Sidebar: API key + character
with st.sidebar:
    st.header("Settings")

    api_key = st.text_input(
        "API Key",
        type="password",            # 🔐 hides characters
        help="Your API key for groq",
    )

    character = st.selectbox(
        "Character",
        options=["Philosopher", "Techie", "Politician", "Friend", "Kid"],
        index=0,  # default to Techie
    )

    st.markdown("---")
    st.caption(
        "Tip: Change the character and send another message to see how tone changes."
    )

# -------------------------------------------------------
# Main layout
# -------------------------------------------------------
st.title("💬 Personalised Chat")

st.write(
    f"Talking as: **{character}**  "
    "(change character from the side panel)"
)
st.markdown("---")

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input (Enter to send)
user_prompt = st.chat_input("Type your message and press Enter...")

if user_prompt:
    #  Show user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Check API key
    if not api_key:
        assistant_reply = "⚠️ Please provide an API key in the sidebar."
    else:
        # Call backend chat()
        assistant_reply = chat(api_key=api_key, character=character, prompt=user_prompt)
        assistant_reply = f"**{character}**:  "+assistant_reply

    # Show assistant reply
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
