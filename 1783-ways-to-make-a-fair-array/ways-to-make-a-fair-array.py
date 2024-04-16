class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even = sum(nums[::2])  # Total sum of elements at even indices
        total_odd = sum(nums[1::2])  # Total sum of elements at odd indices
        prefix_even = prefix_odd = 0  # Initialize prefix sums for even and odd indices
        count = 0  # Counter for fair indices

        for i, num in enumerate(nums):
            if i % 2 == 0:
                total_even -= num  # Adjust even sum for removed element
            else:
                total_odd -= num  # Adjust odd sum for removed element

            # Calculate new sums as if current element is removed
            new_even_sum = prefix_even + total_odd
            new_odd_sum = prefix_odd + total_even

            if new_even_sum == new_odd_sum:
                count += 1  # Increment count if new sums are equal

            # Update prefix sums for the next iteration
            if i % 2 == 0:
                prefix_even += num
            else:
                prefix_odd += num

        return count