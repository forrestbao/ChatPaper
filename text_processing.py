import fitz

from funix.widget.builtin import BytesFile

def pdf2txt(stream: BytesFile):
    with fitz.open(stream = stream, filetype = "pdf") as doc: # open document
        text_list = [page.get_text() for page in doc]
    return "\n\n".join(text_list)

        # self.text = document_bytes.read().decode("utf-8")

class document_chunks(object):
    def __init__(self, text: str, chunk_size):
        self.chunk_size = chunk_size
        self.current_token = 0
        self.text_tokenized = text.split()

    def __iter__(self):
        return self 

    def __next__(self):
        if self.current_token >= len(self.text_tokenized):
            raise StopIteration
        else:
            chunk = self.text_tokenized[self.current_token : self.current_token + self.chunk_size]
            self.current_token += self.chunk_size
            return " ".join(chunk)

if __name__ == "__main__":
    import io
    f = io.BytesIO(b"some initial binary data like this: \x00\x01")
    doc = document_chunks(f.read().decode('utf-8'), chunk_size=2)
    for chunk in doc:
        print(chunk) 