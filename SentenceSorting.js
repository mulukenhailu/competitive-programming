var sortSentence = function(s) {
    const arr=s.split(" ");
      const meaning=[];
      for(let i=0;i<=200;i++){
            arr.forEach(function(word){
                  let str=word.toString();
                  if(str. charAt(str. length - 1) === i.toString()){
                      meaning.push(str.slice(0,-1));
                  }
            })  
      }
    return (meaning.join(" "));
};
