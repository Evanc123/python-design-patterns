Can think of the strategy pattern as:
"What if I assumed I had a thing that implemented such and such method",
and proceeded to use that thing. That is dependency injection.

But how do I construct such a thing?

We can defer creation of objects by using a factory.

Sometimes we want to co-create concrete classes. There we use an abstract factory.
