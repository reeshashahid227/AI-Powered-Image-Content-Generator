import streamlit as st
from PIL import Image

from src.model import load_model
from src.caption import create_caption
from src.content_generator import generate_custom_caption


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI-Powered Image Content Generator",
    page_icon="🖼️",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🖼️ AI-Powered Image Content Generator")

st.subheader(
    "Generate captions, descriptions, hashtags, keywords, "
    "and alt text from uploaded images using pretrained AI models."
)

st.markdown("---")


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("AI-Powered Image Content Generator")

st.sidebar.info(
    "Upload an image and generate AI-powered captions, "
    "descriptions, hashtags, keywords, and alt text."
)


# Supported Formats

st.sidebar.markdown("### 📁 Supported Formats")

st.sidebar.write("✔ JPG")
st.sidebar.write("✔ JPEG")
st.sidebar.write("✔ PNG")


st.sidebar.markdown("---")


# Project Features

st.sidebar.markdown("### 📌 Project Features")

st.sidebar.write("🖼️ Image Upload")
st.sidebar.write("📝 AI Caption Generation")
st.sidebar.write("📖 Image Description")
st.sidebar.write("🏷️ Keywords")
st.sidebar.write("#️⃣ Hashtags")
st.sidebar.write("♿ Alt Text")


st.sidebar.markdown("---")


# Technology

st.sidebar.markdown("### 👨‍💻 Technology")

st.sidebar.write("• Python")
st.sidebar.write("• Streamlit")
st.sidebar.write("• Transformers")
st.sidebar.write("• PyTorch")
st.sidebar.write("• Pillow")
st.sidebar.write("• Groq AI")


st.sidebar.markdown("---")


# --------------------------------------------------
# Phase 4 - Caption Settings
# --------------------------------------------------

st.sidebar.markdown("### 🎨 Caption Settings")


caption_style = st.sidebar.selectbox(
    "Caption Style",
    [
        "Simple",
        "Social Media",
        "Professional",
        "Creative",
        "Marketing"
    ]
)


caption_tone = st.sidebar.selectbox(
    "Caption Tone",
    [
        "Neutral",
        "Friendly",
        "Professional",
        "Funny",
        "Emotional"
    ]
)


caption_language = st.sidebar.selectbox(
    "Caption Language",
    [
        "English",
        "Urdu",
        "Roman Urdu"
    ]
)


# --------------------------------------------------
# Image Upload
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload an Image",
    type=["jpg", "jpeg", "png"]
)


# --------------------------------------------------
# Main Content
# --------------------------------------------------

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns([1, 1])


    # ==================================================
    # LEFT COLUMN
    # ==================================================

    with col1:

        st.markdown("## 🖼️ Image Preview")

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )


        # Image Information

        st.markdown("## 📄 Image Information")

        st.write(
            f"**Filename:** {uploaded_file.name}"
        )

        st.write(
            f"**Resolution:** {image.width} × {image.height}"
        )

        st.write(
            f"**Format:** {image.format}"
        )

        st.write(
            f"**Color Mode:** {image.mode}"
        )

        size_kb = uploaded_file.size / 1024

        st.write(
            f"**File Size:** {size_kb:.2f} KB"
        )


    # ==================================================
    # RIGHT COLUMN
    # ==================================================

    with col2:

        st.markdown("## 🤖 AI Generated Content")


        # Generate Button

        if st.button(
            "🚀 Generate AI Content",
            use_container_width=True
        ):

            try:

                # ------------------------------------------
                # STEP 1 - Load BLIP Model
                # ------------------------------------------

                with st.spinner(
                    "🤖 Loading BLIP model..."
                ):

                    processor, model = load_model()


                # ------------------------------------------
                # STEP 2 - Generate Basic Caption
                # ------------------------------------------

                with st.spinner(
                    "🖼️ Understanding image..."
                ):

                    base_caption = create_caption(
                        image,
                        processor,
                        model
                    )


                # ------------------------------------------
                # STEP 3 - Groq AI
                # ------------------------------------------

                with st.spinner(
                    "✨ Creating customized caption..."
                ):

                    final_caption = generate_custom_caption(
                        caption=base_caption,
                        style=caption_style,
                        tone=caption_tone,
                        language=caption_language
                    )


                # ------------------------------------------
                # Results
                # ------------------------------------------

                st.success(
                    "✅ AI content generated successfully!"
                )


                st.markdown("---")


                # BLIP Caption

                st.subheader("🤖 Original BLIP Caption")

                st.info(base_caption)


                # Customized Caption

                st.subheader("✨ Customized Caption")

                st.success(final_caption)


                # Selected Settings

                st.markdown("### ⚙️ Selected Settings")

                st.write(
                    f"**Style:** {caption_style}"
                )

                st.write(
                    f"**Tone:** {caption_tone}"
                )

                st.write(
                    f"**Language:** {caption_language}"
                )


                # Future Features

                st.markdown("---")

                st.subheader("📖 Description")

                st.info(
                    "Description generation will be implemented in the next phase."
                )


                st.subheader("🏷️ Keywords")

                st.info(
                    "Keyword generation will be implemented in the next phase."
                )


                st.subheader("#️⃣ Hashtags")

                st.info(
                    "Hashtag generation will be implemented in the next phase."
                )


                st.subheader("♿ Alt Text")

                st.info(
                    "Alt text generation will be implemented in the next phase."
                )


            except Exception as e:

                st.error(
                    f"❌ Something went wrong: {e}"
                )


# --------------------------------------------------
# No Image Uploaded
# --------------------------------------------------

else:

    st.warning(
        "📤 Please upload an image to begin."
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "AI-Powered Image Content Generator | "
    "Built with Python, Streamlit, BLIP & Groq AI"
)