# SehatBot – LLM-Based Health Assistant in Flutter

SehatBot is a mobile application built with Flutter that uses a locally hosted Language Model (LLM) to provide intelligent health-related chat assistance to users. It is designed to run offline by connecting to a lightweight LLM API via a local server.

## 🚀 Features

- Chat interface for user health queries
- Integration with a locally hosted LLM API
- Responsive and modern Flutter UI
- Offline support via local server connection
- Clean, modular architecture for easy customization

## 🛠️ Tech Stack

- **Flutter** – Frontend mobile app
- **Python** + **Flask/FastAPI** – Backend for LLM API
- **GPT-2 / DistilGPT2** – LLM (fine-tuned)
- **VS Code** – IDE for Flutter & Python
- **Google Colab** – Used for LLM training

## 📦 Project Structure

```bash
project_root/
│
├── lib/                    # Flutter source code
│   ├── main.dart
│   └── screens/
│
├── backend/                # Python backend for LLM
│   └── llm_flask_api.py
│
├── models/                 # LLM model files
│
├── README.md
└── pubspec.yaml
```

## 📲 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/ahsaansattar/sehatbot_flutter_app.git
   cd sehatbot_flutter_app

2. **Run the LLM API locally**
    ```bash
    cd backend
    python llm_flask_api.py

3. **Launch the Flutter app**
    ```bash
    flutter pub get
    flutter run

## 🤖 Future Plans

- Add speech-to-text and text-to-speech

- Deploy on Android/iOS

- Improve LLM accuracy with medical dataset

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Ahsaan S.
📧 ahsaansattar@gmail.com
🌐 GitHub: @iamahsaansattar
