class Solution:
    def simplifyPath(self, path: str) -> str:
        res_paths = []

        paths = path.split("/")
        for p in paths:
            if not p or p == ".":
                continue
            elif p == "..":
                if res_paths:
                    res_paths.pop()
            else:
                res_paths.append(p)

        return "/" + "/".join(res_paths)
