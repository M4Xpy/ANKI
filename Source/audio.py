import webbrowser


def open_google_image(text: str) -> None:
    """"""
    url = f'https://www.google.com/search?q={text}&tbm=isch&hl=en&tbs=itp:clipart&sa=X&ved=0CAIQpwVqFwoTCKCx4PzezvsCFQAAAAAdAAAAABAD&biw=1349&bih=625'
    webbrowser.open(url, new=0, )


open_google_image('zip')