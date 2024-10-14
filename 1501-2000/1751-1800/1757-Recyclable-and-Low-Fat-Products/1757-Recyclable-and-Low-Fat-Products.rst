###############################################################################
1757. 可回收且低脂的产品
###############################################################################
..
    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    ", for paragraphs

表： ``Products``

::

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | product_id  | int     |
    | low_fats    | enum    |
    | recyclable  | enum    |
    +-------------+---------+
    product_id 是该表的主键（具有唯一值的列）。
    low_fats 是枚举类型， 取值为以下两种 ('Y', 'N')， 其中 'Y' 表示该产品是低脂产\
    品， 'N' 表示不是低脂产品。
    recyclable 是枚举类型， 取值为以下两种 ('Y', 'N')， 其中 'Y' 表示该产品可回\
    收，而 'N' 表示不可回收。
 
**示例 1：**

::

    输入：
    Products 表：
    +-------------+----------+------------+
    | product_id  | low_fats | recyclable |
    +-------------+----------+------------+
    | 0           | Y        | N          |
    | 1           | Y        | Y          |
    | 2           | N        | Y          |
    | 3           | Y        | Y          |
    | 4           | N        | N          |
    +-------------+----------+------------+
    输出：
    +-------------+
    | product_id  |
    +-------------+
    | 1           |
    | 3           |
    +-------------+
    解释：
    只有产品 id 为 1 和 3 的产品，既是低脂又是可回收的产品。


###############################################################################
1757. Recyclable and Low Fat Products
###############################################################################

Table: ``Products``

:: 

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | product_id  | int     |
    | low_fats    | enum    |
    | recyclable  | enum    |
    +-------------+---------+

    product_id is the primary key (column with unique values) for this table.
    low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this \
    product is low fat and 'N' means it is not.
    recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this \
    product is recyclable and 'N' means it is not.
 

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in **any order**.

The result format is in the following example.
    

**Example 1:**

::

    Input: 
    Products table:
    +-------------+----------+------------+
    | product_id  | low_fats | recyclable |
    +-------------+----------+------------+
    | 0           | Y        | N          |
    | 1           | Y        | Y          |
    | 2           | N        | Y          |
    | 3           | Y        | Y          |
    | 4           | N        | N          |
    +-------------+----------+------------+
    Output: 
    +-------------+
    | product_id  |
    +-------------+
    | 1           |
    | 3           |
    +-------------+
    Explanation: Only products 1 and 3 are both low fat and recyclable.
