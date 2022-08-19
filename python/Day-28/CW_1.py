class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        splitted_path = A.split("/")

        path_stack = []
        for path in splitted_path:
            if path == "..":
                if path_stack:
                    path_stack.pop()
            elif path not in (".", ""):
                path_stack.append(path)

        return "/" + "/".join(path_stack)
