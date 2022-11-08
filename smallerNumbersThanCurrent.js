var smallerNumbersThanCurrent = function(nums) {
     let counter=0;
    const arr=[];
    for(let i=0;i<=nums.length-1;i++){
        for(let k=0;k<=nums.length-1;k++){
           if(nums[i]>nums[k]){
            counter++;
           }
       }
       arr[i]=counter;
       counter=0;
    } 
    return arr;
    
};
