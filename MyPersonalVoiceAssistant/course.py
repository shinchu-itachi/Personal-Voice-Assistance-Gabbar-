#Below is the code for the above mentioned question

def find_friends(friends_pairs):
    friends_dict = {}
    seen_pairs = []
    for pair in friends_pairs:
        if len(pair) > 1:
            if sorted(pair) not in seen_pairs:
                seen_pairs.append(sorted(pair))
                for friend in pair:
                    if friend not in friends_dict:
                        friends_dict[friend] = 1
                    else:
                        friends_dict[friend] += 1
    return friends_dict



print(find_friends([[2,3],[3,4],[5],[3,6],[6,3]]))