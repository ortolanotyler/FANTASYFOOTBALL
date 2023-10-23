document.addEventListener("DOMContentLoaded", function () {
    // Select all stat cards
    const statCards = document.querySelectorAll(".stat-card");

    // Function to animate a card onto the page
    function animateCard(card, delay) {
        setTimeout(function () {
            card.style.transform = "translateX(0)"; // Animate translation
            card.style.color = "black"; // Animate text color
        }, delay);
    }

    // Animate each card with a delay when the button is clicked
    let delay = 0;
    const submitButton = document.getElementById("submitButton");
    submitButton.addEventListener("click", function () {
        statCards.forEach(function (card) {
            animateCard(card, delay);
            delay += 500; // Adjust delay as needed
        });
    });
});
