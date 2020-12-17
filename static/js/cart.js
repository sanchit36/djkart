const cartSection = document.getElementById("cart-section");
const cartIcon = document.getElementById("cart-icon");

$(document).on("click", ".update-btn", (e) => {
  const { productid, action } = e.target.dataset;
  if (user != "AnonymousUser") {
    updateUserOrder(productid, action);
  } else {
    updateCookieItem(productid, action);
  }
});

const updateCookieItem = (productid, action) => {
  if (action == "add") {
    if (cart[productid] == undefined) {
      cart[productid] = { quantity: 1 };
    } else {
      cart[productid]["quantity"] += 1;
    }
  }

  if (action == "remove") {
    cart[productid]["quantity"] -= 1;

    if (cart[productid]["quantity"] <= 0) {
      delete cart[productid];
    }
  }
  document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
  updateUi();
};

const updateUserOrder = (productid, action) => {
  url = "/update_cart/";
  fetch(url, {
    method: "POST",
    headers: {
      "Context-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productid, action }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (cartSection != undefined)
        cartSection.innerHTML = data["cart_section"];
      cartIcon.innerHTML = data["cart_icon"];
    })
    .catch((err) => console.log(err));
};

const updateUi = () => {
  url = "/update_cart/";
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      if (cartSection != undefined)
        cartSection.innerHTML = data["cart_section"];
      cartIcon.innerHTML = data["cart_icon"];
    })
    .catch((err) => console.log(err));
};
