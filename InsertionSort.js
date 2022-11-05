
function insertionsort(n,arr){
     const current= arr[n-1];
     for(let i=n-2;i>=0;i--){
      if(arr[i]>current ){
        arr[i+1]=arr[i];
          console.log(arr.join(" "));
      }
      if (i == 0 && arr[0]> current){
        a[0]=current;
      }
      else if(arr[i]<current){
         arr[i+1]=current;
         i=-1;
      }
     }
     console.log(arr.join(" "));
}
