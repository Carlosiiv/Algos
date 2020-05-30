# PART 1------------------------------------------------

x = [ [5,2,3], [10,8,9] ] 
students = [{'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# # answers:

# x[1][0] = 15
# print(x)

# students[0]['last_name'] = 'Bryant'
# print(students)

# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# z[0]['y']=30
# print(z)

#PART2---------------------------------------------------------------------------

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
         ]

# def itdic(arr):
    
#     for i in range(len(arr)):
        # print("First name - " + arr[i]['first_name'] +  ", Last name - "  + arr[i]['last_name'])
# itdic(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# PART 3--------------------------------------------------------------------------------

# def fname(arr,str):
#     for i in range(len(arr)):
#          print(students[i][str])
# fname(students,'first_name')

# def fname(arr,str):
#     for i in range(len(arr)):
#          print(students[i][str])
# fname(students,'last_name')

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict):
        for k in dict.keys():
            print(len(k),k)
            for i in dict[k]:
                print([i])

printInfo(dojo)

def printinf(diction):
    for k,i in diction.items():
        print(len(k),k)
        print(i)
printinf(dojo)