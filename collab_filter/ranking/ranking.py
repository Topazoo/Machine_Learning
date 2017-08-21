import recommendations
from euclid_dist import euc_dist
from pearson_score import pearson_score

def best_match(pref_dict, category, n=5, func=pearson_score):
    '''Returns the top n most similar categories to a given category.
       @pref_dict:  A dictionary of categories containing 
                    dictionaries of items and scores.
       @category:   The category to find similar scores for.
       @n:          The number of scores to return.
       @func:       The function to use to match similarities.'''

    scores = [] # List of all scores from the given function 

    '''Get all scores for the given function'''
    
   # for cat in pref_dict:
    #    if cat != category:
     #       score = func(pref_dict, category, cat)
      #      scores.append((score, cat))

    scores=[(func(pref_dict, category,other),other)
                for other in pref_dict if other!=category]

    '''Sort them from highest to lowest'''

    scores.sort()
    scores.reverse()

    '''Return the top n scores'''

    return scores[0:n]

def recommend(pref_dict, category, func=pearson_score):
    '''Makes a recommendation by weighing the items in each category
       based on the similarity of each category to the given category.

       @pref_dict:  A dictionary of categories containing 
                    dictionaries of items and scores.
       @category:   The category to find similar scores for.
       @func:       The function to use to match similarities.'''

    totals = {}
    sums = {}
    rankings = []

    '''Loop through all categories'''

    for cat in pref_dict:

        '''Skip passed category'''

        if cat == category:
            continue

        '''Get similarity and skip if similarity is 0 or less'''

        similarity = func(pref_dict, category, cat)
        if similarity <= 0:
            continue

        '''For each item not in the passed category, calculate 
           similarity * score and add it to the item's weighted sum'''

        for item in pref_dict[cat]:
            if item not in pref_dict[category] or pref_dict[category][item] == 0:
           
                '''Calculate weighted score'''

                totals.setdefault(item, 0)
                totals[item] += pref_dict[cat][item] * similarity

                '''Add it to the item's sum'''

                sums.setdefault(item, 0)
                sums[item] += similarity

    '''For each item in totals, normalize each and add to rankings'''

    for item, total in totals.items():
        normalized = total/sums[item]
        rankings.append((normalized, item))

    '''Sort highest to lowest'''
    rankings.sort()
    rankings.reverse()

    return rankings

def test_rankings():
    print best_match(recommendations.critics, 'Toby', n=3)
    print recommend(recommendations.critics, 'Toby')
    print recommend(recommendations.critics, 'Toby', euc_dist)

test_rankings()