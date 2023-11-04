

lines = "\r \n 1 : 3 3 : 0 3 /   2 : 0 6 : 3 9 \r \n T h a t ' s   w h y   w e   c h e a t \r \n a n d   s c r e w   u p   a n d   l i e ,"
lines = " ".join(line for line in lines.splitlines()[-3:] if line and "4444" not in line)
print(lines)
