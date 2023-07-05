

def funk0():
    text = funk1()
    if text:
        replaced = funk2()
        text.replace(replaced)

# refine funk0() to async , line 'if text:' and 'funk2()' must operating simultainously , if 'if text:' == False second thread aborted
