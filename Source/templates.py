def get_template(template: str, text: str) -> str:
    """
    >>> get_template(template='check', text='test')
    'This is a test'
    """
    return {
        'ai': f"""
                It is important that the template of your answer matches the following example.
        I ask you for a word 'Linger'.
        You answer me strictly in the following format.
        Begining of the my example.

        Linger - медлить, затягиваться
        Lingers - затягивается (third person singular present tense)
        Lingered - затянулся (past tense)
        Lingering - затяжной, медленный (present participle)
        Lingerer - медлитель (noun)
        Lingerie - женское белье (noun)

        "Time flies over us, but leaves its shadow behind."
        "Время летит над нами, но оставляет свой след" (Nathaniel Hawthorne).

        "Don't linger too long in the past, or you'll risk missing the present."
        "Не задерживайся слишком долго в прошлом, иначе рискуешь упустить настоящее."

        "The taste of success lingers long after the work is done."
        "Вкус успеха остается долго после того, как работа закончена."

        "Time and tide wait for no man."
        "Время и прилив не ждут никого" (Geoffrey Chaucer).

        End of the my example.
        Now give me single-root words and forms for the word '{text}' with theirs translate on russian .And proverbs with some of these words with translate on russian.

                """,
        'check': f"This is a {text}"

    }[template]
