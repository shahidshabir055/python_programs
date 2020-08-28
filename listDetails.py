#Do not remove the below import statement
import sys

'''This function provides the capacity, size and space left in the list.
You can invoke it to get the details of the list'''
"""
def list_details(lst):
    #Number of elements that can be stored in the list
    print("Capacity:", (sys.getsizeof(lst)-36)//4)
    Capacity=(sys.getsizeof(lst)-36)//4
    print("capacity is: ",Capacity)
    #Number of elements in the list
    print("Size:", len(lst))

    #Number of elements that can be accommodated in the space left
    print("Space Left:", ((sys.getsizeof(lst)-36)//4 - len(lst)))

    #formula changes based on the system architecture
    #(size-36)/4 for 32 bit machines and
    #(size-64)/8 for 64 bit machines

    # 36, 64 - size of an empty list based on machine
    # 4, 8 - size of a single element in the list based on machine

marias_lst=[]
print("Empty list created!!!")
print("List details:")
list_details(marias_lst)
"""
def syedlist(lst):
    #capacity
    print("capacity :",(sys.getsizeof(lst)-64)//8)
    #size
    print("Size :",len(lst))
    #available space
    print("available space :",((sys.getsizeof(lst)-64)//8-len(lst)))
    print(lst)
my_list=[1,2,3,4,5]
print("empty list created")
print("list details")
syedlist(my_list)
#insertion
print("after appending")
my_list.append('sugar')
print("list details")
print("after second appending")
my_list.append('mobile')
my_list.append('mobile')
my_list.append('mobile')
my_list.append('mobile')
print("list details")
syedlist(my_list)
print("after insert")
my_list.insert(0,'shahid')
print("list details")
syedlist(my_list)
print("afte removing an element")
my_list.remove('shahid')
syedlist(my_list)
print("after delettion")
my_list.pop(5)
syedlist(my_list)