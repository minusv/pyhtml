'''Python to HTML Framework'''

def hr(): # horizontal rule
    return("<hr>")

def br(): # break tag
    return("<br>")

def title(content): #title tag
    title = "<title> " + content + " </title>\n"
    return(title)

def body(content): #body tag
    body = "<body> " + content + "</body>\n"
    return(body)

def para(content): #p tag
    para = "<p> " + content + "</p>\n"
    return(para)

def h1(content): #heading1 tag
    heading = "<h1> " + content + " </h1>\n"
    return(heading)
    
def h2(content): #heading2 tag
    heading = "<h2> " + content + " </h2>\n"
    return(heading)
        
def h3(content): #heading3 tag
    heading = "<h3> " + content + " </h3>\n"
    return(heading)
    
def h4(content): #heading4 tag
    heading = "<h4> " + content + " </h4>\n"
    return(heading)

def h5(content): #heading5 tag
    heading = "<h5> " + content + " </h5>\n"
    return(heading)

def a(link, text): #adding link tag
    a = "<a href = \"" + link + "\" >" + text + " </a>"
    return(a)

def generate_html(filename, contents): #function to fill content in body tag and add title to page.
    title = ""
    body_content = ""
    
    for content in contents:
        if "<title>" in content:
            title = content
        else:
            body_content = body_content + "\n" + content
    
    body = "<body> " + body_content + "\n</body>\n"
    html = title + "\n" + body
    createhtml(filename, html)

def createhtml(filename,content): #create htmlfile and write html in it
    filename = filename + ".html"
    file_object = open(filename,"w")
    html = "<html>\n" + content + "</html>"
    file_object.write(html)
    file_object.close()