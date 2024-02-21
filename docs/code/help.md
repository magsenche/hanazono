## Markdown

- [Markdown & latex](https://ashki23.github.io/markdown-latex.html)
- [Markdown preview enchanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/)
  - `~/.mume/style.less` for general styles
  - `~/.mume/parser.js` for advanced parsing
  - `./styles.css` for workspace styles, along with `{"markdown.styles": ["styles.css"]}` in the `settings.json`

- Use url hash to target specific and add custom style:
  - in the `style.less`
    ```css
    img[src*="#thumbnail"] {width: 20%;}
    ```
  - in the `.md`
    ```markdown
    ![alt](url#thumbnail)
    ```
- Add images to mardkown and save in `supp/filename/`
  - `Shift + Print` to take area screenshot
  - Rename & copy to clipboard
  - Paste in `filename.md`
  -
    ```json
    "markdown.copyFiles.destination": {
        "/*": "${documentDirName}/supp/${documentBaseName}/${fileName}"
    },
    ```
