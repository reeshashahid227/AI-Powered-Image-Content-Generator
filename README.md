# 🖼️ AI-Powered Image Caption Generator

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-orange?logo=pytorch)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

An AI-powered application that generates meaningful captions from uploaded images using the **BLIP Image Captioning model** and enhances them with **Groq LLM**. Users can customize captions based on style, tone, and language, generate multiple caption suggestions, and export the generated captions.

---

# ✨ Features

| Feature | Description |
|---------|-------------|
| 🖼️ Image Upload | Upload single or multiple images |
| 🤖 Image Caption Generation | Generate captions using the BLIP pretrained model |
| ✨ AI Caption Enhancement | Improve captions using Groq LLM |
| 🎨 Caption Style | Simple, Social Media, Professional, Creative, Marketing |
| 😊 Caption Tone | Neutral, Friendly, Professional, Funny, Emotional |
| 🌍 Language Support | English, Urdu, Roman Urdu |
| 📝 Multiple Captions | Generate multiple AI caption suggestions |
| 📥 Caption Export | Download captions as a TXT file |
| 💻 Interactive UI | Clean and responsive Streamlit interface |

---

# 🏗️ Project Architecture

```text
          User Uploads Image
                  │
                  ▼
     BLIP Image Captioning Model
                  │
        Original Image Caption
                  │
                  ▼
             Groq LLM
                  │
     Caption Enhancement
 (Style • Tone • Language)
                  │
                  ▼
 Multiple AI Caption Suggestions
                  │
                  ▼
          Export as TXT
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Framework | Streamlit |
| Deep Learning | PyTorch |
| Vision Model | BLIP |
| Transformers | Hugging Face Transformers |
| AI Enhancement | Groq LLM |
| Image Processing | Pillow |
| Environment Variables | python-dotenv |

---

# 📂 Project Structure

```text
AI-Powered-Image-Caption-Generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── src/
│   ├── model.py
│   ├── caption.py
│   └── content_generator.py
│
└── exports/
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/reeshashahid227/AI-Powered-Image-Caption-Generator.git
```

```bash
cd AI-Powered-Image-Caption-Generator
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🚀 Workflow

| Step | Description |
|------|-------------|
| 1 | Upload one or multiple images |
| 2 | BLIP generates the original image caption |
| 3 | Groq enhances the caption |
| 4 | Choose caption style, tone, and language |
| 5 | Generate multiple AI caption suggestions |
| 6 | Export captions as a TXT file |

---

# 🎨 Caption Styles

| Available Styles |
|------------------|
| Simple |
| Social Media |
| Professional |
| Creative |
| Marketing |

---

# 😊 Caption Tones

| Available Tones |
|-----------------|
| Neutral |
| Friendly |
| Professional |
| Funny |
| Emotional |

---

# 🌍 Supported Languages

| Languages |
|-----------|
| English |
| Urdu |
| Roman Urdu |

---

# 🤖 AI Models

| Model | Purpose |
|-------|----------|
| Salesforce/blip-image-captioning-base | Image Caption Generation |
| llama-3.1-8b-instant (Groq) | Caption Enhancement |

---

# 📄 Sample Output

```text
Original Caption

A dog running through a grassy park.

----------------------------------------

AI Caption Suggestions

1. Enjoying every moment of adventure in the sunshine! 🐶🌿

2. Happiness is a run through the park with endless energy.

3. Life is better with wagging tails and green fields.
```

---

# 📌 Future Improvements

- Export captions in PDF and CSV formats
- Additional language support
- More caption styles and tones
- Enhanced UI and user experience

---

.