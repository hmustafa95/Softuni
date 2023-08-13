def reverse_text(text):
    start = -1
    end = -len(text)

    while start >= end:
        yield text[start]
        start -= 1
