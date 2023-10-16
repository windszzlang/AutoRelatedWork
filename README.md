# AutoRelatedWork

* A GPT-based Tool for Automatic Related Work Generation

## Introduction

* Feel difficult to write the related work? This project is help you automatically generate related work / literature review.
* Compared to traditional LLMs (ChatGPT), ours can generate text with reference and avoid fabrication.
* Currently, the source related work all origin from [Arxiv](https://arxiv.org/).
* Feel free to modify prompt and improve it!

## Quick Start

1. Put your OPENAI_API_KEY in the file `OPENAI_API_KEY.txt`.
2. Configure the environment `pip install requirements.txt`.
3. Run and generate by `python run.py`!
4. Get output: text in `text.txt` and bibtex file in `bibtex.txt`.

## Example

Keyword: large language models
Output file:
```txt

```

## Acknowledgements

* Based on [Arxiv API](https://info.arxiv.org/help/api/index.html) and [Arxiv API Example](https://info.arxiv.org/help/api/examples/python_arXiv_parsing_example.txt)