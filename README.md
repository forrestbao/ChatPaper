# ChatPaper

Upload a PDF file, and ask ChatGPT to perform tasks (e.g., information extraction) about it. 

ChatPaper is 100% Python. You can easily leverage Python's ecosystem and built-in operations to extend it. Currently, ChatPaper is open source under the terms of AGPL. We are considering using a more permissive license for private deployment. If you want private deployment, please contact us. 

And, thanks to [Funix.io](http://funix.io), ChatPaper's code contains only the core logic. Nothing else about the UI. In no other libraries can you build a chatbot in shorter code. 

The screenshot below is the app in action by analyzing a paper from the author. 

![screenshot](screenshot.png)

**Contact**: forrest dot bao [in] Gmail 

## Setup

Before you start, please set the environmental variable `OPENAI_API_KEY` to your OpenAI API key. One way to do that is 
to simply run the command below in your terminal with your actual OPENAI API key:

```python
export OPENAI_API_KEY = "sk-YOUR-OPENAI-KEY" 
```

Or, you can save the command above into a bash script and `source` it:

```bash
source OPENAI_KEY.bash
```

After setting up the OpenAI API key, run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

Finally, run the following command to start the server:

```bash
funix ChatPaper
```

## Usage

Your query will be in the `prompt_template` box. A hardcoded variable `{article}` is the text extracted from the PDF file you upload. Do NOT change the variable name or drop the curly braces. 

You can also add a system message in `system_message` box. But it is optional. 

A PDF file, especially when it is a paper, is very long. So it needs to be truncated into chunks for OpenAI to process (https://github.com/forrestbao/ChatPaper/pull/1). The `chunk_size` box is for that purpose. The default value is 2000 words -- separated by spaces (hence, ChatPaper cannot support languages whose words are not separated by spaces like Chinese). You can change it to a smaller value if you get token too long error from OpenAI. Note that OpenAI's token length measures both the request and the response, and a word in English may be tokenized into 2-3 tokens.  

## Coming next

* Save history (already enabled in Funix)
* Access control 
* Support more venders (e.g., Claude, etc.)
* Support non-PDF files (e.g., Word, etc.)
* Support languages whose words are not separated by spaces (e.g., Chinese, etc.)


## Disclaimer

ChatPaper is an open source tool. We are not responsible for how you make use of it or what you decide to do based on the responses it receives from OpenAI. 