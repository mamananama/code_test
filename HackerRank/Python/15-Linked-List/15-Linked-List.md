# Linked List

https://www.hackerrank.com/challenges/30-linked-list/problem

#### Objective

## Today we will work with a Linked List. Check out the Tutorial tab for learning materials and an instructional video.

A Node class is provided for you in the editor. A Node object has an integer data field, `data`, and a Node instance pointer, , pointing to another node (i.e.: the next node in the list).

A Node insert function is also declared in your editor. It has two parameters: a pointer, , pointing to the first node of a linked list, and an integer, , that must be added to the end of the list as a new Node object.

#### Task

Complete the insert function in your editor so that it creates a new Node (pass as the Node constructor argument) and inserts it at the tail of the linked list referenced by the parameter. Once the new node is added, return the reference to the node.

Note: The argument is null for an empty list.

#### Input Format

The first line contains T, the number of elements to insert.
Each of the next lines contains an integer to insert at the end of the list.

#### Output Format

Return a reference to the node of the linked list.

#### Sample Input

```
STDIN   Function
-----   --------
4       T = 4
2       first data = 2
3
4
1       fourth data = 1
```

#### Sample Output

`2 3 4 1`

#### Explanation

, so your method will insert nodes into an initially empty list.
First the code returns a new node that contains the data value as the of the list. Then create and insert nodes , , and at the tail of the list.

### Solution

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        current = head
        if current is None:
            head = new_node
        else:
            while current.next:
                current = current.next
            current.next = new_node
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)

```

---

> Solution.insert()
>
> 1. 새로 추가할 `data`를 `Node()`로 생성, `new_node` 변수에 대입.
> 2. `current`: 현재 가리키고 있는 `Node()`를 담는 변수, 초기 값으로 `head` `Node()`를 가지도록 한다.
> 3. `current=head`가 `None`이라면 즉, `head`가 비어었다면, `head`가 `new_node` 가리키도록 한다.
> 4. `head`가 비어있지 않으면, `current.next`로 순회하면서 `current`가 가장 마지막 `Node()`를 가리키도록 한다.
> 5. `current.next = new_node`: 가장 마지막 `Node()`의 다음 노드가 `new_node`가리키도록 한다.
