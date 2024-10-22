import os


async def get_pdf_path(personality_type):
    filename = f"{personality_type.upper()}.pdf"
    filepath = os.path.join('src', 'static', filename)
    if os.path.exists(filepath):
        return filepath
    else:
        return None
