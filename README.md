# 🖼️ AI-Powered Image Caption Generator

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![BLIP](https://img.shields.io/badge/BLIP-Image%20Captioning-orange)
![Groq](https://img.shields.io/badge/Groq-LLM-black)

</p>

### 🚀 Live Demo

[Open the Live Demo](https://ai-powered-image-caption-generator-4dkems5s7atpryuabmqe85.streamlit.app/)

---

An AI-powered application that generates captions from uploaded images using the **BLIP Image Captioning** model and enhances them with **Groq LLM**. Users can customize captions based on style, tone, and language while generating multiple caption suggestions through an interactive Streamlit interface.

---

# ✨ Features

| Feature | Description |
|---------|-------------|
| 🖼️ Image Upload | Upload single or multiple JPG, JPEG, and PNG images |
| 🤖 Image Caption Generation | Generate captions using the BLIP pretrained model |
| ✨ AI Caption Enhancement | Improve captions using Groq LLM |
| 🎨 Caption Styles | Simple, Social Media, Professional, Creative, Marketing |
| 😊 Caption Tones | Neutral, Friendly, Professional, Funny, Emotional |
| 🌍 Language Support | English, Urdu, Roman Urdu |
| 📝 Multiple Captions | Generate multiple AI caption suggestions |
| 💻 Interactive UI | User-friendly Streamlit interface |

---

# 🏗️ Project Workflow

```text
          Upload Image(s)
                 │
                 ▼
      BLIP Image Caption Model
                 │
                 ▼
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
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Framework | Streamlit |
| Vision Model | BLIP (Salesforce/blip-image-captioning-base) |
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
   ├── model.py
   ├── caption.py
   └── content_generator.py
```

---

# ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/reeshashahid227/AI-Powered-Image-Caption-Generator.git
```

```bash
cd AI-Powered-Image-Caption-Generator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate (Windows)

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

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
| 4 | Select caption style, tone, and language |
| 5 | Generate multiple AI caption suggestions |

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

- Support for additional languages
- More caption styles and tones
- Better prompt customization
- Improved user interface

---

