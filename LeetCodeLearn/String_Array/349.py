class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))

    def intersection_2(self, nums1, nums2):
        nums1_dict =dict()
        for itm in nums1:
            if not itm in nums1_dict:
                nums1_dict[itm] = 1

        res = []
        for itm in nums2:
            if itm in nums1_dict:
                res.append(itm)
                del nums1_dict[itm]

        return res