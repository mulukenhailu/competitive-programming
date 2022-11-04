function countSwaps(a) {
  let count=0;
      for (let i = 0; i < a.length; i++) {  
        for (let j = 0; j < a.length - 1; j++) {
            if (a[j] > a[j + 1]) {
              count +=1;
              const temp = a[j];
              a[j]=a[j+1];
              a[j+1]=temp;
            }
        } 
      }
  console.log("Array is sorted in "+ count+" swaps. ") ;
  console.log("First Element: "+Math.min.apply(null,a));
  console.log("second Element: "+Math.max.apply(null,a));
}
