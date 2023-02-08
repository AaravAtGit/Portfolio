import gtts
import PyPDF2



book = input("Enter Filepath: ")
print(book)
try:
    pdf_file = open(book, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_text = ''
    for page in range(len(pdf_reader.pages)):
        pdf_text += pdf_reader.pages[page].extract_text()

    audio_book = gtts.gTTS(pdf_text,lang="hi")
    book = book.replace(".pdf", "")
    book = book.replace("/","")
    audio_book.save(f"C:/Users/My Pic/Downloads/{book}.mp3")
    print("Audio Book has been saved in your Downloads folder")
except FileNotFoundError:
    print("No such file or directory")
    

