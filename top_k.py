"""
Homework 5: The Top-K Countdown -- starter.

Complete heapify and find_k_largest below. Requires your completed
MinHeap in min_heap.py (copy in your Lab 10 solution first). See
HW5_The_Top_K_Countdown.md, Part B, for the full requirements.
"""

from typing import List

from min_heap import MinHeap


def heapify(data: List[float]) -> None:
    """
    Convert `data` in place into a valid min-heap using bottom-up
    construction: call _sift_down on every non-leaf index, starting
    from the LAST non-leaf index and working back to the root. Do not
    build this via repeated insert() calls.
    """
    # TODO
    raise NotImplementedError


def find_k_largest(data: List[float], k: int) -> List[float]:
    """
    Return the k largest values in `data`, in descending order,
    without fully sorting `data`. Use a min-heap of size k: for each
    element, insert it if the heap has fewer than k items; otherwise,
    replace the heap's minimum if the element is larger than it.
    Must run in O(n log k), not O(n log n).
    """
    # TODO
    raise NotImplementedError
