class Solution:
    def simplifyPath(self, path: str) -> str:
        path_parts = []
        i = 0
        while i < len(path):
            if path[i] == "/":
                i += 1
                continue

            part_end = i + 1
            while part_end < len(path) and path[part_end] != "/":
                part_end += 1

            part = path[i:part_end]
            if part == ".":
                i = part_end
            elif part == "..":
                if path_parts:
                    path_parts.pop()
            else:
                path_parts.append(part)
            i = part_end

        return "/" + "/".join(path_parts)
