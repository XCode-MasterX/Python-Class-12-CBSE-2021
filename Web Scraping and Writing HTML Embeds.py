import requests # This is the most essential thing. Without this the program won't work.

# In case you don't have the requests module: https://www.youtube.com/watch?v=HdJywzSCGbc.
# Use the given link.

index = 1
links_found = [] # List to store the links that were found in the page.
query = input("Enter your query: ").replace(" ", "+") # Getting the required search query and reaplcing the spaces for '+' symbol.

'''
    If you look at a youtube link after you have searched something up the format would be like this:
    https://youtube.com/results?search_query=(the query here)

    If you look up: "Tree data structure in Python"
    then the resultant link would be: https://youtube.com/results?search_query=Tree+data+structure+in+Python

    You can check it for yourself.
'''

query_link = f"https://www.youtube.com/results?search_query={query}"
HTML_File = input("Enter the path of the HTML File: ")
youtube = requests.get(query_link)

# Checking if the user gave the right format of file name, if not, we are going to add ".html" to make a valid html-file.
if not(HTML_File.endswith(".html") or HTML_File.endswith(".htm")):
    HTML_File += ".html"

while index != 0:
    '''
    If you look at the link of a youtube video you will find a similar format: https://youtube.com/watch?v={video_id}
    The length of a video-id is always 11 character long, and another thing to note is, every youtube link follows this format.
    So, if we look for "/watch?v=" and then take the next 11 characters we will have the video-id.
    '''
    index = youtube.text.find("/watch?v=", index) # The index of the "/watch?v="
    video_id = youtube.text[index + 9 : index + 20] # Getting the video_id
    links_found.append(video_id) # Appending the video_id
    index += 9 #'9' is the length of the string: "/watch?v="

links_found = list(set(links_found)) # Removing all the duplicate links. (In case)

with open(HTML_File, "w+") as html:
    html.write("<html>\n")
    html.write("<body>\n")
    for link in links_found:
        html.write(f"<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/{link}\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"allowfullscreen></iframe>\n")
    html.write("</body>\n")
    html.write("</html>")

# PROGRAM BY 'JAMES COLLINS'
