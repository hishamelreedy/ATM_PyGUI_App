# #tuple
# #A tuple is a collection which is ordered and unchangeable
# thistuple = ("apple", "banana", "cherry")
# thistuple=list(thistuple)
# thistuple[1]="x"

# x = range(6)
# for n in x:
#     print(n)
#     for n in x:
#         print(n)

#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "brand": "k",
#   "year": 1964
# }

# print(thisdict)
# thidict_model_elem = thisdict["year"]
# print(thidict_model_elem)

# # The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable
# mylist = ['apple', 'banana', 'cherry']
# mylist= list(mylist)
# mylist[1] = "strawberry"
# print(mylist)

# x = range(3, 6)
# for n in x:
#   print(n)
  
# x = range(6)
# for n in x:
#     print(n,end=" ")

# list(range(0, 30, 5))

# print ("Hi")
# print ('Hello world')
# print ('I\'m muhammad')
# print ("I'm Hussein")

# #complex
# a = 2+3j
# print('a =',a)
# print('a =',a.real)
# print('a =',a.imag)
# print('Type of a is',type(a))

# #lists 
# #List is a collection which is ordered and changeable. Allows duplicate members.
# thislist = ["apple", "banana", "cherry"]


# #tuple
# #A tuple is a collection which is ordered and unchangeable
# thistuple = ("apple", "banana", "cherry")


# #A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# x = thisdict["model"]

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# print(thisdict["model"])


# x = range(6)
# for n in x:
#   print(n)
  

# x = range(3, 6)
# for n in x:
#   print(n)
  
# x = range(6)
# for n in x:
#     print(n,end=" ")

# list(range(0, 30, 5))
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year" : 1964
# }
# print(thisdict)

# x = thisdict["model"]

# print(x)

# #A set is a collection which is unordered and unindexed. In Python, sets are written with curly brackets.

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# print(thisset[1])


# # The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable
# mylist = ['apple', 'banana', 'cherry']
# mylist= frozenset(mylist)
# mylist[1] = "strawberry"

# #bool: Booleans represent one of two values: True or False.
# print(10 > 9)
# print(bool("Hello"))
# print(bool(15))
# print(10 > 9)
# print(1 > 2)
# print(bool("Hello"))
# print(bool(15)     )
# print(bool(False)   )
# print(bool(None)    )
# print(bool(0)       )
# print(bool("")      ) #empty string
# print(bool(())      ) #empty tuple
# print(bool([])      ) #empty list
# print(bool({})      ) #empty set

# # bytes  converts an object to immutable byte represented object of given size and data.
# empty_bytes =bytes(4)
# print(empty_bytes)
# print(type(empty_bytes))

# data=bytes(b'\xFF\xFF')
# print(data)
# data=bytes(b'\xFF\xFF')
# data[0]=1
# print(data)

# #convert list to bytes
# rList = [1, 2, 3, 4, 5]
# arr = bytes(rList)
# print(arr)

# str1 = 'HellÖrHeaven'  
# # Giving ascii encoding and ignore error 
# print ("Byte conversion with ignore error : " +
#       str(bytes(str1, 'ascii', errors = 'ignore')))  
  
# # Giving ascii encoding and replace error 
# print ("Byte conversion with replace error : " +
#       str(bytes(str1, 'ascii', errors = 'replace')))  
  
# # Giving ascii encoding and strict error 
# # throws exception 
# print ("Byte conversion with strict error : " +
#       str(bytes(str1, 'ascii', errors = 'strict')))
      
# data="\x68\x65\x6c\x6c\x6f"
# print ("Byte conversion with ignore error : " +
#       str(bytes(data, 'ascii', errors = 'ignore')))  
      
# #bytearray
# mutable_empty_bytes =bytearray(4)
# print(mutable_empty_bytes)
# print(type(mutable_empty_bytes))

# mutable_empty_bytes =bytearray(b'\xF1\xF2\xF3\xF4')
# print(mutable_empty_bytes)
# print(type(mutable_empty_bytes))

# mutable_empty_bytes =bytearray(b'\xF1\xF2\xF3\xF4')
# mutable_empty_bytes[0]=0
# mutable_empty_bytes.append(255)
# print(mutable_empty_bytes)
# print(type(mutable_empty_bytes))

# #The memoryview() function returns a memory view object of the given argument this is done via Python Buffer Protocol
# #The buffer protocol allows one object to expose its internal data (buffers) and the other to access those buffers without intermediate copying.

# byte_array = bytearray('XYZ', 'utf-8') 
# print('Before update:', byte_array) 
  
# mem_view = memoryview(byte_array) 
  
# # update 2nd index of mem_view to J  
# mem_view[2]= 74
# print('After update:', byte_array)


# import time
# for n in (100000, 200000, 300000, 400000):
#     data = 'x'*n
#     start = time.time()
#     while data:
#         data = data[1:]
#     print ('bytes', n, time.time()-start)
    

# for n in (100000, 200000, 300000, 400000):
#     data = 'x'*n
#     start = time.time()
#     data=bytearray(data,'utf-8')
#     data = memoryview(data)
#     while data:
#         data = data[1:]
#     print ('memoryview', n, time.time()-start)
    
# #Bitwise operators 
# a = 60            # 60 = 0011 1100 
# b = 13            # 13 = 0000 1101 
# c = 0

# c = a & b;        # 12 = 0000 1100
# print ("Line 1 - Value of c is ", c)

# c = a | b;        # 61 = 0011 1101 
# print ("Line 1 - Value of c is ", c)

# c = a ^ b;        # 49 = 0011 0001
# print ("Line 1 - Value of c is ", c)

# c = ~a;           # -61 = 1100 0011
# print ("Line 1 - Value of c is ", c)

# c = a << 2;       # 240 = 1111 0000
# print ("Line 1 - Value of c is ", c)

# c = a >> 2;       # 15 = 0000 1111
# print ("Line 1 - Value of c is ", c)




# #membership operators
# a = 10
# b = 20
# list = [1, 2, 3, 4, 5 ];

# if ( a in list ):
#    print "Line 1 - a is available in the given list"
# else:
#    print "Line 1 - a is not available in the given list"

# if ( b not in list ):
#    print "Line 2 - b is not available in the given list"
# else:
#    print "Line 2 - b is available in the given list"
   

# #identity operators   
# a = 20
# b = 20

# if ( a is b ):
#    print "Line 1 - a and b have same identity"
# else:
#    print "Line 1 - a and b do not have same identity"

# if ( id(a) == id(b) ):
#    print "Line 2 - a and b have same identity"
# else:
#    print "Line 2 - a and b do not have same identity"

# b = 30
# if ( a is b ):
#    print "Line 3 - a and b have same identity"
# else:
#    print "Line 3 - a and b do not have same identity"

# if ( a is not b ):
#    print "Line 4 - a and b do not have same identity"
# else:
#    print "Line 4 - a and b have same identity"