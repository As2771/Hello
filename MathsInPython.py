# Python is a straight-forward language that on some levels can be used as a scripting language
# Compared to Java there's no boilerplate code required to do basic operations. So maths is also easy:

simple = 1 + 1
print(simple)
# prints '2'
# If you want to increment an existing variable:

simple += 2 # Equivalent of writing simple = simple + 2
print(simple)
# Prints '4'

# This applies to all operations:

sub = 3 - 2
print(sub)
sub -= 2
print(sub)
sub += 10
print(sub)
sub /= 2
print(sub)
sub *= 2
print(sub)
sub = 900
print (sub) # If you set the variable instead of "editing" it, it becomes that (in this case) number
sub = sub / 2# Less efficient than writing sub /= 2, but it produces the same result
print(sub)
#Printing division directly is also possible:
print(sub / 2)
print(sub)#But it doesn't set the variable permanently
sub = 10**2 # Powers is also an option
print(sub)
# There's no requirement to print afterwards, that is done here to show how the numbers behave
