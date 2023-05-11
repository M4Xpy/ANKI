def star_separated_words_from(text: str) -> str:
    """ extract first word of each line, removing any digits or underscores from the word, and join them with asterisks
    >>> star_separated_words_from('one , two\\nthree , four\\nfive , six')
    ' * one * three * five * '
    """
    return f" * {' * '.join(line.split()[0].strip('_1234567890') for line in text.splitlines() if line and '.mp3' not in line)} * "


print(("first , second , \\n\\n , third , fourth "))
print(star_separated_words_from("""
BACKING_3667 _поддержка, задний ход, подкладка, опора, подложка  

BACKLOG   задолженность, резервы , невыполненные заказы

BACKUP_4582 _резервный, резервное копирование, резервирование, создавать резервную копию, дублирование, дублирующий

BACKWARDS_3784 _в обратном направлении

COMEBACK_6663 _возвращение

CUTBACK_7926 _сокращение

OUTBACK_12203 _малонаселенная, необжитая местность

SETBACK_8783 _регресс , неудача , задержка


ABACK_10140 _назад, задом, сзади

BACK   назад , обратно , защитник , спина

backfire  обратный эффект , встречный пожар , разрыв патрона

backfired  имел неприятные последствия

[sound:BACKING.mp3][sound:BACKLOG.mp3][sound:BACKUP.mp3][sound:BACKWARDS.mp3][sound:COMEBACK.mp3][sound:CUTBACK.mp3][sound:OUTBACK.mp3][sound:SETBACK.mp3][sound:ABACK.mp3][sound:BACK.mp3]

[sound:backfire.mp3]

"""))
