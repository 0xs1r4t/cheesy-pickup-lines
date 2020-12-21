function createHeart() {
    const heart = document.createElement("div");
    heart.classList.add("heart");

    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = Math.random() * 2 + 3 + "s";

    heart.innerHTML="<img src=\"https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/237/heart-with-arrow_1f498.png\" width=\"20px\" height=\"20px\">";
    document.body.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, 5000);
}

setInterval(createHeart, 300);