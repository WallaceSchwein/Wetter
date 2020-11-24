import wetter

crawl = wetter.DataGetter()

for elem in crawl.get():
    print("Am " + str(elem.tag) + " wird es zwischen " + str(elem.max) + " tags und " + str(elem.min) + " nachts. Himmel: " + elem.regen + "!")

input("\nEXIT")