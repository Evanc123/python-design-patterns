Important thing here is that update(), which is defined on the observer, gets passed the subject, so that the observer can get the data it needs from the subject.

Registering an observer =/= passing the observer to the update function

One thing that isn't clear to me is whether I need to pass the Subject class
to the instantiator of the observer, or if it is sufficient to pass it
in the update object.
