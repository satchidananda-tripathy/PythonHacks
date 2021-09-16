##Here **keyval accepts data as tuples.

def get_details(**keyval):
    print(keyval)

print('------Student Details-----')
get_details(id=1,name='sachin',mark=20)
get_details(id=2,name='dravid',mark=21)
get_details(id=3,name='laxman',mark=22)
get_details(id=4,name='yuvraj',mark=23)