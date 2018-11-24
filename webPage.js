let pizzas = 0;
let size = "";
let toppings = 0;
let address = [""];
let radius = 0; //radius of search in km

function select(){ //pull the selected choice
  pizzas = document.getElementById("pizzaNumber");
  let numSelected = pizzas.options[pizzas.selectedIndex].value;
  size = document.getElementById("pizzaSize");
  let sizeSelected = size.options[size.selectedIndex].value;
  toppings = document.getElementById("pizzaToppings");
  let topSelected = toppings.options[toppings.selectedIndex].value;
  radius = document.getElementById("radius");
  let radiusSelected = radius.options[radius.selectedIndex].value;
  address = document.getElementById("message").value;

  console.log(numSelected);
  console.log(sizeSelected);
  console.log(topSelected);
  console.log(radiusSelected);
  console.log(address);


}
