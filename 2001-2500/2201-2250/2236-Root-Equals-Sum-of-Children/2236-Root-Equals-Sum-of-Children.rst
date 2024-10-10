###############################################################################
2236. 判断根结点是否等于子结点之和
###############################################################################
..
    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    ", for paragraphs

给你一个 **二叉树** 的根结点 ``root``， 该二叉树由恰好 ``3`` 个结点组成： 根结点、 \
左子结点和右子结点。

如果根结点值等于两个子结点值之和， 返回 ``true``， 否则返回 ``false``。
 
**示例 1：**

.. figure:: graph3drawio.png
    :name: Example 1

::

    输入：root = [10,4,6]
    输出：true
    解释：根结点、左子结点和右子结点的值分别是 10 、4 和 6 。
    由于 10 等于 4 + 6 ，因此返回 true 。

**示例 2：**

.. figure:: graph3drawio-1.png
    :name: Example 2

::

    输入：root = [5,3,1]
    输出：false
    解释：根结点、左子结点和右子结点的值分别是 5 、3 和 1 。
    由于 5 不等于 3 + 1 ，因此返回 false 。


**提示：**

- 树只包含根结点、左子结点和右子结点
- ``-100 <= Node.val <= 100``


###############################################################################
2236. Root Equals Sum of Children
###############################################################################

You are given the ``root`` of a **binary tree** that consists of exactly 3 \
nodes: the root, its left child, and its right child.

Return ``true`` if the value of the root is equal to the **sum** of the \
values of its two children, or ``false`` otherwise.

**Example 1:**

.. figure:: graph3drawio.png
    :name: Example 1-1

::

    Input: root = [10,4,6]
    Output: true
    Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
    10 is equal to 4 + 6, so we return true.

**Example 2:**

.. figure:: graph3drawio-1.png
    :name: Example 2-1

::

    Input: num1 = -10, num2 = 4
    Output: -6
    Explanation: num1 + num2 = -6, so -6 is returned.


**Constraints:**

- The tree consists only of the root, its left child, and its right child.
- ``-100 <= Node.val <= 100``
