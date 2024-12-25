import streamlit as st
from langchain_groq import ChatGroq
from PIL import Image
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

## Set upi the Stramlit app
st.set_page_config(page_title="Maths Problem Solver And Data Search Assistant",page_icon="🧮")

title_container = st.container()
col1, col2 = st.columns([1, 5])
image = Image.open('technical-support.png')
with title_container:
    with col1:
        st.image(image, width=90)
    with col2:
        st.markdown('<h2 style="color: white;">MathsGPT : Maths Problem Solver</h2>',
                    unsafe_allow_html=True)

# st.title("MathsGPT : Maths Problem Solver")

groq_api_key = st.sidebar.text_input(label="Groq API Key", type="password")

# Add better error handling for API key
if not groq_api_key.strip():  # Check for empty strings or whitespace
    st.error("⚠️ Please add your Groq API key to continue")
    st.stop()

try:
    llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)
except Exception as e:
    st.error(f"Error initializing ChatGroq: {str(e)}")
    st.stop()

## Initializing the tools
wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_tool=Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the Internet to find the various information about the topics mentioned"

)

## Initializa the MAth tool

math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for answering math related questions. Only input mathematical expression to get the answer."
)

prompt = """
You're a mathematical assistant tasked with solving users' mathematical questions. Please:
1. Break down the problem into steps
2. Show your logical reasoning
3. Provide a clear, detailed explanation
4. Include the final answer

Question: {question}
Answer:
"""

prompt_template=PromptTemplate(
    input_variables=["question"],
    template=prompt
)

## Combine all the tools into chain
chain=LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool=Tool(
    name="Reasoning tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

## initialize the agents

assistant_agent=initialize_agent(
    tools=[wikipedia_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hi! I'm a Math chatbot who can help you solve mathematical problems. Feel free to ask any math-related questions!"
        }
    ]

# Add a clear button
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = [st.session_state.messages[0]]  # Keep only the welcome message
    st.rerun()

# Improve question input
question = st.text_area(
    "Enter your question:",
    placeholder="Type your math question here...",
    help="You can ask any math-related question, including word problems, calculations, or mathematical concepts.",
    key="question_input"
)

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

## LEts start the interaction
if st.button("Answer"):
    if question.strip():  # Check for empty strings or whitespace
        try:
            with st.spinner("🤔 Thinking..."):
                st.session_state.messages.append({"role": "user", "content": question})
                st.chat_message("user").write(question)

                st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
                response = assistant_agent.run(question, callbacks=[st_cb])  # Fixed: pass question directly, not message history
                
                st.session_state.messages.append({'role': 'assistant', "content": response})
                st.write('### Response:')
                st.success(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("⚠️ Please enter a question before clicking Answer")









