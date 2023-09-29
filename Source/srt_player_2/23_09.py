def no_repit(text, test=False):
    """
    >>> no_repit(" - No, no - no, no, no, no. Yes, no . - No way, no way, no way! Now, now? now? What. what.. what... - how , - how ?")
    '  - No. Yes, No way! Now? What.... how ?'
    >>> no_repit(" - No, no - no, no, no, no. Yes, no . - No way, no way, no way! Now, now? now? What. what.. what... - how , - how ?")
    '  - No. Yes, No way! Now? What.... how ?'
    """
    in_put = text
    text = f"{text}*"
    compares = [" "]
    part = ""
    for letter in text:
        part = part + letter
        if letter not in "abcdefghijklmnopqrstuvwxyz' \"ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            now_compare = 1
            for index, compare in enumerate(compares):
                now_compare = part.strip(' -?!,.:*').lower()
                if compare.strip(' -?!,.:*').lower() == now_compare and now_compare:
                    compares[index] = compares[index][:-1] + letter
                    now_compare = 0
                    break
            if now_compare or part == compares[-1][-1] or compares == [" "]:
                compares.append(part)
            part = ""
    out_put = "".join(compares).replace("*", " ")

    if len(in_put.strip()) - 3 < len(out_put.strip()):
        return in_put.replace("*", " ")
    if test:
        print(f"{in_put}\n{out_put}\n", len(in_put.strip()), len(out_put.strip()))
    return out_put