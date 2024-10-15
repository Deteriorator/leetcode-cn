###############################################################################
584. 寻找用户推荐人
###############################################################################
..
    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    ", for paragraphs

表: Customer

::

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | name        | varchar |
    | referee_id  | int     |
    +-------------+---------+

    在 SQL 中，id 是该表的主键列。
    该表的每一行表示一个客户的 id、姓名以及推荐他们的客户的 id。

找出那些 **没有被** id = 2 的客户 **推荐** 的客户的姓名。

以 **任意顺序** 返回结果表。

结果格式如下所示。
 
**示例 1：**

::

    输入： 
    Customer 表:
    +----+------+------------+
    | id | name | referee_id |
    +----+------+------------+
    | 1  | Will | null       |
    | 2  | Jane | null       |
    | 3  | Alex | 2          |
    | 4  | Bill | null       |
    | 5  | Zack | 1          |
    | 6  | Mark | 2          |
    +----+------+------------+
    输出：
    +------+
    | name |
    +------+
    | Will |
    | Jane |
    | Bill |
    | Zack |
    +------+


###############################################################################
584. Find Customer Referee
###############################################################################

Table: Customer

::

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | name        | varchar |
    | referee_id  | int     |
    +-------------+---------+

    In SQL, id is the primary key column for this table.
    Each row of this table indicates the id of a customer, their name, and \
    the id of the customer who referred them.
    

Find the names of the customer that are **not referred by** the customer with \
``id = 2``.

Return the result table in ``any order``.

The result format is in the following example.

**Example 1:**

::

    Input: 
    Customer table:
    +----+------+------------+
    | id | name | referee_id |
    +----+------+------------+
    | 1  | Will | null       |
    | 2  | Jane | null       |
    | 3  | Alex | 2          |
    | 4  | Bill | null       |
    | 5  | Zack | 1          |
    | 6  | Mark | 2          |
    +----+------+------------+
    Output: 
    +------+
    | name |
    +------+
    | Will |
    | Jane |
    | Bill |
    | Zack |
    +------+
