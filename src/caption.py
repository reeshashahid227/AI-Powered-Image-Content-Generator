def create_caption(image, processor, model):
    """
    Generate a caption from a PIL Image.
    """

    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    output = model.generate(**inputs)

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption