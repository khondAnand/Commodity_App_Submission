let gold_change = document.getElementById("gold_change");
let gold_change_per = document.getElementById("gold_change_per");
let sil_change = document.getElementById("sil_change");
let sil_change_per = document.getElementById("sil_change_per");
let c_change = document.getElementById("c_change");
let c_change_per = document.getElementById("c_change_per");
let n_change = document.getElementById("n_change");
let n_change_per = document.getElementById("n_change_per");



function myFunction(x) {
    if (x.innerText < 0) {
      x.style.color ='red';
    }else{
        x.style.color ='green'; 
    }
  }

  myFunction(gold_change);
  myFunction(gold_change_per);
  myFunction(sil_change);
  myFunction(sil_change_per);
  myFunction(c_change);
  myFunction(c_change_per);
  myFunction(n_change);
  myFunction(n_change_per);


  function AutoRefresh( t ) {
    setTimeout("location.reload(true);", t);
 }

