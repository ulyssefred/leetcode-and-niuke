class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes = (votes +1 if x == num else votes -1)
        return x

    # 哈希表统计法： 遍历数组
    # nums ，用
    # HashMap
    # 统计各数字的数量，即可找出
    # 众数 。此方法时间和空间复杂度均为
    # O(N)
    # O(N) 。
    # 数组排序法： 将数组
    # nums
    # 排序，数组中点的元素
    # 一定为众数。

    # 摩尔投票法： 核心理念为
    # 票数正负抵消 。此方法时间和空间复杂度分别为
    # O(N)
    # O(N)
    # 和
    # O(1)
    # O(1) ，为本题的最佳解法。
    # 摩尔投票法：
    # 设输入数组
    # nums
    # 的众数为
    # xx ，数组长度为
    # nn 。
    #
    # 推论一： 若记
    # 众数
    # 的票数为 + 1 + 1 ，非众数
    # 的票数为 - 1−1 ，则一定有所有数字的
    # 票数和 > 0 > 0 。
    #
    # 推论二： 若数组的前
    # aa
    # 个数字的
    # 票数和 = 0 = 0 ，则
    # 数组剩余(n - a)(n−a) 个数字的
    # 票数和一定仍 > 0 > 0 ，即后(n - a)(n−a) 个数字的
    # 众数仍为
    # xx 。
    #
    #
    #
    # 根据以上推论，记数组首个元素为
    # n_1n
    # 1
    # ​
    # ，众数为
    # xx ，遍历并统计票数。当发生
    # 票数和 = 0 = 0
    # 时，剩余数组的众数一定不变 ，这是由于：
    #
    # 当
    # n_1 = xn
    # 1
    # ​
    # =x ： 抵消的所有数字，有一半是众数
    # xx 。
    # 当
    # n_1 \neq
    # xn
    # 1
    # ​
    #
    # 
    # ​
    # =x ： 抵消的所有数字，众数
    # xx
    # 的数量为一半或
    # 0
    # 个。
    # 利用此特性，每轮假设发生
    # 票数和 = 0 = 0
    # 都可以
    # 缩小剩余数组区间 。当遍历完成时，最后一轮假设的数字即为众数。
    #
    # 算法流程:
    # 初始化： 票数统计
    # votes = 0 ， 众数
    # x；
    # 循环： 遍历数组
    # nums
    # 中的每个数字
    # num ；
    # 当
    # 票数
    # votes
    # 等于
    # 0 ，则假设当前数字
    # num
    # 是众数；
    # 当
    # num = x
    # 时，票数
    # votes
    # 自增
    # 1 ；当
    # num != x
    # 时，票数
    # votes
    # 自减
    # 1 ；
    # 返回值： 返回
    # x
    # 即可；
    #
    # 作者：jyd
    # 链接：https: // leetcode - cn.com / problems / shu - zu - zhong - chu - xian - ci - shu - chao - guo - yi - ban - de - shu - zi - lcof / solution / mian - shi - ti - 39 - shu - zu - zhong - chu - xian - ci - shu - chao - 3 /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。