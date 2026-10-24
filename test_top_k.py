"""
Homework 5: The Top-K Countdown -- verification suite.

Run: python test_top_k.py
Prints the Success Token only if every check below passes.
"""

import base64
import hashlib
import random
import sys
from typing import List

from top_k import find_k_largest, heapify

ASSIGNMENT_ID = "HW05"


def get_student_id() -> str:
    """Prompt for the student's USI username; baked into the Success Token
    so a copied/shared token decodes to someone else's name, not yours."""
    student_id = input("Enter your USI username (e.g. cwill): ").strip()
    while not student_id:
        student_id = input("Username cannot be blank. Enter your USI username: ").strip()
    return student_id


def generate_token(assignment_id: str, student_id: str) -> str:
    digest = hashlib.sha256(f"CS311-{assignment_id}-{student_id}-VERIFIED".encode()).hexdigest()[:16]
    raw = f"CS311|{assignment_id}|{student_id}|PASS|{digest}"
    return base64.b64encode(raw.encode()).decode()


def print_success_banner(assignment_id: str) -> None:
    student_id = get_student_id()
    token = generate_token(assignment_id, student_id)
    print("\n" + "=" * 60)
    print(f"  ALL CHECKS PASSED -- {assignment_id}")
    print(f"  STUDENT: {student_id}")
    print("  SUCCESS TOKEN (paste this into Blackboard):")
    print(f"  {token}")
    print("=" * 60 + "\n")


def check(label: str, condition: bool, failures: list) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}")
    if not condition:
        failures.append(label)


def is_heap_property(data: List[float]) -> bool:
    for i in range(len(data)):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(data) and data[left] < data[i]:
            return False
        if right < len(data) and data[right] < data[i]:
            return False
    return True


def main() -> int:
    failures: list = []
    rng = random.Random(311)

    print("Testing heapify on random arrays...\n")
    for trial in range(15):
        size = rng.randint(1, 200)
        data = [rng.randint(0, 100_000) for _ in range(size)]
        original_multiset = sorted(data)
        heapify(data)
        check(f"trial {trial}: heapify preserves the multiset of values (size={size})", sorted(data) == original_multiset, failures)
        check(f"trial {trial}: heapify produces a valid min-heap (size={size})", is_heap_property(data), failures)

    if failures:
        print(f"\n{len(failures)} check(s) failed -- fix heapify before find_k_largest. No token issued.")
        return 1

    print("\nTesting find_k_largest against a sorted() reference...\n")
    for trial in range(20):
        size = rng.randint(1, 500)
        k = rng.randint(1, size)
        data = [rng.randint(0, 1_000_000) for _ in range(size)]
        expected = sorted(data, reverse=True)[:k]
        result = find_k_largest(data, k)
        check(f"trial {trial}: find_k_largest(data, k={k}) matches sorted(data)[-k:] reversed (size={size})", result == expected, failures)

    print()
    if failures:
        print(f"{len(failures)} check(s) failed. No token issued.")
        return 1

    print_success_banner(ASSIGNMENT_ID)
    return 0


if __name__ == "__main__":
    sys.exit(main())
