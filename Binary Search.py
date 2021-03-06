#There's one thing. The list needs to be sorted before hand.
def search(li, elem):
    index = -1 # Initialising the index as -1 so we know that the intem was not found if the returned value is '-1'
    start, end = 0, len(li) # Initialising the starting point and the ending point.
    middle = (start + end) // 2 # The middle element of the list/array. (Don't care what you call it.)

    while start < end: 
        if li[middle] > elem: # If the middle element is larger than the required element, then the required element is behind us.
            end = middle
            middle = (start + end) // 2
            print(li[middle])

        elif li[middle] < elem: # If the middle element is smaller than the required element, then the required element is ahead of us.
            start = middle
            middle = (start + end) // 2
            print(li[middle])
        
        if li[middle] == elem: # Checking if the current 'middle' index contains the element, if not then continue on with your day.
            index = middle
            break
    return index

# Main Program Starts
l = list(map(int, input("Enter your input: ").strip().split())) # Gotta take the input. Can't work without that you know.
elem = int(input("Enter element to look for: ")) # Taking the element of our concern.
print(sort(l))
print("Index: ", search(l, elem))
# Main Program Ends

# PROGRAM BY 'JAMES COLLINS'
