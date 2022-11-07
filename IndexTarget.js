 
var targetIndices = function(nums, target) {
    const  b=[];
    const TargetArray=[];
    let i=0;
    while(i <= nums.length-1){
        let fsmall=Math.min(...nums);
        let index=nums.indexOf(Math.min(...nums));
        if(index !== 0){
            const temp=nums[0];
            nums[0]=fsmall;
            nums[index]=temp;
        }
        let shifted= nums.shift();
            b.push(shifted);
    }
        for(let k=0;k<=b.length-1;k++){
            if(b[k] === target){
                TargetArray.push(k);
            }
    }
     i++;
    return TargetArray;
};
