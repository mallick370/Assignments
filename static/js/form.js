let part1 = document.querySelector(".part1")
let part2 = document.querySelector(".part2")
let nextBtn = document.querySelector(".nextBtn")
part2.style.display = "none";

nextBtn.addEventListener("click", nextPart)
function nextPart(){
    if (validation()===true){
        part1.style.display = "none"
        part2.style.display = "block"
    }
}
function validation(){
    let f_name = document.forms["subForm"]["f_name"]
    let l_name = document.forms["subForm"]["l_name"]
    let univ = document.forms["subForm"]["university"]
    let roll = document.forms["subForm"]["roll"]

    if(f_name.value===""||l_name.value===""||univ.value===""||roll.value===""){
        nextBtn.style.backgroundColor="#ff6347"
        alert("Please fill us all the fields")
        return false
    }
    else {
        return true
    }
}

function passwordValidation(){

}