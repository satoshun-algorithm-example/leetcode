#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda a: (-a[0], a[1]))
        sort = []

        for person in people:
            sort.insert(person[1], person)

        return sort
