import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration


@st.cache_resource
def load_model():

    print("Loading BLIP processor...")

    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    print("Processor loaded!")
    print("Loading BLIP model...")

    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    print("BLIP model loaded!")

    return processor, model