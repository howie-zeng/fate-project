# Author: Danny Saelid
import pickle
import os


# splits the DOCUMENT# by the middle '00' to get qid and r
def splitByDoubleZeros(doc_num):
    # finds index of last zero, not including any trailing zeroes
    num_trailing = 0
    temp_ind = len(doc_num) - 1
    while doc_num[temp_ind] == str(0):
        num_trailing += 1
        temp_ind -= 1

    last_zero_ind = doc_num[:len(doc_num) - num_trailing].rindex('0')

    # [qid, r]
    return [doc_num[:last_zero_ind - 1], doc_num[last_zero_ind + 1:]]


# finds the index of a Snippet with the given original rank in a list of Snippets
# might be improved upon with binary search if the snippet_list is sorted by original rank
# returns -1 if the desired Snippet is not found
def getIndexOf(rank, snippet_list):
    ind = 0
    for snip in snippet_list:
        if (int (snip.get_rank()) == rank):
            return ind
        ind += 1

    return -1


"""
returns snippet data in the format:
    {
        qid1: [[query_name, snippet1title, snippet1url, snippet1desc], [query_name, snippet2title...]],
        qid2: [...]
    }
for each qid, snippet1 corresponds to the first snippet in the reranked list
"""


def extractFromFile(file_name, num_snippets):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "../SampleData/", file_name)
    file = open(filename)
    lines = file.readlines()
    file.close()

    myPickle = os.path.join(dirname, "../src/snippet.pickle")
    with open(myPickle,'rb') as fr:
        query_snippet_list = pickle.load(fr)

    results = {}

    # there are 10 results for a given query, but we only want to
    # inspect a certain number

    # the number of snippets added to the current qid in results
    snippets_added = 0
    curr_qid = -1
    for line in lines:
        tokens = line.split(' ')
        q_and_r = splitByDoubleZeros(tokens[2])
        qid = int(q_and_r[0])

        # once a new qid is reached, set currQid equal to it,
        # set snippetsAdded equal to zero, and add an empty list at
        # results[currQid]
        if curr_qid != qid:
            curr_qid = qid
            snippets_added = 0
            results[curr_qid] = []

        if snippets_added < num_snippets:
            og_rank = int(q_and_r[1])
            new_rank = int(tokens[3])  # corresponds to RANK

            query_snippet = query_snippet_list[qid - 1]
            snippet_list = query_snippet.snippetList
            sid = getIndexOf(og_rank, snippet_list)
            curr_snippet = snippet_list[sid]

            if og_rank != int(curr_snippet.get_rank()):
                print("Current Snippet's original rank is unequal to the 'r' field in the .txt file.")

            # [query_name, title, url, description]
            # replaces double quotes with single quotes to avoid messing up JSON
            results[qid].append([query_snippet.query.replace('"', "'"), curr_snippet.get_title().replace('"', "'"),
                                 curr_snippet.get_url().replace('"', "'"), curr_snippet.get_desc().replace('"', "'")])

            snippets_added += 1

    return results
