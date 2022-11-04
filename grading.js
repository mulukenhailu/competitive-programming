grades=[73, 67, 38,33];
function gradingstudents(grades){
  return  grades.map(function(grade){
      const nextnumber = Math.ceil((grade+1)/5)*5;
      if((nextnumber - grade <3 ) && grade >=38){
        return nextnumber;
      }
      else
       return grade ;
  });
}
console.log(gradingstudents(grades))
