window.addEventListener('scroll', scroling);


function scroling(){
    
    console.log(pageYOffset);
    show();
}


function show(){
   var nums = document.querySelectorAll('.num');
   nums.forEach((num)=>{
    num.classList.remove('hide');
    num.classList.add('show')
   })
}