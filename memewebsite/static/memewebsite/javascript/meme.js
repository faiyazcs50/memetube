var page_no = 1;
var has_next = true;
var before_number = 1;

document.addEventListener("DOMContentLoaded", () => {
    display_meme();

    window.onscroll = () => {
        if (window.scrollY + window.innerHeight >= document.body.offsetHeight) {
            display_meme();
        }
    };
});

function display_meme() {
    if (before_number != page_no || has_next == false) {
        return;
    }

    fetch(`memes/${page_no}`)
        .then((response) => response.json())
        .then((response) => {
            if (response == { has_next: false }) {
                return;
            }
            has_next = response[1]['has next'];
            var content = document.getElementById("content");
            response[0].forEach((element) => {
                var meme = document.createElement("div");
                meme.className = "meme";
                meme.innerHTML = `<img class="image" src="${element.meme}" />`;
                content.appendChild(meme);
            });

            page_no++;
        });

    before_number++;
}