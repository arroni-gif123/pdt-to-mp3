"  " " This script try to read out pdfs loudly " " "
import PyPDF2 as pdf
from gtts import gTTS

def get_page(num: int, filename: str):
    " " " Get a page of the pdf " " "
    num -= 1
    book = open(filename, 'rb')
    reader = pdf.PdfFileReader(book)
    page = reader.getPage(num)
    text = str(page.extractText())
    text = "".join([s for s in text.strip().splitlines(True) if s.strip()])
    result = replace_chars(text)
    return result

def replace_chars(tpsext: str):
    " " " fix possibly badly encoded characters" " "
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

def main(start: int, stop: int, filename: str):
    " " " Combine the other scripts, read the pages from start to stop, and save them" " "
    for page_no in range(start, stop+1):
        page = get_page(page_no, filename)
        print(page)
        print('#############################', page_no)
        save(page, f'Page_{page_no}')
    
    
if __name__ == '__main__':
    while True:
        try:
            filename = input('What\'s the name of the file?')
            if filename.endswith('.pdf'):
                break
            else:
                print('The file must be a PDF file.')
        except Exception as error:
            print('Invalid value. Try again!')
    while True:
        try:
            start = int(input('At what page should I start?'))
            break
        except Exception as error:
            print('Invalid value. Try again!')

    while True:
        try:
            stop = int(input('At what page should I stop?'))
            break
        except Exception as error:
            print('Invalid value. Try again!')
    main(start, stop )
    
