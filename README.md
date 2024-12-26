# MathsGPT : Maths Problem Solver
[![LangChain](https://img.shields.io/badge/LangChain-Framework-blue)](https://langchain.io/) [![Streamlit](https://img.shields.io/badge/Streamlit-User%20Interface-green)](https://streamlit.io/) [![ChatGroq](https://img.shields.io/badge/ChatGroq-Language%20Model-orange)](https://www.groq.com/) [![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-yellow)](https://python-pillow.org/)


## Overview
MathsGPT is an intuitive and interactive Streamlit application designed to assist users with solving mathematical problems and retrieving data efficiently. It leverages advanced AI capabilities for solving math-related queries, providing logical reasoning, and conducting searches for information via Wikipedia. The application ensures ease of use with its clean interface and robust functionalities.

## Launch Application
In order to view application, click ([Launch App](https://yunus5603-mathsgpt-app-acxexx.streamlit.app/))
![](Screenshot.jpg)
---

## Features

- **Mathematical Problem Solving**: 
  - Breaks down problems into steps.
  - Provides logical reasoning and clear explanations.
  - Offers a detailed final answer for queries.

- **Wikipedia Integration**: 
  - Fetches relevant information from Wikipedia for a wide range of topics.

- **Calculator Tool**: 
  - Handles mathematical expressions with precision.

- **Reasoning Assistance**:
  - Designed for logic-based questions and reasoning tasks.

- **Interactive Chat Interface**:
  - Stores message history for context.
  - Offers a "Clear Chat History" button for resetting sessions.

---

## Tech Stack

- **Streamlit**: For building the interactive UI.
- **LangChain**: Core framework to integrate tools and manage reasoning chains.
- **LangChain Tools**:
  - WikipediaAPIWrapper: To fetch Wikipedia data.
  - LLMMathChain: For solving mathematical queries.
- **Pillow (PIL)**: To manage images.
- **ChatGroq**: LLM backend for handling user queries.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mathsGPT.git
   cd mathsGPT
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Groq API key:
   - Enter your API key in the sidebar when prompted.

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Launch the application and enter your Groq API key.
2. Input your math-related question or search topic in the text area.
3. Click **Answer** to get a detailed response.
4. Use the sidebar to clear the chat history if needed.

---

## Future Enhancements

- Add support for more advanced mathematical topics.
- Integrate additional data sources for broader search capabilities.
- Enhance UI for better user experience.

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to suggest improvements or report bugs.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any questions or feedback, please contact [syunus838@gmail.com].
