import os

def SortMessage(msg, limit): 
    final = []
    words = msg.split(" ")
    build = ""
    for i in words:
        if len(i) > limit:
            raise
        if len(build + f" {i}") <= limit:
            build += f" {i}"
        else:
            final.append(build)
            build = i
    final.append(build)
    final = f"{os.linesep}".join([str(elem) for elem in final])
    final = final[1:]
    return final
