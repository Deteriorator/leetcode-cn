###############################################################################
2586. 统计范围内的元音字符串数
###############################################################################
..
    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    ", for paragraphs

给你一个下标从 **0** 开始的字符串数组 ``words`` 和两个整数： ``left`` 和 ``right`` 。

如果字符串以元音字母开头并以元音字母结尾， 那么该字符串就是一个 **元音字符串**， 其中\
元音字母是 ``'a'``、 ``'e'``、 ``'i'``、 ``'o'``、 ``'u'``。

返回 ``words[i]`` 是元音字符串的数目， 其中 ``i`` 在闭区间 ``[left, right]`` 内。

**示例 1：**

::

    输入：words = ["are","amy","u"], left = 0, right = 2
    输出：2
    解释：
    - "are" 是一个元音字符串，因为它以 'a' 开头并以 'e' 结尾。
    - "amy" 不是元音字符串，因为它没有以元音字母结尾。
    - "u" 是一个元音字符串，因为它以 'u' 开头并以 'u' 结尾。
    在上述范围中的元音字符串数目为 2 。

**示例 2：**

::

    输入：words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
    输出：3
    解释：
    - "aeo" 是一个元音字符串，因为它以 'a' 开头并以 'o' 结尾。
    - "mu" 不是元音字符串，因为它没有以元音字母开头。
    - "ooo" 是一个元音字符串，因为它以 'o' 开头并以 'o' 结尾。
    - "artro" 是一个元音字符串，因为它以 'a' 开头并以 'o' 结尾。
    在上述范围中的元音字符串数目为 3 。



**提示：**

- ``1 <= words.length <= 1000``
- ``1 <= words[i].length <= 10``
- ``words[i]`` 仅由小写英文字母组成
- ``0 <= left <= right < words.length``


###############################################################################
2586. Count the Number of Vowel Strings in Range
###############################################################################

You are given a **0-indexed** array of string ``words`` and two integers \
``left`` and ``right``.

A string is called a **vowel string** if it starts with a vowel character and \
ends with a vowel character where vowel characters are ``'a'``, ``'e'``, \
``'i'``, ``'o'``, and ``'u'``.

Return the number of vowel strings ``words[i]`` where ``i`` belongs to the \
inclusive range ``[left, right]``.

**Example 1:**

::

    Input: words = ["are","amy","u"], left = 0, right = 2
    Output: 2
    Explanation: 
    - "are" is a vowel string because it starts with 'a' and ends with 'e'.
    - "amy" is not a vowel string because it does not end with a vowel.
    - "u" is a vowel string because it starts with 'u' and ends with 'u'.
    The number of vowel strings in the mentioned range is 2.

**Example 2:**

::

    Input: words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
    Output: 3
    Explanation: 
    - "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
    - "mu" is not a vowel string because it does not start with a vowel.
    - "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
    - "artro" is a vowel string because it starts with 'a' and ends with 'o'.
    The number of vowel strings in the mentioned range is 3.



**Constraints:**

- ``1 <= words.length <= 1000``
- ``1 <= words[i].length <= 10``
- ``words[i]`` consists of only lowercase English letters.
- ``0 <= left <= right < words.length``
