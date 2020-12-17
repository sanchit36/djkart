const sameAddress = document.getElementById("same-address");
const formEl = document.getElementById("form");
const csrf = document.querySelector("[name=csrfmiddlewaretoken]").value;
const makePayment = document.getElementById("make-payment");

sameAddress.addEventListener("click", (e) => {
  if (sameAddress.checked == true) {
    let address = formEl.address_s.value;
    let city = formEl.city_s.value;
    let state = formEl.state_s.value;
    let zipCode = formEl.zip_code_s.value;

    formEl.address_b.value = address;
    formEl.city_b.value = city;
    formEl.state_b.value = state;
    formEl.zip_code_b.value = zipCode;
  } else {
    formEl.address_b.value = "";
    formEl.city_b.value = "";
    formEl.state_b.value = "";
    formEl.zip_code_b.value = "";
  }
});

formEl.addEventListener("submit", (e) => {
  e.preventDefault();
  document.getElementById("payment-info").classList.remove("hidden");
  document.getElementById("form-btn").classList.add("hidden");
});

const submitFormData = (e) => {
  console.log("Payment button clicked");
  var userFormData = {
    first_name: null,
    last_name: null,
    email: null,
    phone_number: null,
    total: total,
  };

  var shippingInfo = {
    address: null,
    city: null,
    state: null,
    zipcode: null,
  };

  var billingInfo = {
    address: null,
    city: null,
    state: null,
    zipcode: null,
  };
  if (user == "AnonymousUser") {
    userFormData.first_name = formEl.first_name.value;
    userFormData.last_name = formEl.last_name.value;
    userFormData.email = formEl.email.value;
    userFormData.phone_number = formEl.phone_number.value;

    shippingInfo.address = formEl.address_s.value;
    shippingInfo.city = formEl.city_s.value;
    shippingInfo.state = formEl.state_s.value;
    shippingInfo.zipcode = formEl.zip_code_s.value;

    billingInfo.address = formEl.address_b.value;
    billingInfo.city = formEl.city_b.value;
    billingInfo.state = formEl.state_b.value;
    billingInfo.zipcode = formEl.zip_code_b.value;
  } else {
    shippingInfo.address = formEl.address_s.value;
    shippingInfo.city = formEl.city_s.value;
    shippingInfo.state = formEl.state_s.value;
    shippingInfo.zipcode = formEl.zip_code_s.value;

    billingInfo.address = formEl.address_b.value;
    billingInfo.city = formEl.city_b.value;
    billingInfo.state = formEl.state_b.value;
    billingInfo.zipcode = formEl.zip_code_b.value;
  }

  const url = "/process_order/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrf,
    },
    body: JSON.stringify({
      form: userFormData,
      shipping: shippingInfo,
      billing: billingInfo,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      console.log("Success: ", data);
      alert("Transaction complete");

      cart = {};
      document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
      window.location.href = "/store/";
    })
    .catch((err) => console.log(err));
};

makePayment.addEventListener("click", submitFormData);
