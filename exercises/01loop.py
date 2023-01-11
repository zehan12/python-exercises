# Write a method called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example method call:
#

def p_times(value,num):
 if type(num) == int and type(value) == str:
  for i in range(num):
    print(value);
 else:
    print("Not Valid Input")
    
    
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there

