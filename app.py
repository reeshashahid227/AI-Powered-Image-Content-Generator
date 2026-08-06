import streamlit as st
from PIL import Image

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
    "Generate captions, descriptions, hashtags, keywords, and alt text from uploaded images using pretrained AI models."
)

st.markdown("---")

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("AI-Powered Image Content Generator")

st.sidebar.info(
    "Upload an image and generate AI-powered captions, descriptions, hashtags, keywords, and alt text."
)

st.sidebar.markdown("### 📁 Supported Formats")
st.sidebar.write("✔ JPG")
st.sidebar.write("✔ JPEG")
st.sidebar.write("✔ PNG")

st.sidebar.markdown("---")

st.sidebar.markdown("### 📌 Project Features")

st.sidebar.write("🖼️ Image Upload")
st.sidebar.write("📝 AI Caption Generation")
st.sidebar.write("📖 Image Description")
st.sidebar.write("🏷️ Keywords")
st.sidebar.write("#️⃣ Hashtags")
st.sidebar.write("♿ Alt Text")

st.sidebar.markdown("---")

st.sidebar.markdown("### 👨‍💻 Technology")

st.sidebar.write("• Python")
st.sidebar.write("• Streamlit")
st.sidebar.write("• Transformers")
st.sidebar.write("• PyTorch")
st.sidebar.write("• Pillow")

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

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 1])

    # ---------------- Left Column ---------------- #

    with col1:

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        st.markdown("## 📄 Image Information")

        st.write(f"**Filename:** {uploaded_file.name}")
        st.write(f"**Resolution:** {image.width} × {image.height}")
        st.write(f"**Format:** {image.format}")
        st.write(f"**Color Mode:** {image.mode}")

        size_kb = uploaded_file.size / 1024
        st.write(f"**File Size:** {size_kb:.2f} KB")

    # ---------------- Right Column ---------------- #

    with col2:

        st.markdown("## 🤖 AI Generated Content")

        if st.button("🚀 Generate AI Content", use_container_width=True):

            st.success("✅ Image uploaded successfully!")

            st.info(
                "AI caption generation will be implemented in Phase 3."
            )

        st.markdown("---")

        with st.container():

            st.subheader("📝 Caption")
            st.info("Waiting for AI...")

            st.subheader("📖 Description")
            st.info("Waiting for AI...")

            st.subheader("🏷️ Keywords")
            st.info("Waiting for AI...")

            st.subheader("#️⃣ Hashtags")
            st.info("Waiting for AI...")

            st.subheader("♿ Alt Text")
            st.info("Waiting for AI...")

else:

    st.warning("📤 Please upload an image to begin.")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "AI-Powered Image Content Generator | Built with Python, Streamlit & Pretrained Vision Models"
)