# Vscode

## Snippets

Use [snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets) to define macros on vscode (search for configure snippets)

```json title="markdown.json"
	"Generate code block":{
		"prefix":"cb",
		"body":[
			"```${1:langage} title=\"${2:}\"",
			"${3:code}",
			"```",
			""
		],
		"description":"generate code block"
	},
	"Generate flashcard": {
		"prefix": "fc",
		"body": [
			"??? question \"${1:Question Text} [](){.fbutton .ok}[](){.fbutton .nok}\"",
			"    ${2:$CLIPBOARD}",
			"    ##### id: $RANDOM_HEX, box: 1, score: 0/0, next: $CURRENT_DATE/$CURRENT_MONTH/$CURRENT_YEAR, last: $CURRENT_DATE/$CURRENT_MONTH/$CURRENT_YEAR",
			""
		],
		"description": "generate flashcard"
	}
```

??? question "How to define macros on vscode? [](){.fbutton .ok}[](){.fbutton .nok}"
    Use snippets (search for configure snippets)
    ```json title="markdown.json"
	"Generate code block":{
		"prefix":"cb",
		"body":[
			"```${1:langage} title=\"${2:}\"",
			"${3:code}",
			"```",
			""
		],
		"description":"generate code block"
	}
    ```
    ##### id: a2faaa, box: 3, score: 2/2, next: 21/10/2023, last: 15/10/2023
