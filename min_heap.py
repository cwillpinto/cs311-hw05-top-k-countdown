"""
Homework 5: The Top-K Countdown -- MinHeap.

Copy in your completed MinHeap class from Lab 10 (test_triage.py) --
insert, _sift_up, _sift_down, and extract_min all need to already
work correctly before you start heapify/find_k_largest in top_k.py.
"""

from typing import List


class MinHeap:
    def __init__(self) -> None:
        self._data: List[float] = []

    def __len__(self) -> int:
        return len(self._data)

    def insert(self, value: float) -> None:
        # TODO: paste your Lab 10 solution
        raise NotImplementedError

    def _sift_up(self, index: int) -> None:
        # TODO: paste your Lab 10 solution
        raise NotImplementedError

    def _sift_down(self, index: int) -> None:
        # TODO: paste your Lab 10 solution
        raise NotImplementedError

    def extract_min(self) -> float:
        # TODO: paste your Lab 10 solution
        raise NotImplementedError
