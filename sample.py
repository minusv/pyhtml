'''Creating new HTML page named index.html using pyhtml module'''

import pyhtml

hr = pyhtml.hr() #hr tag
br = pyhtml.br() #br tag

title = pyhtml.title("GSoc") #title tag

h1_1 = pyhtml.h1("Manasvi Saxena") #h1 tag

a1 = pyhtml.a("msmanasup@gmail.com", "msmanasup@gmail.com") #link tag
a2 = pyhtml.a("https://github.com/minusv23", "Github") #link tag

h2_1 = pyhtml.h2("Education") #h2 tag

h4_1 = pyhtml.h4("B. TECH | 2015-2019 | JAYPEE UNIVERSITY OF ENGINEERING AND TECHNOLOGY, GUNA") #h4 tag
p_1 = pyhtml.para("Electronics and Communication, CGPA: 8.7") #p tag

h2_2 = pyhtml.h2("Skills") #h2 tag

h3_1 = pyhtml.h3("Programming Language") #h3 tag
p_2 = pyhtml.para("Python, C and C++") #p tag

h3_2 = pyhtml.h3("Web Development") #h3 tag
p_3 = pyhtml.para("HTML, CSS, Bootstrap, Django") #p tag

h3_3 = pyhtml.h3("Operting Systems") #h3 tag
p_4 = pyhtml.para("Microsoft Windows and Linux") #p tag

h3_4 = pyhtml.h3("Others") #h3 tag
p_5 = pyhtml.para("Git, AWS, Google API, MATLAB, Arduino") #p tag

h2_3 = pyhtml.h2("Internship and Work Experience") #h2 tag

h3_5 = pyhtml.h3("Comezo") #h3 tag
h5_1 = pyhtml.h4("Back-end Web Developer, Jan 2018 - March 2018") #h4 tag
p_6 = pyhtml.para("""Designed and configured database and back end applications using Django. 
Handled development and management of front end user interfaces with help of HTML, CSS.""") #p tag

h3_6 = pyhtml.h3("IETE Students Forum (ISF)") #h3 tag
h5_2 = pyhtml.h4("Volunteer E.C.E Technical Club, July 2015 - April 2015") #h4 tag 
p_7 = pyhtml.para("Organized and instructed several technical workshops/events throughout the year.") #p tag

h2_4 = pyhtml.h2("Projects") #h2 tag

h3_7 = pyhtml.h3("Online Judge") #h3 tag
h5_3 = pyhtml.h4("Jan 2018 - Present") #h4 tag
p_8 = pyhtml.para("""Online system to test programs in programming contests.
The system can compile and execute code, and test them with pre-constructed data. 
Submitted code will be run with restrictions, including time limit, memory limit. 
The output of the code will be captured by the system, and compared with the standard output. 
The system will then return the result. """) #p tag

h3_8 = pyhtml.h3("Blog") #h3 tag
h5_4 = pyhtml.h4("August 2017 - August 2017") #h4 tag
p_9 = pyhtml.para("""Used CSS3 with W3 web framework to implement object-oriented stylesheets for headers.   
Implemented back end with Django to facilitate posting new posts and uploading media""") #p tag
a3 = pyhtml.a("https://goo.gl/KV46Eg", "View") #a tag

h3_9 = pyhtml.h3("Offline Dictonary") #h3 tag
h5_5 = pyhtml.h4("July 2017 - July 2017") #h4 tag
p_10 = pyhtml.para("""The dictionary not only gives multiple meanings of a word but also suggests 
related words to an incorrect word entered. 
JSON database has been used which contains over fifty thousand words and meanings. """) #p tag
a4 = pyhtml.a("https://github.com/minusv23/Offline-Dictionary", "View") #a tag

h2_5 = pyhtml.h2("Languages") #h2 tag

p_11 = pyhtml.para("English, Professional proficiency") #p tag
p_12 = pyhtml.para("Hindi, Native or Bilingual proficiency") #p tag

# Once all the content of a page is created using the functions,
# the content is passed in a list in the exact order to
# be displayed.

idea_body = [ #content list
    title,
    h1_1,
    hr,
    a1,
    br,
    a2,
    hr,
    h2_1,
    h4_1,
    p_1,
    hr,
    h2_2,
    h3_1,
    p_2,
    h3_2,
    p_3,
    h3_3,
    p_4,
    h3_4,
    p_5,
    hr,
    h2_3,
    h3_5,
    h5_1,
    p_6,
    h3_6,
    h5_2,
    p_7,
    hr,
    h2_4,
    h3_7,
    h5_3,
    p_8,
    h3_8,
    h5_4,
    p_9,
    a3,
    h3_9,
    h5_5,
    p_10,
    a4,
    hr,
    h2_5,
    p_11,
    p_12,
    hr,
]

 #the list is now passed to generate_html() function.
pyhtml.generate_html("index", idea_body)