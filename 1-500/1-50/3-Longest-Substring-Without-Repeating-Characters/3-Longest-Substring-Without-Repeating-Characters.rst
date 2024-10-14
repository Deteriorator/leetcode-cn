###############################################################################
3. 无重复字符的最长子串
###############################################################################
..
    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    ", for paragraphs

给定一个字符串 ``s`` ，请你找出其中不含有重复字符的 **最长** [子串]_ 的长度。

.. [子串] 子字符串 是字符串中连续的 非空 字符序列。

**示例 1：**

::

    输入: s = "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

**示例 2：**

::

    输入：s = "bbbbb"
    输出：1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

**示例 3：**

::

    输入：s = "pwwkew"
    输出：3
    解释：因为无重复字符的最长子串是 "wke"，所以其长度为 3。
    请注意， 你的答案必须是 子串 的长度， "pwke" 是一个子序列， 不是子串。

**提示：**

- ``0 <= s.length <= 5 * 104``
- ``s`` 由英文字母、数字、符号和空格组成


###############################################################################
3. Longest Substring Without Repeating Characters
###############################################################################

Given a string ``s``, find the length of the **longest** [substring]_ without \
repeating characters.

.. [substring] A **substring** is a contiguous **non-empty** sequence of \
   characters within a string.

**Example 1:**

::

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

**Example 2:**

::

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

**Example 3:**

::

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and \
    not a substring.

**Constraints:**

- ``0 <= s.length <= 5 * 104``
- ``s`` consists of English letters, digits, symbols and spaces.
