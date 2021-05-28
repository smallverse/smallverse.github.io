#  readme.md
```
造得了航母，拧得了螺丝!!!
带得了团队，码的了代码!!!
吹得了牛皮，做的了实事!!!
---------------------------
                           
少谈点概念，多解决问题...
少谈点语言，多解决问题...
少谈点框架，多解决问题...
少谈点模式，多解决问题...
少谈点算法，多解决问题...
少谈点协议，多解决问题...
---------------------------
                           
多解决问题，多了解协议...
多解决问题，多理解算法...
多解决问题，多应用模式...
多解决问题，多分析框架...
多解决问题，多总结概念...
---------------------------
```
**by code:**
```

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

```


-----------------------------------------------------------------

<a name="hwy2C"></a>
## 1 Blog

---

> **_受此_**[**_文章_**](https://github.com/rainzhaojy/blogs/issues/1)**_影响，使用_**[**_issues_**](https://github.com/xiaonaoer/xiaonaoer.github.io/issues)**_作为blog，另可以直接关注我的[google 协作站点](https://big-ears-cat.jfzhai.top/)、[语雀](https://www.yuque.com/xiaonaoer)_**


---

<a name="fvcR9"></a>
## 2 推荐链接
> [链接](https://github.com/xiaonaoer/xiaonaoer.github.io/blob/master/referral_links.md)


---

<a name="YxIXb"></a>
## 3 书籍推荐
> [链接](https://github.com/xiaonaoer/xiaonaoer.github.io/blob/master/books.md)


---

<a name="9lCv2"></a>
## 4 工具
> [链接](https://github.com/xiaonaoer/xiaonaoer.github.io/blob/master/tools.md)



