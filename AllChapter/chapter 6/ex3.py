while True:
    name = input("Enter text(enter-exit) : ")
    if name == "exit": break
    print(f"Enter text(enter-exit) : {name}")
    print(f"Text has 'a' : {name.count("a")}")
    print(f"Text has 'e' : {name.count("e")}")
    print(f"Text has 'i' : {name.count("i")}")
    print(f"Text has 'o' : {name.count("o")}")
    print(f"Text has 'u' : {name.count("u")}\n")