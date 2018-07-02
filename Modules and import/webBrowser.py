import webbrowser

#webbrowser.open_new("https://google.com")
#help(webbrowser)

fire = webbrowser.get(using='firefox')
fire.open('https://google.com',new=2)