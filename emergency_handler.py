def check_emergency(text):
    crisis_keywords = [
        "أفكر أنتحر",
        "ما أتحمل",
        "أريد أخلص من حياتي",
        "زهقت من الدنيا",
        "ودي أموت"
    ]
    for phrase in crisis_keywords:
        if phrase in text:
            print("🚨 Suicide risk phrase detected.")
            return True
    return False
