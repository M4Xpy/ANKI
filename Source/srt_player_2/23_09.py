import re


def split_text_with_punctuation(text, punctuation='.,;!?'):
    parts = re.split(f"([{punctuation}])", text)
    parts.append('')
    result = []
    for index in range(0, len(parts), 2):
        if text.lower().count(parts[index].strip(" -").lower()) < 2:
            result.append(parts[index] + parts[index + 1])







    return result

text = "Hello, world... How are you today? I'm doing well, thank you.."
parts = split_text_with_punctuation(text)
print(parts)
















