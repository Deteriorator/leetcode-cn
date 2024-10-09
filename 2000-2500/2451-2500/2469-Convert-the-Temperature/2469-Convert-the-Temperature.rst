###############################################################################
2469. 温度转换
###############################################################################
..
    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    ", for paragraphs

给你一个四舍五入到两位小数的非负浮点数 ``celsius`` 来表示温度， 以 \
**摄氏度（Celsius）** 为单位。

你需要将摄氏度转换为 **开氏度（Kelvin）** 和 **华氏度（Fahrenheit）** ， 并以数组 \
``ans = [kelvin, fahrenheit]`` 的形式返回结果。

返回数组 ``ans`` 。 与实际答案误差不超过 ``10^-5`` 的会视为正确答案。

**注意：**

- ``开氏度 = 摄氏度 + 273.15``
- ``华氏度 = 摄氏度 * 1.80 + 32.00``

**示例 1：**

::

    输入：celsius = 36.50
    输出：[309.65000,97.70000]
    解释：36.50 摄氏度：转换为开氏度是 309.65 ，转换为华氏度是 97.70 。

**示例 2：**

::

    输入：celsius = 122.11
    输出：[395.26000,251.79800]
    解释：122.11 摄氏度：转换为开氏度是 395.26 ，转换为华氏度是 251.798 。


**提示：**

- ``0 <= celsius <= 1000``


###############################################################################
2469. Convert the Temperature
###############################################################################

You are given a non-negative floating point number rounded to two decimal \
places ``celsius``, that denotes the **temperature in Celsius**.

You should convert Celsius into **Kelvin** and **Fahrenheit** and return it \
as an array ``ans = [kelvin, fahrenheit]``.

Return the array ``ans``. Answers within ``10^-5`` of the actual answer will \
be accepted.

**Note that:**

- ``Kelvin = Celsius + 273.15``
- ``Fahrenheit = Celsius * 1.80 + 32.00``

**Example 1:**

::

    Input: celsius = 36.50
    Output: [309.65000,97.70000]
    Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.

**Example 2:**

::

    Input: celsius = 122.11
    Output: [395.26000,251.79800]
    Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.


**Constraints:**

- ``0 <= celsius <= 1000``
