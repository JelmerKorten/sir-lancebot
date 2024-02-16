import re


def suppress_links(message: str) -> str:
    """Accepts a message that may contain links, suppresses them, and returns them."""
    for link in set(re.findall(r"https?://[^\s]+", message, re.IGNORECASE)):
        message = message.replace(link, f"<{link}>")
    return message

def neutralise_string(txt: str | None) -> str | None:
    """Attempts to neutralise all punctuation and cases and returns a string of lowercase words."""
    # return early if no text provided.
    if not txt:
        return None

    # take out punctuation
    txt = re.sub(r"([^\w\s]|_)", " ", txt)

    # full caps words but leaves camelCase / PascalCase
    words = [word.lower() if word.isupper() else word for word in txt.split()]
    txt = " ".join(words)

    # attempt to split PascalCase and camelCase
    words = []
    old_i = 0
    for i, char in enumerate(txt):
        # to avoid PascalCase getting leading empty append
        if char.isupper() and i != 0:
            words.append(txt[old_i:i])
            old_i = i
    words.append(txt[old_i:])

    # strip white spaces and make lowercase
    words = [word.strip().lower() for word in words]
    return " ".join(words)
