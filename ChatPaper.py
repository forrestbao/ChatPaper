# Python built-in
import os
from typing import List, Dict

# open AI
import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

# Funix
import funix
from funix.widget.builtin import BytesFile
from funix.hint import Markdown

# from this module
import text_processing

def single_chatGPT_query(
    messages: List[Dict[str, str]],
    model: str,
    max_tokens: int,
)   -> str:
    completion = openai.ChatCompletion.create(
        model= model,
        messages=messages,
        max_tokens=max_tokens,
    )

    return completion.choices[0]["message"]["content"]

@funix.funix(
    description= """ChatPaper is a tool to query a PDF paper with a question. It was made purely in Python in [Funix.io](http://funix.io). If you like it, give both ChatPaper and Funix a star on Github! 

* https://github.com/forrestbao/ChatPaper
* https://github.com/TexteaInc/funix

    """, 
    widgets = {
        'prompt_template': 'textarea', 
        'max_tokens': 'slider[20,500,25]',
    },
    argument_labels = {
        'chunk_size': "Space-splitted words per query? It needs to be much smaller than model token limit.",
        'max_tokens': "Length of return (each document segment)"
    },
    show_source=True 
)
def ChatPaper(
    PDFBytes: BytesFile,
    prompt_template: str = "The following is part of a paper {article}. Please answer the question: ...",
    system_message: str = "",
    chunk_size: int = 2000,
    max_tokens: int = 100,
) -> Markdown:

    # Load the PDF file and convert it to text iterator
    article = text_processing.pdf2txt(PDFBytes)
    article_chunks = text_processing.document_chunks(article, chunk_size=chunk_size)

    # Incrementally query the document and concatenate the responses
    response_messages = []
    for text_chunk in article_chunks:

        # Fresh message list for each query
        if system_message != "" or " ":
            messages = [ {"role": "system", "content": system_message}]
        else:
            messages = [] # no system message

        query = prompt_template.format(article=text_chunk)
        messages.append({"role":"user", "content":query}) # add the query to the context
        single_response = single_chatGPT_query(
            messages=messages,
            model= 'gpt-3.5-turbo',
            max_tokens=max_tokens,
        )

        print (single_response)

        response_messages.append(single_response)

    return "\n [Continued]\n ".join(response_messages)