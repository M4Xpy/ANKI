def get_template(template: str, text: str) -> str:
    """
    >>> get_template(template='check', text='test')
    'This is a test'
    """
    return {
        'ai': f"Provide single-root words and forms for the word '{text}' , along with popular phrases(better proverbs)  that directly include these single-root words and their translations into Russian.",
        'check': f"This is a {text}"

    }[template]
