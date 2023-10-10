const katexMacros = {
    "\\res": "\\textcolor{orangered}{\\boxed{#1}}" // important results
};

const katexConfig = {
    delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
        { left: "\\(", right: "\\)", display: false },
        { left: "\\[", right: "\\]", display: true }
    ],
    macros: katexMacros
};

// Subscribe to document events and render KaTeX
document$.subscribe(({ body }) => {
    renderMathInElement(body, katexConfig);
});
