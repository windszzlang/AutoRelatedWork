import requests
import urllib
import json
import openai
import feedparser
import xml.etree.ElementTree as ET

from prompt import PROMPT_TEMPLATE



with open('OPENAI_API_KEY.txt') as f:
    OPENAI_API_KEY = f.read().strip()
openai.api_key = OPENAI_API_KEY



#### Arxiv API Access


# keyword = 'large language models'
# max_results = 10


keyword = input('Please input your keyword: ')
max_results = input('How many related work do you want to include in this section: ')
# max_results = 10

keyword = keyword.replace(" ", "%20")
field='cs'
sortBy = 'relevance' # "relevance", "lastUpdatedDate", "submittedDate"
sortOrder = 'descending' # "ascending" or "descending"


# url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=max_results'
url = 'http://export.arxiv.org/api/query?search_query=' + field + ':' + keyword + '&start=0&max_results=' + str(max_results) + '&sortBy=' + sortBy + '&sortOrder=' + sortOrder
# print(url)


response = urllib.request.urlopen(url).read()
print(response.decode('utf-8'))

# debug example
# with open('query.txt') as f:
    # response = f.read()

feed = feedparser.parse(response)


bibtex_template = '''@misc{{{bibtex_id},
    title={{{title}}}, 
    author={{{author}}}, 
    year={{{year}}},
    eprint={{{arxiv_id}}},
    archivePrefix={{arXiv}},
    primaryClass={{{primary_class}}}
}}'''


related_work = []
for entry in feed.entries:
    title = entry.title
    arxiv_id = entry.id.split('/abs/')[-1]
    year = entry.published.split('-')[0]
    authors = ', '.join(author.name for author in entry.authors)
    abstract = entry.summary
    primary_class = entry.tags[0]['term']

    # get the links to the abs page and pdf for this e-print
    # for link in entry.links:
    #     if link.rel == 'alternate':
    #         print('abs page link: %s' % link.href)
    #     elif link.title == 'pdf':
    #         print('pdf link: %s' % link.href)

    bibtex = bibtex_template.format(bibtex_id=authors.split()[0].lower() + year + title.split()[0].lower(),
                                    title=title,
                                    author=authors,
                                    year=year,
                                    arxiv_id=arxiv_id,
                                    primary_class=primary_class)
    paper = {
        'title': title,
        'authors': authors,
        'abstract': abstract,
        'bibtex': bibtex
    }
    print(paper)
    related_work.append(paper)



#### GPT Processing and Generating

input('Confirm to generate? ')

model_input = PROMPT_TEMPLATE.format(keyword=keyword, related_work=json.dumps(related_work))


resp = openai.ChatCompletion.create(
    model='gpt-4', # official model: gpt-3.5-turbo, gpt-4,
    messages=[
        {'role': 'user', 'content': model_input}
    ],
    temperature=0
)
model_output = resp.choices[0].message.content
print(model_output)

related_work = model_output

with open('output.txt', 'w') as f:
    f.write(related_work)
