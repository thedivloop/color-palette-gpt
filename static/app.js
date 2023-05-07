const form = document.querySelector("#form");
const container = document.querySelector(".container");

form.addEventListener("submit", function (e) {
	e.preventDefault();
	getColors(e.target.elements.query.value);
});

function getColors(query) {
	fetch("/palette", {
		method: "POST",
		headers: {
			"Content-Type": "application/x-www-form-urlencoded",
		},
		body: new URLSearchParams({
			query,
		}),
	})
		.then((response) => response.json())
		.then((data) => {
			createColorBoxes(data.colors, container);
		});
}

function createColorBoxes(colors, parent) {
	parent.innerHTML = "";
	for (const color of colors) {
		const div = document.createElement("div");
		div.classList.add("color");
		div.style.backgroundColor = color;
		div.style.width = `calc(100% /${colors.length})`;
		const span = document.createElement("span");
		span.innerText = color;
		div.appendChild(span);
		parent.appendChild(div);
	}
}
