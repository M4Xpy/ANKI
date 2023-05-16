def get_template(template: str, text: str) -> str:
    """
    >>> get_template(template='check', text='test')
    'This is a test'
    """
    return {
        'ai': f"""
        You answer must be strictly in the format of the following examle.
        Examle for the word 'HUMAN'
        Begining of the my example.

        Human - человек, человеческий
        Humans - люди (plural)
        Humanity - человечество, гуманность
        Humanize - возвышать до человеческого уровня, гуманизировать
        Humanized - гуманизированный (past participle)
        Humanizing - гуманизация, возвышение до человеческого уровня (present participle)
        Humanely - человечно (adverb)
        Humanitarian - гуманитарный (adjective)
        Humanitarian - гуманитар (noun)

        "To err is human, to forgive divine."
        "Человеку свойственно ошибаться, прощать — божественно."
        
        "Charity appeals to the best side of human nature."
        "Благотворительность обращается к лучшей стороне человеческой природы."
        
        "You can't repeal human nature."
        "Вы не можете отменить человеческую природу." (Barbara Kingsolver)

        End of the my example.
        
        Now give me single-root words and forms for the word '{text}' with theirs translate on russian .And proverbs with some of these words with translate on russian.

                """,
        'check': f"This is a {text}"

    }[template]
