#
# @lc app=leetcode id=5231 lang=python3
#
# [5231]
#
from typing import List


# @lc code=start
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        sub_folder = []
        for path in folder:
            is_match = False
            for i, sub in enumerate(sub_folder):
                if (sub + "/").startswith(path + "/"):
                    sub_folder[i] = path
                    is_match = True
                    break
                if (path + "/").startswith(sub + "/"):
                    is_match = True
                    break
            if not is_match:
                sub_folder.append(path)

        return sub_folder

# @lc code=end
