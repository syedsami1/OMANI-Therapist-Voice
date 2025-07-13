def adapt_response(text):
    replacements = {
        "كيف حالك": "شو أخبارك",
        "أفهم شعورك": "أحس فيك والله",
        "دعونا نناقش": "خلنا نحاول نفهم سوا",
        "الله معك": "تقدر تصلي ركعتين وتهدأ، الله دايم معك"
    }
    for src, tgt in replacements.items():
        text = text.replace(src, tgt)

    if "صلاة" in text or "الله" in text:
        text += " 🌙 لا تنسى إنك قريب من ربك دائمًا."

    return text
