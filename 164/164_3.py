from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        for i in range(1, len(searchWord) + 1):
            word = searchWord[:i]
            result = []
            res.append(result)
            remove_list = []
            for p in products:
                if p.startswith(word):
                    result.append(p)
                    if len(result) == 3:
                        break
                else:
                    remove_list.append(p)

            for r in remove_list:
                products.remove(r)

        return res
