#Occurs when copied from the url while playing a video
Standard_link = "https://www.youtube.com/watch?v=QwHN36rSA5g"

#Occurs when share button is clicked
Shortened_link = "https://youtu.be/CJ5LC7f0Zus?si=1KQs-Na4QuOdtiH_"

#Occurs when an embed link is copied #Still does not support embedded links
embedded_link ='<iframe width="560" height="315" src="https://www.youtube.com/embed/QwHN36rSA5g?si=1Ge0kzbJAiwR2ohD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'

#Occurs when a shorts link is copied
shorts_link = "https://youtube.com/shorts/Xhp2vwKWQ_g?si=wdWdts6GUAHjIr42"


from url_validator import YoutubeURLValidator

validator = YoutubeURLValidator()

result = validator.validate(Shortened_link)

print(result)
