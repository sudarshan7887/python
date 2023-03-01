def searcher():        #coroutine
    import time
    book = "This is a coroutine tutorial in the python learning"
    time.sleep(3)

    while True:
        text = (yield )
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()          #start coroutine
print("Start Search...")
next(search)
search.send("python")
input("press any key")
search.send("Sudarshan")
search.close()              #close coroutine