# Tuntun Mausi Voice Assistant

A fun, Hinglish-speaking Python voice assistant that listens for your wake word and responds to voice commands — built entirely with open-source libraries. Supports browser automation, jokes, time & date queries, and casual Hinglish conversation.

---

## Description

**Tuntun Mausi** is a wake-word-activated voice assistant built in Python. It was created as a hands-on learning project to explore speech recognition, text-to-speech synthesis, and real-world Python automation.

Say **"Tuntun Mausi"** and she wakes up, listens to your command, and responds — in her signature Hinglish style. Whether you want to open a website, hear a joke, or just have a quick chat, Tuntun Mausi has you covered.

---

## Features

- **Wake-word activation** — listens continuously and activates only on "Tuntun Mausi"
- **Text-to-Speech responses** — speaks back using a female voice via `pyttsx3`
- **Browser automation** — opens Google, YouTube, LinkedIn, and GitHub on command
- **Voice-powered web search** — say "search for..." and she Googles it for you
- **Joke teller** — fetches and speaks random jokes using `pyjokes`
- **Time & Date queries** — tells you the current time and date
- **Casual Hinglish conversation** — greetings, small talk, and fun replies
- **ALSA noise suppression** — suppresses Linux audio library error messages for a clean terminal

---

## Tech Stack / Libraries Used

| Library              | Purpose                                       |
| -------------------- | --------------------------------------------- |
| `speech_recognition` | Captures and converts voice input to text     |
| `pyttsx3`            | Offline text-to-speech engine                 |
| `pyjokes`            | Fetches random programming/general jokes      |
| `webbrowser`         | Opens URLs in the default browser             |
| `datetime`           | Retrieves current time and date               |
| `ctypes`             | Suppresses ALSA audio error messages on Linux |

---

## Installation

**Prerequisites:** Python 3.x must be installed. [Download Python here.](https://www.python.org/downloads/)

```bash
# 1. Clone the repository
git clone https://github.com/b-suhas/tuntun-mausi-voice-assistant

# 2. Navigate into the project folder
cd tuntun-mausi-voice-assistant

# 3. Install required libraries
pip install -r requirements.txt
```

> **Linux users:** You may need to install additional system packages for PyAudio and espeak:
>
> ```bash
> sudo apt-get install python3-pyaudio espeak
> ```

> **Windows users:** If `pyaudio` fails to install via pip, download the appropriate `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install manually.

---

## Requirements

| Requirement | Details                                    |
| ----------- | ------------------------------------------ |
| Language    | Python 3.x                                 |
| Microphone  | Required for voice input                   |
| Internet    | Required for Google Speech Recognition API |
| Platform    | Windows / macOS / Linux                    |

---

## How to Run

```bash
python main.py
```

Once started, Tuntun Mausi will greet you and start listening. Say **"Tuntun Mausi"** to wake her up, then give your command.

### Example Interaction

```
[Assistant starts]
🎙️ "Tuntun Mausi is my name..."

[You say]: "Tuntun Mausi"
🎙️ "Ha ji!"
🎙️ "Tuntun Mausi is ready to help you..."

[You say]: "Open YouTube"
🎙️ "YouTube khol diya!"   ← opens YouTube in browser

[You say]: "Tell me a joke"
🎙️ [speaks a random joke]

[You say]: "What's the time?"
🎙️ "Currently the time is 14:35"
```

---

## Voice Commands / Functionalities

### Casual Conversation

| What You Say           | Tuntun Mausi Replies                                |
| ---------------------- | --------------------------------------------------- |
| "Hi" / "Hello" / "Hey" | "Namaste ji!"                                       |
| "How are you?"         | "Main ekdum badhiya!!"                              |
| "How was your day?"    | "My day was wonderful..."                           |
| "What are you doing?"  | "Making laddoos and helping you out!"               |
| "Who are you?"         | "I am Laddoo specialist aur aapki pyari assistant!" |
| "Thank you"            | "Arey koi baat nahi ji!"                            |
| "Bye"                  | "Byeeee jii"                                        |

### Browser & Web Commands

| What You Say         | Action                     |
| -------------------- | -------------------------- |
| "Open Google"        | Opens google.com           |
| "Open YouTube"       | Opens youtube.com          |
| "Open LinkedIn"      | Opens linkedin.com         |
| "Open GitHub"        | Opens github.com           |
| "Search for [topic]" | Google searches your query |

### Information Commands

| What You Say       | Action               |
| ------------------ | -------------------- |
| "Tell me a joke"   | Speaks a random joke |
| "What's the time?" | Tells current time   |
| "What's the date?" | Tells today's date   |

### Exit Commands

| What You Say    | Action                                |
| --------------- | ------------------------------------- |
| "Exit" / "Quit" | Says goodbye and closes the assistant |

---

## Project Structure

```
tuntun-mausi-voice-assistant/
│
├── main.py            # Main assistant logic (wake word + command handler)
├── requirements.txt   # All required Python dependencies
└── README.md          # Project documentation
```

---

## Future Improvements

- [ ] **Custom wake word engine** — replace Google STT with an offline wake-word detector (e.g., Porcupine)
- [ ] **Weather updates** — fetch and speak live weather using the OpenWeatherMap API
- [ ] **Music playback** — play songs directly from YouTube or Spotify
- [ ] **Reminders & alarms** — set and manage voice-triggered reminders
- [ ] **Wikipedia summaries** — "Tell me about [topic]" using the `wikipedia` library
- [ ] **GUI dashboard** — a minimal Tkinter window showing the assistant's status and last command
- [ ] **Conversation memory** — remember context across multiple commands in one session
- [ ] **More Hinglish personality** — expand casual conversation responses with randomized replies

---

## 👤 Author

**B SUHAS**

- GitHub: [@b-suhas](https://github.com/b-suhas)
- LinkedIn: [B SUHAS](https://www.linkedin.com/in/b-suhas)

---

Feel free to fork this project, open issues, or submit pull requests. Contributions are welcome!
