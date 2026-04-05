def categorize_complaint(text):
    text = text.lower()

    if "wifi" in text or "internet" in text:
        return "Internet"

    elif "water" in text or "bathroom" in text or "tap" in text:
        return "Water"

    elif "fan" in text or "light" in text or "electric" in text:
        return "Electrical"

    elif "food" in text or "mess" in text or "canteen" in text:
        return "Mess"

    elif "clean" in text or "garbage" in text or "dirty" in text:
        return "Cleaning"

    elif "security" in text or "ragging" in text or "fight" in text:
        return "Security"

    else:
        return "Other"