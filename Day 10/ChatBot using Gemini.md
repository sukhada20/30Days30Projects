# Gemini 1.5 Flash Chatbot with Gradio UI & Smart Timeout Interceptor
A sleek, conversational AI application built with Python that combines the powerful context window of Google's **Gemini 1.5 Flash** model with an interactive **Gradio web user interface**. 
A standout feature of this repository is its implementation of **asynchronous thread monitoring** to prevent API hangs, ensuring the user interface remains responsive even under slow network conditions or API rate limit delays.

---

## ✨ Key Features
* **Stateful Conversations**: Implements multi-turn conversation memory using Gemini's native chat sessions (`start_chat`), allowing the model to recall previous user prompts and answers seamlessly.
* **Fault-Tolerant Timeout Interceptor**: Wraps API execution in an independent background worker thread (`threading.Thread`). If Google's servers take longer than 10 seconds to respond, the app gracefully interrupts the block and flags a warning instead of freezing the UI.
* **Modern Web Interface**: Built entirely with Gradio (`gr.Blocks`), yielding a fully responsive, clean, and interactive chat interface usable in both local browsers and notebook cells.
* **Instant Session Reset**: Features a "Clear Chat" execution lifecycle that completely purges chat history and instantiates a brand new session token dynamically on the backend.

---

## 🛠️ Architecture & Core Mechanics
The backend architecture ensures stability by decoupling the user interface thread from the external network requests:
```
[ User Inputs Message ] ──> [ Launches Background Worker Thread ]
│
┌───────────────┴───────────────┐
▼                               ▼
[ API returns in <10s ]        [ API hangs beyond 10s ]
│                               │
▼                               ▼
Updates UI Chat History        Intercepts with Timeout Alert
```

---

## 🚀 Tech Stack
* **Language:** Python 3.8+
* **LLM Engine:** Google Generative AI SDK (`gemini-1.5-flash`)
* **Frontend UI:** Gradio (Blocks API)
* **Concurrency:** Python Standard `threading` Library

---

## 💻 Installation & Setup
### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/gemini-gradio-chatbot.git](https://github.com/YOUR_USERNAME/gemini-gradio-chatbot.git)
cd gemini-gradio-chatbot
```
### 2. Install Dependencies
Install the required packages using pip:
```bash
pip install google-generativeai gradio
```
### 3. Acquire Google Gemini API Key
To communicate with the model, you must possess an API key from Google AI Studio.
1. Head over to [Google AI Studio](https://aistudio.google.com/).
2. Generate an API Key and substitute it in the configuration line within the code:
```python
genai.configure(api_key="YOUR_ACTUAL_API_KEY")
```
### 4. Running the Application
If you are running this project locally or inside a Jupyter/Google Colab environment, execute the workspace code block. Gradio will spin up a local server and output a public, shareable tunnel URL:
```bash
python app.py
```
*Expected Output:*
```text
* Running on public URL: [https://xxxxxxxxxxxxxx.gradio.live](https://xxxxxxxxxxxxxx.gradio.live)
This share link expires in 1 week.
```

---

## ⚙️ Hyperparameter Configuration
The implementation configures the `gemini-1.5-flash` engine using the following customized parameters to optimize speed and conciseness:

| Parameter | Value | Description |
| --- | --- | --- |
| **`max_output_tokens`** | `512` | Restricts response sizes to maintain chat speed and prevent token bloat. |
| **`temperature`** | `0.7` | Balances deterministic precision with creative variation. |
| **`timeout_seconds`** | `10` | Hard deadline allocated to background API worker threads. |

---

~ sukhada20
