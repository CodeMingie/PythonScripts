from collections import defaultdict

interests = [(0, "A"), (1, "B")]

def data_scientists(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

print(data_scientists("B"))
