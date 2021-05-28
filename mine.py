
tagsList = ["造得了航母，拧得了螺丝", "带得了团队，码的了代码", "吹得了牛皮，做的了实事"]
notDoList = ["概念", "语言", "框架", "模式", "算法", "协议"]
doingList = ["了解协议", "理解算法", "应用模式", "分析框架", "总结概念"]


def printEnd(fun):
    """[summary]

    Args:
        fun ([type]): [description]
    """
    def inner():
        fun()
        print("-"*(3**3))
        print(" "*(3**3))
    return inner


@printEnd
def printTagsList():
    for item in tagsList:
        print(item, "!!!", sep="")


@printEnd
def printNotDoList():
    for item in notDoList:
        print("少谈点", item, "，多解决问题...", sep="")


@printEnd
def printDoingList():
    for item in doingList:
        print("多解决问题，多", item, "...", sep="")


def main():
    printTagsList()
    printNotDoList()
    printDoingList()


if __name__ == '__main__':
    main()
