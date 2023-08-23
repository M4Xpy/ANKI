def transform_string(input_string):
    if "|" in input_string:
        parts = input_string.split("|", 1)
        if parts[1].strip()[0].islower():
            return "I " + parts[1].strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ')
        return input_string.strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ').replace("|", "I")
    return input_string.strip('°\n™-=*~@#$%^&*()_+[]{}|/\>< ')

text = "| uxfn|", "| Ifkiusdfhuijf|    "
text = " ".join(transform_string(line) for line in text)
print(text)