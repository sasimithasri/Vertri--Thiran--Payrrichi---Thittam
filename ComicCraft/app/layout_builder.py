def build_comic_layout(images, stories):
    layout = []

    for index, image_path in enumerate(images):
        story = stories[index] if index < len(stories) else ""

        layout.append({
            "panel": index + 1,
            "image": image_path,
            "text": story
        })

    return layoutss