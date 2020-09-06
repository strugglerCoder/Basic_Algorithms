# "Hello My World" => 3
# Hrishi "Lokhande Ashok" Ajinkya


def words(string):
    strip = string.strip()
    count = 1
    if len(strip) == 0:
        return 0

    for s in strip:
        if s == " ":
            count += 1
    #if string[len(string) - 1] == " ":
            #count -= 1
    return count


print(words("Hello world as sa           "))
print(words("        "))
print(words("         Hello     world as    sa           "))



