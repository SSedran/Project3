'''Semantic Similarity: starter code
Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    numerator = 0
    for i in range(0,len(vec1)):
        for a in range(0,len(vec2)):
            if list(vec1)[i] == list(vec2)[a]:
                numerator += list(vec1.values())[i]*list(vec2.values())[a]

    denominator_v1 = 0
    denominator_v2 = 0

    for i in vec1:
        denominator_v1 += (vec1[i])**2
    
    for i in vec2:
        denominator_v2 += (vec2[i])**2
    
    return numerator/math.sqrt(denominator_v1*denominator_v2)


def build_semantic_descriptors(sentences):
    d = {}
    for i in range(len(sentences)):
        sen_d = {}

        for w in sentences[i]:
            sen_d[w] = {}

            for other_w in sentences[i]:
                if other_w != w and other_w != " ":
                    if other_w not in sen_d[w].keys():
                        sen_d[w][other_w] = 1
                    else:
                        sen_d[w][other_w] += 1

        for w in list(sen_d.keys()):
            if other_w != " " and w != " ":
                if w not in d.keys():
                    d[w] = sen_d[w]
                else: 
                    for other_w in list(sen_d[w].keys()):
                        if other_w != w:
                            if other_w in d[w].keys():
                                d[w][other_w] += 1
                            else: 
                                d[w][other_w] = 1 

    return d


def build_semantic_descriptors_from_files(filenames):
    orig_text = ''
    for i in range(0, len(filenames)):
        orig_text += open(filenames[i], "r", encoding="latin1").read()
        orig_text += ' '        
    orig_text = orig_text.lower()
    orig_text = orig_text.replace(".", "?")
    orig_text = orig_text.replace("!", "?")
    orig_text = orig_text.replace("\n", " ")
    orig_text = orig_text.replace(",", " ")
    orig_text = orig_text.replace("-", " ")
    orig_text = orig_text.replace("--", " ")
    orig_text = orig_text.replace(";", " ")
    orig_text = orig_text.replace(":", " ")
    orig_text = orig_text.split("?")

    sens = []
    for i in range(0, len(orig_text)):
        words = orig_text[i].strip().split(" ")
        words = [word for word in words if word != ""]
        sens.append(words)


    '''for a in range(0, len(orig_text)):
        orig_text[a] = orig_text[a].replace("\n", "")
        orig_text[a] = orig_text[a].replace(",", "")
        orig_text[a] = orig_text[a].replace("-", "")
        orig_text[a] = orig_text[a].replace("--", "")
        orig_text[a] = orig_text[a].replace(";", "")
        orig_text[a] = orig_text[a].replace(":", "")
        orig_text[a] = orig_text[a].split(" ")'''

            #for t in range(0, len(orig_text[a])):
                #orig_text[a][t] = orig_text[a][t].strip("\n")


    return build_semantic_descriptors(sens)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    most_sim_val = -1
    most_sim_word = ""

    for i in range(0, len(choices)):
        if choices[i] in semantic_descriptors.keys():
            sim = similarity_fn(semantic_descriptors[choices[i]], semantic_descriptors[word])
            if sim > most_sim_val:
                most_sim_val = sim
                most_sim_word = choices[i]
    
    if most_sim_val == -1:
        return -1
    return most_sim_word


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    # making filename nice :)
    filename = str(filename)
    filename = filename.lower()
    fileList = filename.splitlines()
    list1 = []
    for i in range(len(fileList)):
        readable = fileList[i].split()
        list1.append(readable)
    print(list1)
    
    score = 0
    if len(list1[i]) <= 1:
        pass
    else:
        for i in range(len(list1)):
            q = list1[i][0]
            ans = list1[i][1]
            guess = most_similar_word(q, list1[i][2:], semantic_descriptors, similarity_fn)
            if guess == ans:
                score += 1
    
    return float((score/(len(list1)))*100)


if __name__ == "__main__":
    #print(len({"a": 1, "b": 2, "c": 3}))
    #print(open(filenames[0], "r", encoding="latin1"))
    filenames = ["swans_way.txt"]
    print(build_semantic_descriptors_from_files(filenames))
    