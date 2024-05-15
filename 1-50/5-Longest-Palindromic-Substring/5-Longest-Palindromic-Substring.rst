###############################################################################
5. 最长回文子串
###############################################################################
..
    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    ", for paragraphs

给你一个字符串 ``s``， 找到 ``s`` 中最长的 [回文]_ [子串]_。

如果字符串的反序与原始字符串相同， 则该字符串称为回文字符串。

.. [回文] 如果字符串向前和向后读都相同， 则它满足 **回文性**。
.. [子串] **子字符串** 是字符串中连续的 **非空** 字符序列。

**示例 1：**

::

    输入：s = "babad"
    输出："bab"
    解释："aba" 同样是符合题意的答案。

**示例 2：**

::

    输入：s = "cbbd"
    输出："bb"

**提示：**

- ``1 <= s.length <= 1000``
- ``s`` 仅由数字和英文字母组成


###############################################################################
5. Longest Palindromic Substring
###############################################################################

Given a string ``s``, return the longest [palindromic]_ [substring]_ in ``s``.

.. [palindromic] A string is **palindromic** if it reads the same forward and \
   backward.
.. [substring] A **substring** is a contiguous **non-empty** sequence of \
   characters within a string.

**Example 1:**

::

    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.


**Example 2:**

::

    Input: s = "cbbd"
    Output: "bb"

**Constraints:**

- ``1 <= s.length <= 1000``
- ``s`` consist of only digits and English letters.
