function clicked(){
  dropdown=document.getElementById('dropdown').style
  navLinks=document.getElementsByTagName('nav')[0].style
  if (dropdown.transform=="rotateX(180deg)") {
    dropdown.transform="rotateX(0deg)"
    navLinks.display="none"
  } else {
    dropdown.transform="rotateX(180deg)"
    navLinks.display="block"
  }

}
