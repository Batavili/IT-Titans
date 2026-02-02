const page = document.getElementById("page");
const title = document.getElementById("title");
const text = document.getElementById("text");
const dots = document.querySelectorAll(".dot");
const link = document.getElementById("text");

const sections = [
    {
        bg: "#1C1C1C",
        title: "IT Titans",
        text: "Bővebben rólunk",
        link: "ITT.html"
    },
    {
        bg: "#552222",
        title: "Cyber Osynt",
        text: "Bővebben partnerünkről",
        link: "https://ceg.atanarur.hu/cyberosint/"
    },
    {
        bg: "#727272",
        title: "Commit & Pray",
        text: "Bővebben partnerünkről",
        link: "https://ceg.atanarur.hu/cnp/"
    },
    {
        bg: "#225534",
        title: "Horizon Code",
        text: "Bővebben partnerünkről",
        link: "https://ceg.atanarur.hu/horizoncode/"
    }
];

dots.forEach(dot => {
  dot.addEventListener("click", () => {
    dots.forEach(d => d.classList.remove("active"));
    dot.classList.add("active");

    const index = dot.dataset.index;

    page.style.backgroundColor = sections[index].bg;
    title.textContent = sections[index].title;
    link.textContent = sections[index].text;
    link.href = sections[index].link;
  });
});
