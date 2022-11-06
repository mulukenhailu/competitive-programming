function countingSort(arr){
    let counter=0;
    const freq=[];
    freq.length=100;
    freq.fill(0);
            for(let i=0;i<100;i++){
                    arr.forEach(function(item){
                        if(item === i){
                        counter++;
                        freq[i]=counter;
                    }
                })
                counter=0;
            }
        return freq;
};
