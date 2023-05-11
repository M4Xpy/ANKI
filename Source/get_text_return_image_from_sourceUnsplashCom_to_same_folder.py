import requests
from io import BytesIO
from PIL import Image


def get_image(text_or_word: str) -> None:
    """ Takes a string and puts an image describing the text_or_word  """
    if not isinstance(text_or_word, str):
        raise TypeError("The 'text_or_word' argument must be a string.")
    if not text_or_word:
        raise ValueError("The 'text_or_word' argument cannot be an empty string.")

    # Send a request to obtain an image for the given text or word
    url = f"https://source.unsplash.com/800x600/?{text_or_word}"
    response = requests.get(url)
    response.raise_for_status()

    # Load the image from the response content and save it
    img = Image.open(BytesIO(response.content))
    img.save("clipboard.png")

get_image('apple')
