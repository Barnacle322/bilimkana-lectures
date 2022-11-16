my_str = "Hello"

my_int = [123]

# new_str = "{} {}".format(my_str, my_int)

new_str2 = f"{my_str} {my_int if my_int is not None else ' '}"
print(new_str2)
