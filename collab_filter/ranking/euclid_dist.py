from math import sqrt
import recommendations

'''Code for calculating Euclidean Distance scores.
   Two preferences are mapped on axes to determine
   similarities''' 

def distance(y1, y2, x1, x2):
    '''Calculating Distance:
        1. Take the difference in each axis
        2. Square them
        3. Add them
        4. Take the sqaure root of the sum
       
       Returns a score between 0 (opposite) and 1
       (identical)'''

    dist = sqrt(pow(y1 - y2, 2)+pow(x1 - x2, 2))
    
    '''Invert distance so higher values mean higher 
       similarities'''

    inv_dist = 1/(1 + dist)

    return inv_dist

def euc_dist(pref_dict, cat1, cat2):
    '''Calculates the similarity between two categories
       and returns a Euclidean Distance score between 0
       (opposite) and 1 (identical)

        @pref_dict:  A dictionary of categories containing 
                    dictionaries of items and scores.
        @cat1: The first category to compare items from.
        @cat2: The category to compare items 2.'''

    shared = {} #Hold the items shared by both categories
    dist_scores = []

    '''Store all items that are in both categories'''

    for item in pref_dict[cat1]:
        if item in pref_dict[cat2]:
            shared[item] = 1

    '''If there are no shared items return 0'''

    if len(shared) == 0:
        return 0 

    '''Calculate the Euclidean Distance of all shared
       items and sum them'''

    for item in pref_dict[cat1]:
        if item in pref_dict[cat2]:
            score = pow(pref_dict[cat1][item] - pref_dict[cat2][item], 2)
            dist_scores.append(score)

    score_sum = sum(dist_scores)

#    dist_scores = sum([pow(pref_dict[cat1][item]-pref_dict[cat2][item],2)
 #                     for item in shared])
    '''Invert the sum'''

    invert_dist = 1/(1+sqrt(score_sum))
    
    return invert_dist

def test_euclid():
    print euc_dist(recommendations.critics, 'Lisa Rose', 'Gene Seymour')
    print euc_dist(recommendations.critics, 'Lisa Rose', 'Claudia Puig')


