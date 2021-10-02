"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.
"""gives xth number of the fibonnaci sequence"""
def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra+rb
    pass

def longest_run(mylist, key):
    counter = 0
    max = 0
    for i in mylist:
        print(counter)
        if i == key:
            counter = counter + 1
            if i == mylist[len(mylist)-1]:
                max = counter

        else:
            if counter > max:
                max = counter
            counter = 0

    print(counter)
    return max
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    counter = 0
    max = 0
    if len(mylist) == 1:
        return mylist[1]
    first = longest_run_recursive[mylist[0:],key]
    second = longest_run_recursive[mylist[1:],key]
    if first == second:
        counter = counter + 1
    else:
        if counter > max:
            max = counter
        counter = 0
    return max


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([1,1,1,2,3,4,5,1,1,1,1], 1) == 4

foo(9)
test_longest_run()

