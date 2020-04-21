int findMaxConsecutiveOnes(int* nums, int numsSize){
    int max = 0;
    int tmp = 0;
    int i = 0;
    for (i = 0; i < numsSize; i++) {
        if (nums[i] == 1) {
            tmp = tmp + 1;
            if (tmp >= max) {
                max = tmp;
            }
        }
        else {
            if (tmp >= max) {
                max = tmp;
            }
            tmp = 0;
        }
    }
    return max;
}
