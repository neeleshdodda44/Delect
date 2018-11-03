var restaurants = "{{ restaurants | safe}}";
console.log(restaurants);

if (restaurants.length < 3) {
    console.error("Restaurants length was shorter than expected.")
}

var one = restaurants[0];
var two = restaurants[1];
var three = restaurants[2];

document.getElementById('first').innerHTML = one;
document.getElementById('second').innerHTML = two;
document.getElementById('third').innerHTML = three;