def is_jumping(number: int) -> str:
    # write your code here
    str_number = str(number)
    order = str_number[0]
    for sign in str_number[1:]:
        if int(sign) != int(order) + 1 and int(sign) != int(order) - 1:
            return "NOT JUMPING"
        order = sign
    return "JUMPING"





