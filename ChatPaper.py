import fitz

def pdf2txt(stream):
    with fitz.open(stream=stream, filetype="pdf") as doc:  # open document
        text_list = [page.get_text() for page in doc]
    return "\n\n".join(text_list)

def split_text(text, max_length=4000):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(" ".join(current_chunk)) + len(word) <= max_length:
            current_chunk.append(word)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
    chunks.append(" ".join(current_chunk))

    return chunks

import openai
import ChatPaper_config  # a simple python file containing
# a variable called openai_api_key
openai.api_key = ChatPaper_config.openai_api_key

import funix

from funix.widget.builtin import BytesFile

@funix.funix()
def ChatPaper(
    PDFBytes: BytesFile,
    prompt_template: str = "The following is part of a paper about {article}",
    system_message: str = "",
) -> str:


    article = pdf2txt(PDFBytes)
    text_chunks = split_text(article)
    response_messages = []
    for chunk in text_chunks:
        if system_message != "":
            messages = [{"role": "system", "content": system_message}]
        else:
            messages = []  # empty context
        query = prompt_template.format(article=chunk)
        messages.append({"role": "system", "content": query})  # add the query to the context
        print ('messages', messages)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        response_messages.append(completion.choices[0]["message"]["content"])

    return " ".join(response_messages)
