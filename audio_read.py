############# FOR READING THE TEXT I GAVE IT###
# import pyttsx3
# speaker = pyttsx3.init()
# speaker.say('look abdul i can talk')
# speaker.runAndWait()

############ FOR READING PDF ##############
# import pyttsx3
# import PyPDF2
# book = open('OKAY.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages
# print(pages)
#
# speaker = pyttsx3.init()
# ############ FOR THE PAGE YOU WANT IT TO READ FOR YOU #####
# page = pdfReader.getPage(7)
# text = page.extractText()
# speaker.say(text)
# speaker.runAndWait()

# #### TO READ FROM THE BEGINNING TO THE END##############
import pyttsx3
import PyPDF2
book = open('OKAY.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(1)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()