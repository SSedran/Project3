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
    dic = {}
    for i in range(len(sentences)):
        sen_dic = {}

        for w in sentences[i]:
            sen_dic[w] = {}

            for other_w in sentences[i]:
                if other_w != w and other_w != " ":
                    if other_w not in sen_dic[w].keys():
                        sen_dic[w][other_w] = 1
                    else:
                        sen_dic[w][other_w] += 1

        for w in list(sen_dic.keys()):
            if other_w != " ":
                if other_w not in dic.keys():
                    dic[w] = sen_dic[w]
                else: 
                    if other_w:
                        if other_w not in sen_dic[w].keys():
                            sen_dic[w][other_w] = 1
                        else:
                            sen_dic[w][other_w] += 1

    return dic



def build_semantic_descriptors_from_files(filenames):
    #for i in range    
    pass




def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass

if __name__ == "__main__":
    print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
    #print(len({"a": 1, "b": 2, "c": 3}))