###############################################################################
326. 3 的幂
###############################################################################
..
    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    ", for paragraphs

给定一个整数， 写一个函数来判断它是否是 3 的幂次方。 如果是， 返回 ``true``； 否则\
， 返回 ``false``。

整数 ``n`` 是 3 的幂次方需满足： 存在整数 ``x`` 使得 ``n == 3^x``
 
**示例 1：**

::

    输入：n = 27
    输出：true

**示例 2：**

::

    输入：n = 0
    输出：false

**示例 3：**

::

    输入：n = 9
    输出：true

**示例 4：**

::

    输入：n = 45
    输出：false 


**提示：**

- ``-2^31 <= n <= 2^31 - 1``

**进阶：** 你能不使用循环或者递归来完成本题吗？

###############################################################################
326. Power of Three
###############################################################################

Given an integer ``n``, return ``true`` if it is a power of three. Otherwise, \
return ``false``.

An integer ``n`` is a power of three, if there exists an integer ``x`` such \
that ``n == 3x``.
 

**Example 1:**

::

    Input: n = 27
    Output: true
    Explanation: 27 = 33

**Example 2:**

::

    Input: n = 0
    Output: false
    Explanation: There is no x where 3x = 0.

**Example 3:**

::

    Input: n = -1
    Output: false
    Explanation: There is no x where 3x = (-1).


**Constraints:**

- ``-2^31 <= n <= 2^31 - 1``

**Follow up:** Could you solve it without loops/recursion?