var sortColors = function(nums) {
     for(let k=1;k<=nums.length-1;k++){
          let current = nums[k];
          let position = k;
         while( position > 0 && nums[position-1] > current){
          nums[position] = nums[position -1];
          position -=1;
         }
         nums[position] =current;
      }
  return nums;
};
