# Strategy Pattern

Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

To me, it basically asks you to compose interfaces instead of using inheritence.

Synopsis of video (https://www.youtube.com/watch?v=v9ejT8FO-7I)

Imagine we have a city duck and a country duck class that inherit from Duck. Duck has methods like display, quack and fly.

Now we introduce a rubber duck, which has different behavior for fly.

We also have a cloud duck and a mountain duck, which implement the same version (it is copy pasted) of fly() -- they fly using jets (this is contrived but bear with it).

The strategy pattern posits that it is better to define a IFlyable interface, with concrete instantiations like DefaultFlying, NoFlying, JetFlying. Now, when we define a duck, we do so as:

```
class Duck:
    def __init__( flying_method: IFlyable ):
    	self.flying_method = flying_method


mountain_duck = Duck(JetFlying() )
```

in contrast to

```
class Duck:
	def __init__(self):
		pass

	def fly():
		print('this is the default flying method which must be later overrided')
```

Now from: https://www.youtube.com/watch?v=OMPfEXIlTVE

Sandy says don't use if statements

Conditionals breed!!

In other words, we inject the object to play the role of the thing that varies

This allows us to get pluggable behavior! It enables dependency injection / is? dependency injection. Moreso it is composition + dependency injection
