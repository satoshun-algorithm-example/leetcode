#
# @lc app=leetcode id=5231 lang=python3
#
# [5231]
#
from typing import List
import re


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        sub_folder = []
        sub_re = ""
        sub_re_re = None
        for path in folder:
            is_match = False

            if sub_re:
                is_match = sub_re_re.match(path + "/")

            if not is_match:
                if sub_re:
                    sub_re += "|"
                sub_re += path + "/"
                sub_re_re = re.compile(sub_re)
                sub_folder.append(path)

        return sub_folder
