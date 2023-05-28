"""
In the event you have an iterable that you need to process in bulk, and the processing method raises an exception,
but doesn't provide any indication as to which item/s in the iterable were the cause of the exception, and the
performance impact of running the iterable items one by one is too great, this may be the solution for you.

The aim is to take the entire iterable, try and process all items in the iterable in one go. If this fails the iterable
is then split into two halves, and processing is reattempted. This process will repeat until we are left with a known
set of processed 'good', and unprocessed 'bad' items.

It's worth noting that this algorithm won't be efficient in large data sets where there will be large numbers of
exception triggers relatively evenly dispersed throughout the input iterable. It will be most efficient when there are
as few exception scenarios as possible.

In the vast majority of cases there will be better approaches to this problem. This particular approach was the best
solution to cover exception handling gaps present in a proprietary API.
"""

from typing import List, Tuple, Callable, Iterable


def divide_and_conquer_iterable(
    iterable: Iterable, action: Callable
) -> Tuple[List, List]:
    """
    Takes an iterable and attempts to run an action over the entire iterable.

    If some items in the iterable result in the action raising an exception, the iterable will be split into two halves.
    Each half will then be processed again.

    The aim is to end up with two sets of know good, and known bad items.

    :param iterable: Iterable to process.
    :param action: Action to perform on the iterable.
    :return: Bad items in input iterable, good items in input iterable.
    """

    stack = [iterable]
    good_items = []
    bad_items = []

    while stack:
        sublist = stack.pop()

        try:
            action(sublist)
            good_items.extend(sublist)
        except Exception:
            if len(sublist) == 1:
                bad_items.extend(sublist)
            else:
                mid = len(sublist) // 2
                stack.append(sublist[:mid])
                stack.append(sublist[mid:])

    return bad_items, good_items
