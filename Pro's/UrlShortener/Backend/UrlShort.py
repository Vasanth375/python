try:
    import pyshorteners 
    link="https://google.com" # link you want shortener

    # Creating object of Shortener and the important thing is bitly needs api_key to short URL so we already created
    # bitly account 
    shortener=pyshorteners.Shortener(api_key="22118e73d41c6c170ac2a836e0b48bffd0f372d9") # pass api_key as parameter

    x=shortener.bitly.short(link) #passing link as parameter 
    print("Original Link: ",shortener.bitly.expand(x)) # extracting original link
    print("Shortened Link: ",x)

    # To check url clicks total_clicks()
    print("Total Clicks of Shorten link: ",shortener.bitly.total_clicks(x)) 

except Exception as e:
    print(e)