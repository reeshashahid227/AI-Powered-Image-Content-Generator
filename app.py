import streamlit as st
from PIL import Image

from src.model import load_model
from src.caption import create_caption
from src.content_generator import generate_custom_captions


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI-Powered Image Caption Generator",
    page_icon="🖼️",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🖼️ AI-Powered Image Caption Generator")

st.subheader(
    "Generate captions from uploaded images using pretrained AI models."
)

st.markdown("---")


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("AI-Powered Image Caption Generator")

st.sidebar.info(
    "Upload one or multiple images and generate AI-powered captions."
)


# ------------------------------------------------------------
# Supported Formats
# ------------------------------------------------------------

st.sidebar.markdown("### 📁 Supported Formats")

st.sidebar.write("✔ JPG")
st.sidebar.write("✔ JPEG")
st.sidebar.write("✔ PNG")

st.sidebar.markdown("---")


# ------------------------------------------------------------
# Project Features
# ------------------------------------------------------------

st.sidebar.markdown("### 📌 Project Features")

st.sidebar.write("🖼️ Multiple Image Upload")
st.sidebar.write("📝 AI Caption Generation")
st.sidebar.write("📖 Image Description")
st.sidebar.write("🏷️ Keywords")
st.sidebar.write("#️⃣ Hashtags")
st.sidebar.write("♿ Alt Text")

st.sidebar.markdown("---")


# ------------------------------------------------------------
# Technology
# ------------------------------------------------------------

st.sidebar.markdown("### 👨‍💻 Technology")

st.sidebar.write("• Python")
st.sidebar.write("• Streamlit")
st.sidebar.write("• Transformers")
st.sidebar.write("• PyTorch")
st.sidebar.write("• Pillow")
st.sidebar.write("• Groq AI")

st.sidebar.markdown("---")


# ============================================================
# CAPTION SETTINGS
# ============================================================

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


num_captions = st.sidebar.slider(
    "Number of Caption Suggestions",
    min_value=1,
    max_value=5,
    value=3
)


# ============================================================
# MULTIPLE IMAGE UPLOAD
# ============================================================

uploaded_images = st.file_uploader(
    "📤 Upload Images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)


# ============================================================
# IF IMAGES ARE UPLOADED
# ============================================================

if uploaded_images:

    st.success(
        f"✅ {len(uploaded_images)} image(s) uploaded successfully!"
    )

    # --------------------------------------------------------
    # Preview Uploaded Images
    # --------------------------------------------------------

    st.markdown("## 🖼️ Uploaded Images")

    preview_columns = st.columns(3)

    for i, uploaded_file in enumerate(uploaded_images):

        image = Image.open(uploaded_file).convert("RGB")

        with preview_columns[i % 3]:

            st.image(
                image,
                caption=uploaded_file.name,
                width="stretch"
            )


    st.markdown("---")


    # ========================================================
    # GENERATE BUTTON
    # ========================================================

    if st.button(
        "🚀 Generate AI Captions",
        width="stretch"
    ):

        try:

            # ------------------------------------------------
            # STEP 1 - LOAD BLIP MODEL
            # ------------------------------------------------

            with st.spinner(
                "🤖 Loading BLIP model..."
            ):

                processor, model = load_model()


            st.success("✅ BLIP model loaded successfully!")


            # ------------------------------------------------
            # PROGRESS INDICATOR
            # ------------------------------------------------

            st.markdown("## ⚙️ Processing Images")

            progress_bar = st.progress(0)

            status_text = st.empty()

            total_images = len(uploaded_images)


            # =================================================
            # PROCESS EACH IMAGE
            # =================================================

            for i, uploaded_file in enumerate(uploaded_images):

                # ---------------------------------------------
                # Open Image
                # ---------------------------------------------

                image = Image.open(
                    uploaded_file
                ).convert("RGB")


                # ---------------------------------------------
                # Progress Status
                # ---------------------------------------------

                status_text.write(
                    f"🔄 Processing image {i + 1} of {total_images}: "
                    f"{uploaded_file.name}"
                )


                # ---------------------------------------------
                # Create Result Section
                # ---------------------------------------------

                st.markdown("---")

                st.markdown(
                    f"## 🖼️ Image {i + 1}: {uploaded_file.name}"
                )


                col1, col2 = st.columns([1, 1])


                # =================================================
                # LEFT COLUMN
                # =================================================

                with col1:

                    st.markdown("### 🖼️ Image Preview")

                    st.image(
                        image,
                        caption=uploaded_file.name,
                        width="stretch"
                    )


                    # ---------------------------------------------
                    # Image Information
                    # ---------------------------------------------

                    st.markdown("### 📄 Image Information")

                    st.write(
                        f"**Filename:** {uploaded_file.name}"
                    )

                    st.write(
                        f"**Resolution:** "
                        f"{image.width} × {image.height}"
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


                # =================================================
                # RIGHT COLUMN
                # =================================================

                with col2:

                    st.markdown(
                        "### 🤖 AI Generated Captions"
                    )


                    # ---------------------------------------------
                    # STEP 2 - BLIP CAPTION
                    # ---------------------------------------------

                    with st.spinner(
                        "🖼️ Understanding image..."
                    ):

                        base_caption = create_caption(
                            image,
                            processor,
                            model
                        )


                    # ---------------------------------------------
                    # Original BLIP Caption
                    # ---------------------------------------------

                    st.subheader(
                        "🤖 Original BLIP Caption"
                    )

                    st.info(base_caption)


                    # ---------------------------------------------
                    # STEP 3 - GROQ CUSTOM CAPTIONS
                    # ---------------------------------------------

                    with st.spinner(
                        "✨ Creating customized captions..."
                    ):

                        captions = generate_custom_captions(
                            caption=base_caption,
                            style=caption_style,
                            tone=caption_tone,
                            language=caption_language,
                            num_captions=num_captions
                        )


                    # ---------------------------------------------
                    # Customized Captions
                    # ---------------------------------------------

                    st.subheader(
                        "✨ AI Caption Suggestions"
                    )

                    caption_lines = captions.split("\n")

                    for line in caption_lines:

                        if line.strip():
                            st.success(line)


                    # ==================================================
                    # EXPORT AI CAPTION
                    # ==================================================

                    export_text = f"""AI Caption Generator

Image:
{uploaded_file.name}

Original BLIP Caption:
{base_caption}

AI Caption Suggestions:
{captions}
"""

                    file_name = (
                        f"AI_Caption_"
                        f"{uploaded_file.name.rsplit('.', 1)[0]}.txt"
                    )

                    st.download_button(
                        label="📥 Export AI Caption",
                        data=export_text,
                        file_name=file_name,
                        mime="text/plain"
                    )


                    # ---------------------------------------------
                    # Selected Settings
                    # ---------------------------------------------

                    st.markdown(
                        "### ⚙️ Selected Settings"
                    )

                    st.write(
                        f"**Style:** {caption_style}"
                    )

                    st.write(
                        f"**Tone:** {caption_tone}"
                    )

                    st.write(
                        f"**Language:** {caption_language}"
                    )



                # ---------------------------------------------
                # UPDATE PROGRESS
                # ---------------------------------------------

                progress_value = (i + 1) / total_images

                progress_bar.progress(
                    progress_value
                )


            # =================================================
            # COMPLETED
            # =================================================

            status_text.success(
                f"✅ Completed! {total_images} image(s) processed."
            )

            st.success(
                "🎉 All AI captions generated successfully!"
            )


        except Exception as e:

            st.error(
                f"❌ Something went wrong: {e}"
            )


# ============================================================
# NO IMAGE UPLOADED
# ============================================================

else:

    st.info(
        "📤 Please upload one or more images to begin."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "AI-Powered Image Content Generator | "
    "Built with Python, Streamlit, BLIP & Groq AI"
    )
