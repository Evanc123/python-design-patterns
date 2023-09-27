Imagine you are designing a class for a starbucks order. We want to calculate the cost
of arbitrary order.

Iced, steamed, espresso shot, oat milk, etc

There shouldn't be a Beverage class that has all of these

nor should there be a set of booleans that we set

what if you have a Tea class. then adding chocolate doesn't make much sense( or maybe they would let you do that LOL)

In python we have function decorators because they are first class fns:

```
def repeat_decorator(fn):
    def decorated_fn():
        fn()
        fn()
    # returns a function
    return decorated_fn

def hello_world():
    print ("Hello world!")

hello_world_twice = repeat_decorator(hello_world)

# call the function
hello_world_twice()
```
