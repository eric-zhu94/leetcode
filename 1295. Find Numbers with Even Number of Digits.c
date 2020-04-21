int findNumbers(int* nums, int numsSize){
    int count = 0;
    int i = 0;
    for (i = 0; i < numsSize; i++) {
        int tmp = nums[i];
        int digits = 0;
        while (tmp != 0) {
            tmp = tmp / 10;
            digits += 1;
        }
        if (digits % 2 == 0) {
            count += 1;
        }
        
    }
    return count;
}
