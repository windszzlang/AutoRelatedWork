PROMPT_TEMPLATE = '''You are an AI to help me write the related work section in an academic paper in Latex.

I will first give you a keyward which is the title of one section of related work and also provide true related work. Then you need to generate paragraphs of related work section.

#### Keyword: {keyword}

#### Related Work: {related_work}


Your text should be in Latex format and include references with `\cite{{}}`
Maybe you do not need to use all related work I provide with you. You just need to use some important and related ones.


You should generate two part text (the generated text of the related work section in Latex format) and bibtex (the bibtex form of references).
Your output should follow the following format:
#### Output Begin ####
Text:
...(content of text part)...

Bibtex:
...(content of bibtex part)...
#### Output End ####

Notice: you cannot fabricate any papers or works, and you cannot use papers or works that do not appear in Related Work provided by the user.
Notice: you should notice escape characters in the json string. For example, a double quote (") should be escaped as \", and a backslash () should be escaped as \\.

Now, generate your response of related work.
'''