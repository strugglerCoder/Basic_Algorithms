import textwrap
def wrap(string, max_width):

    a = textwrap.fill(string,max_width)
    return a

    # i = 0
    # lst = []
    # while(i<len(string)):

    #    lst.append(string[i:i+max_width])

    #    i = max_width + i
    # return "\n".join(lst)


print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))