Parallel Processing
###################

What it is
----------

We only employ **multi-process** parallelism as opposed
to **GPU** utilization (which can be far faster! ~100-1000x)

The waveform is divided into chunks which can be indexed by ``p``.
The first thing a spawned child process does is call the method & arguments it was dispatched with.

input arguments. The first thing a child does is run it's dispatch method, passing it's set of input arguments.
In this scheme, each child is given a *different* ``p``, indicating which chunk of the divided waveform
it's responsible for calculating. All children are given the *same* ``q``,

The chunks are then indexed, **starting at 0** by ``p``, so the calculation must be done accordingly.

.. _fix:

Gotcha
------
When child processes spawn, they import your script to access the function dispatched to them. This unintentionally
runs your script as a side-effect. To obviate the issue, you can enclose your script's main routine within::

    if __name__ == '__main__':
        ## Your Script ##

The ``__name__`` variable will only evaluate to ``'__main__'`` from within a directly executed module; as opposed to
within a module imported by another module, evaluating to the importing module's name in that case.
