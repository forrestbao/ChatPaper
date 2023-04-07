
import fitz

def pdf2txt(stream):
    with fitz.open(stream=stream, filetype="pdf") as doc: # open document
        text_list = [page.get_text() for page in doc]
    return "\n\n".join(text_list)

import openai 
import ChatPaper_config # a simple python file containing 
                     # a variable called openai_api_key
openai.api_key = ChatPaper_config.openai_api_key

import funix

from funix.widget.builtin import BytesFile 

@funix.funix()
def ChatPaper(
    PDFBytes: BytesFile,
    prompt_template: str="The following is a paper about {article}", 
    system_message: str="",
    ) -> str: 

    if system_message != "": 
        messages = [ {"role": "system", "content": system_message}]
    else:
        messages = [] # empty context

    article = pdf2txt(PDFBytes)
    query = prompt_template.format(article=article)

    messages.append({"role":"system", "content":query}) # add the query to the context

    completion = openai.ChatCompletion.create(
        model= 'gpt-3.5-turbo',
        messages=messages 
    )

    return completion.choices[0]["message"]["content"]
