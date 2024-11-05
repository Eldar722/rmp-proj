function cakeMe() {
    let menulist = document.getElementById("menu-list");
    menulist.style.display = menulist.style.display === "none" ? "block" : "none";
}

document.getElementById('checkout-button').addEventListener('click', function() {
    document.getElementById('delivery-form').submit();
});