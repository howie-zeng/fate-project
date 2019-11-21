## 1. Folders and files shared
### repeat_rerank folder 
https://www.dropbox.com/sh/puv1ec036hpx9qe/AABDU_3ZHAP7SIpmJTkSVgsJa?dl=0
### snippet.pickle file 
https://www.dropbox.com/s/t8m53fq5wrvuw44/snippet.pickle?dl=0
### snippet.py file
https://www.dropbox.com/s/9o01eawjoqyqwvu/snippet.py?dl=0

## 2. repeat_rerank folder contains rerank lists. 
* There are 1000 subfolders denoting 1000 runs of the rerank algorithms. 
* Each subfolder contains 21 text files. 
* 0gf.txt and 0gfp.txt are not used. 
* All 0g.txt, t.txt, tp.txt are the same regardless of runs. 
* Each text file is the produced rerank list of an algorithm at this run.

### text file names 
The text files can be divided into 3 groups:
* Non-fair algorithms: all files with a number but without 'f' in the name
* Fair (group1) algorithms: includes files with 'p' in the file names
* Fair (group2) algorithms: all other files  p, r, t, 01gf, 001gf, 05gf, 1gf

## 3. Text file format 
TOPIC    Q0    DOCUMENT#    RANK    SCORE    ALGORITHM_NAME
* This is in the standard format as required by TREC web track.
* See "Submission Format for Adhoc and Risk-sensitive Tasks" at the followin link
http://www-personal.umich.edu/~kevynct/trec-web-2014/

### You need two fields: 
* DOCUMENT# = qid00r
* RANK = rank position in the rerank list
* qid is the query_id, used with the snippet.pickle file. 
* r is the original rank of the document in google search results. This corresponds to the "__rank" field in a Snippet object.  
* You need to extract qid and r to get the actual queries and documents. 
* You need RANK to position each document in the rerank list. The lower the RANK value, the higher the document should be positioned. 

===== END repeat_rerank=====

snippet.pickle file contains a "list" of QuerySnippet object in python
The index of each QuerySnippet object corresponds to qid-1. 
  e.g., the 5th query (qid=5) corresponds to the 5th item in the list. <br />

Each QuerySnippet contains a "list" of Snippet object
* Snippet represents a search result snippet in google web search,
* which includes a title, link, and excerpt of the webpage.
* Each snippet is considered as a unique document.

Each Snippet object has 4 fields describing the original search result document:
* __rank: integer, original rank position in google search. e.g.,__rank=1 means originally ranked 1st.
* __title: title extracted from the original snippet
* __link: link extracted from the original snippet
* __desc: excerpt from the original snippet

The __rank is a unique id of a document under it's query. corresponds to the "r" in each rerank list result file. 


## 4. snippet.py 
* snippet.py file contains the QuerySnippet and Snippet class. 
* You can use this file to understand the structure of the object in snippet.pickle 

## 5. Use tips
-- To find a document (snippet) from the rerank list file,
& extract the DOCUMENT#  and RANK columns.
* extract qid and r from DOCUMENT#, they are separated by 00
* load snippet.pickle file into a list:
with open('snippet.pickle', 'rb') as fr:
	query_snippet_list = pickle.load(fr)

-- locate a query and its snippets, qid converted to integer:
* updated code
* gets the QuerySnippet object by qid
qs = query_snippet_list[qid-1]	
* gets the list of snippets for a query
* see snippet.py ClassSnippet's init method
snippet_list = qs.snippetList

-- locate a snippet result, r converted to integer:
* each snippet is hashed using its original rank "__rank"
* sid = snippet_list.index(r)
* snippet = snippet_list[sid]

Then you can present the query and the document according to title, link, excerpt, and position in the reranked list according to RANK



