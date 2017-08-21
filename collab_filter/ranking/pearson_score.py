from math import sqrt
import recommendations

'''Code for calculating Pearson Scores.
   Data is normalized for a better comparison.
   Items in categories are plotted and a line of best
   fit is drawn between them''' 

def pearson_score(pref_dict, cat1, cat2):
    '''Calculates the similarity between two categories
       and returns a Pearson Score between -1
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

    items = len(shared)
    if items == 0:
        return 0 

    '''Add all preferences for both categories'''

    sum_cat1 = sum([pref_dict[cat1][item] for item in shared])
    sum_cat2 = sum([pref_dict[cat2][item] for item in shared])

    '''Sum of squares for both categories'''

    sum_sq_cat1 = sum([pow(pref_dict[cat1][item], 2) for item in shared])
    sum_sq_cat2 = sum([pow(pref_dict[cat2][item], 2) for item in shared])

    '''Sum of products'''

    sum_products = sum([pref_dict[cat1][item] * pref_dict[cat2][item] for item in shared])

    '''Pearson Score equation'''

    numerator = sum_products - (sum_cat1 * sum_cat2/items)
    denominator = sqrt((sum_sq_cat1 - pow(sum_cat1, 2)/items) *
                        (sum_sq_cat2 - pow(sum_cat2, 2)/items))    
    
    if denominator == 0:
        return 0

    return numerator/denominator

def test_pearson():
    print pearson_score(recommendations.critics, 'Lisa Rose', 'Gene Seymour')
    print pearson_score(recommendations.critics, 'Lisa Rose', 'Claudia Puig')

