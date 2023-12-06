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
    common_keys = set(vec1.keys()).intersection(set(vec2.keys()))
    dot_product = 0
    for k in common_keys:
        dot_product += vec1.get(k, 0) * vec2.get(k, 0)

    sum_of_squares_vec1 = 0
    for v in vec1.values():
        sum_of_squares_vec1 += v**2
    sum_of_squares_vec2 = 0
    for v in vec2.values():
        sum_of_squares_vec2 += v**2

    magnitudes = math.sqrt(sum_of_squares_vec1) * math.sqrt(sum_of_squares_vec2)
    if magnitudes == 0:
        return -1
    return dot_product / magnitudes


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
    orig_text = orig_text.replace("/", " ")
    orig_text = orig_text.replace("|", " ")
    orig_text = orig_text.replace("(", " ")
    orig_text = orig_text.replace(")", " ")
    orig_text = orig_text.replace("\"", " ")
    orig_text = orig_text.replace("\'", " ")
    orig_text = orig_text.replace("*", " ")
    orig_text = orig_text.split("?")

    sens = []
    for i in range(0, len(orig_text)):
        words = orig_text[i].strip().split(" ")
        words = [word for word in words if word != ""]
        if len(words) !=0:
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
    most_sim_val = -10
    most_sim_word = choices[0]

    if word in semantic_descriptors.keys():
        for i in range(len(choices)):
            if choices[i] in semantic_descriptors:
                sim = similarity_fn(semantic_descriptors[choices[i]], semantic_descriptors[word])
                if sim > most_sim_val:
                    most_sim_val = sim
                    most_sim_word = choices[i]
    
    return most_sim_word


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    # making filename nice :)
    with open (filename, "r", encoding="latin1") as f: 
        data = f.readlines()
        list1 = []
        for i in range(len(data)):
            list1.append(data[i].lower().split())
    
    score = 0
    for i in range(len(list1)):
        q = list1[i][0]
        ans = list1[i][1]
        guess = most_similar_word(q, list1[i][2:], semantic_descriptors, similarity_fn)
        if guess == ans:
            score += 1
    
    return score/(len(list1))*100


if __name__ == "__main__":
    #print(len({"a": 1, "b": 2, "c": 3}))
    #print(open(filenames[0], "r", encoding="latin1"))
    #filename = ["swans_way.txt"]
    #semantic_descriptors = build_semantic_descriptors_from_files(filename)
    #print(run_similarity_test(filename, semantic_descriptors, cosine_similarity))
    #print(build_semantic_descriptors_from_files(filename))

    sem_descriptors = build_semantic_descriptors_from_files(["war_and_peace.txt", "swans_way.txt"])
    res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
    print(res, "%of the guesses were correct")
    