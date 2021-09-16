import pandas as pd

'''Amgen Python question:

Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time, the ID of the user making the access, and the resource ID.

The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.

Example 1:
logs1 = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_22", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_6"],
["54359", "user_1", "resource_3"],
]


We would like to compute user sessions, specifically:
write a function that takes the logs and returns a data structure that associates to each user their earliest and latest access times.

Example 1 should return:
{'user_1': [54001, 58523],
'user_2': [54060, 62314],
'user_3': [53760, 53760],
'user_5': [53651, 53651],
'user_6': [2, 215],
'user_7': [400, 400],
'user_8': [100, 100],
'user_22': [58522, 58522],
}

Example 2:
logs2 = [
["300", "user_1", "resource_3"],
["599", "user_1", "resource_3"],
["900", "user_1", "resource_3"],
["1199", "user_1", "resource_3"],
["1200", "user_1", "resource_3"],
["1201", "user_1", "resource_3"],
["1202", "user_1", "resource_3"]
]

Example 2 should return:
{'user_1': [300, 1202]}

Complexity analysis variables:

n: number of logs in the input
'''

logs1 = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_22", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_6"],
["54359", "user_1", "resource_3"],
]

user_login_details ={items[1]:items[0] for items in logs1 }
users = pd.DataFrame(data=logs1)

sorted_users = users.sort_values(by=1)

print(sorted_users.groupby(1).first())
print(sorted_users.groupby(1).last())








