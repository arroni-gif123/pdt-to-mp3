"  " " This script try to read out pdfs loudly " " "
import PyPDF2 as pdf
from gtts import gTTS

def get_page(num: int):
    " " " Get a page of the pdf named book.pdf " " "
    num -= 1
    book = open('book.pdf', 'rb')
    reader = pdf.PdfFileReader(book)
    page = reader.getPage(num)
    text = str(page.extractText())
    text = "".join([s for s in text.strip().splitlines(True) if s.strip()])
    result = replace_chars(text)
    return result

def replace_chars(text: str):
    " " " docstring " " "
    lista = list(text)
    for i in dict(enumerate(lista)):
        if lista[i] =='™':
            lista[i] ="'"
        elif lista[i] == '˜':
            lista[i] = 'fi'
        elif lista[i] == 'Š':
            lista[i] = '; '
    result = ''.join(lista)
    return result

def save(text: str, mp3name: str):
    " " " Initialize the audio engine, and save the text of the pdf as an mp3 file" " "
    engine = gTTS(text=text, lang='en', slow=False)
    engine.save(f'{mp3name}.mp3')

def main(start: int, stop: int):
    " " " Combine the other scripts, read the pages from start to stop, and save em" " "
    for page_no in range(start, stop+1):
        page = get_page(page_no)
        print(page)
        print('#############################', page_no)
        save(page, f'Page_{page_no}')
    
    
if __name__ == '__main__':
    main(1, 1)
    
