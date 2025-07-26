def fun(fruit = "orange"):  # this means if we call fun with no argument it will pass "orange"
    print("I like " + fruit)


fun("peach")  # here fruit will be peach not orange
fun("Guava")
fun()         # here fruit will be orange as there are no Arguments Passed
fun("Banana")
fun("Apple")